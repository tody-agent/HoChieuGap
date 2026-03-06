#!/usr/bin/env python3
"""
HoChieuGap Content Factory — AI Article Generator with Real-Time Dashboard
Usage:
  python3 generate-200-ai.py                          # Interactive mode (asks for API key)
  GEMINI_API_KEY=xxx python3 generate-200-ai.py       # With env key
  python3 generate-200-ai.py --batch 10               # Limit to 10 articles
  python3 generate-200-ai.py --priority P0             # Only P0 articles
  python3 generate-200-ai.py --cluster visa            # Only visa cluster
  python3 generate-200-ai.py --dry-run                 # Validate topics only
  python3 generate-200-ai.py --audit-only              # Audit existing articles only
"""
import os, sys, json, time, re, argparse, threading, signal
from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime

# ─── Configuration ───
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(SCRIPT_DIR, '..', '..')
BLOG_DIR = os.path.join(SCRIPT_DIR, '..', 'src', 'content', 'blog')
TOPICS_FILE = os.path.join(PROJECT_ROOT, 'topics-queue', 'topics-200.json')
STATE_FILE = os.path.join(PROJECT_ROOT, '.content-factory-state.json')
EVENTS_FILE = os.path.join(PROJECT_ROOT, 'logs', 'events.jsonl')
DASHBOARD_HOST = 'content-factory'
DASHBOARD_PORT = 5050
DASHBOARD_URL = f'http://{DASHBOARD_HOST}:{DASHBOARD_PORT}'
RATE_LIMIT_SLEEP = 8  # seconds between API calls
MODEL = "gemini-2.5-flash"

# ─── State Manager ───
class StateManager:
    def __init__(self):
        self.state = {
            "phase": "init", "total": 0, "completed": 0, "failed": 0,
            "current_article": "", "started_at": "", "errors": [],
            "token_usage": {"input": 0, "output": 0, "cost_usd": 0.0},
            "paused": False, "pause_reason": ""
        }
        os.makedirs(os.path.dirname(EVENTS_FILE), exist_ok=True)

    def update(self, **kwargs):
        self.state.update(kwargs)
        self._write_state()

    def add_error(self, slug, error):
        self.state["errors"].append({"slug": slug, "error": str(error)[:200], "time": _now()})
        self.state["failed"] += 1
        self._write_state()

    def add_tokens(self, input_t, output_t):
        self.state["token_usage"]["input"] += input_t
        self.state["token_usage"]["output"] += output_t
        # Gemini 2.0 Flash pricing: $0.10/1M input, $0.40/1M output
        self.state["token_usage"]["cost_usd"] = round(
            self.state["token_usage"]["input"] * 0.0000001 +
            self.state["token_usage"]["output"] * 0.0000004, 4)
        self._write_state()

    def _write_state(self):
        tmp = STATE_FILE + '.tmp'
        with open(tmp, 'w') as f:
            json.dump(self.state, f, ensure_ascii=False, indent=2)
        os.replace(tmp, STATE_FILE)

    def log_event(self, event_type, data=""):
        with open(EVENTS_FILE, 'a') as f:
            f.write(json.dumps({"type": event_type, "data": data, "time": _now()}, ensure_ascii=False) + '\n')

def _now():
    return datetime.now().strftime("%H:%M:%S")

# ─── Dashboard Server ───
DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>🏭 HoChieuGap Content Factory</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Inter',system-ui,sans-serif;background:#0a0a1a;color:#e0e0e0;min-height:100vh}
.header{background:linear-gradient(135deg,#1a1a2e,#16213e);padding:20px 30px;border-bottom:1px solid #2a2a4a;display:flex;justify-content:space-between;align-items:center}
.header h1{font-size:1.4rem;color:#fff}.header .badge{background:#e74c3c;padding:4px 12px;border-radius:20px;font-size:.8rem;font-weight:600}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;padding:20px 30px;max-width:1200px;margin:0 auto}
.card{background:#12122a;border:1px solid #2a2a4a;border-radius:12px;padding:20px}
.card h3{color:#8ab4f8;font-size:.9rem;margin-bottom:12px;text-transform:uppercase;letter-spacing:1px}
.progress-bar{background:#1a1a3a;border-radius:8px;height:24px;overflow:hidden;margin:8px 0}
.progress-fill{height:100%;background:linear-gradient(90deg,#e74c3c,#f39c12);border-radius:8px;transition:width .5s ease;display:flex;align-items:center;justify-content:center;font-size:.75rem;font-weight:700;min-width:30px}
.stat{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #1a1a3a;font-size:.9rem}
.stat .label{color:#888}.stat .value{color:#fff;font-weight:600}
.log-box{max-height:300px;overflow-y:auto;font-family:'JetBrains Mono',monospace;font-size:.8rem;line-height:1.6;padding:8px;background:#0a0a15;border-radius:8px}
.log-line{padding:2px 4px}.log-line.error{color:#e74c3c}.log-line.success{color:#2ecc71}.log-line.info{color:#8ab4f8}
.full-width{grid-column:1/-1}
.error-card{background:#2a1515;border:1px solid #e74c3c;border-radius:8px;padding:12px;margin:6px 0;font-size:.85rem}
.error-card .slug{color:#f39c12;font-weight:600}.error-card .msg{color:#e0e0e0;margin-top:4px}
.paused-banner{background:linear-gradient(135deg,#f39c12,#e74c3c);padding:16px 30px;text-align:center;font-weight:700;font-size:1rem;display:none}
.paused-banner.show{display:block}
.token-input-area{display:none;background:#1a1a2e;padding:20px 30px;border:2px solid #f39c12;border-radius:12px;margin:16px 30px}
.token-input-area.show{display:block}
.token-input-area input{width:60%;padding:10px;border-radius:8px;border:1px solid #2a2a4a;background:#0a0a1a;color:#fff;font-size:1rem;margin-right:10px}
.token-input-area button{padding:10px 24px;border-radius:8px;border:none;background:#e74c3c;color:#fff;font-weight:700;cursor:pointer;font-size:1rem}
.token-input-area button:hover{background:#c0392b}
@media(max-width:768px){.grid{grid-template-columns:1fr}}
</style></head><body>
<div class="header"><h1>🏭 HoChieuGap Content Factory</h1><div class="badge" id="phase">INIT</div></div>
<div class="paused-banner" id="paused-banner">⚠️ PIPELINE TẠM DỪNG — <span id="pause-reason"></span></div>
<div class="token-input-area" id="token-area">
  <h3 style="color:#f39c12;margin-bottom:10px">🔑 Nhập Gemini API Key mới để tiếp tục</h3>
  <input type="text" id="new-token" placeholder="AIzaSy...">
  <button onclick="submitToken()">▶ Chạy tiếp</button>
  <p style="color:#888;margin-top:8px;font-size:.8rem">Pipeline sẽ resume từ bài viết cuối cùng đã hoàn thành.</p>
</div>
<div class="grid">
  <div class="card"><h3>📊 Tiến Độ</h3>
    <div class="progress-bar"><div class="progress-fill" id="progress" style="width:0%">0%</div></div>
    <div class="stat"><span class="label">Hoàn thành</span><span class="value" id="completed">0/0</span></div>
    <div class="stat"><span class="label">Thất bại</span><span class="value" id="failed" style="color:#e74c3c">0</span></div>
    <div class="stat"><span class="label">Đang viết</span><span class="value" id="current" style="color:#f39c12">—</span></div>
    <div class="stat"><span class="label">Bắt đầu</span><span class="value" id="started">—</span></div>
  </div>
  <div class="card"><h3>💰 Token Usage</h3>
    <div class="stat"><span class="label">Input tokens</span><span class="value" id="input-tokens">0</span></div>
    <div class="stat"><span class="label">Output tokens</span><span class="value" id="output-tokens">0</span></div>
    <div class="stat"><span class="label">Chi phí ước tính</span><span class="value" id="cost">$0.0000</span></div>
    <div class="stat"><span class="label">Model</span><span class="value">gemini-2.0-flash</span></div>
  </div>
  <div class="card full-width"><h3>📋 Event Log</h3><div class="log-box" id="log"></div></div>
  <div class="card full-width" id="errors-card" style="display:none"><h3>❌ Errors</h3><div id="errors"></div></div>
</div>
<script>
function poll(){
  fetch('/api/state').then(r=>r.json()).then(s=>{
    const pct=s.total?Math.round(s.completed/s.total*100):0;
    document.getElementById('progress').style.width=pct+'%';
    document.getElementById('progress').textContent=pct+'%';
    document.getElementById('completed').textContent=s.completed+'/'+s.total;
    document.getElementById('failed').textContent=s.failed;
    document.getElementById('current').textContent=s.current_article||'—';
    document.getElementById('started').textContent=s.started_at||'—';
    document.getElementById('phase').textContent=s.phase.toUpperCase();
    document.getElementById('input-tokens').textContent=s.token_usage.input.toLocaleString();
    document.getElementById('output-tokens').textContent=s.token_usage.output.toLocaleString();
    document.getElementById('cost').textContent='$'+s.token_usage.cost_usd.toFixed(4);
    const pb=document.getElementById('paused-banner');
    const ta=document.getElementById('token-area');
    if(s.paused){pb.classList.add('show');document.getElementById('pause-reason').textContent=s.pause_reason;
      if(s.pause_reason.includes('token')||s.pause_reason.includes('API key')||s.pause_reason.includes('quota'))ta.classList.add('show');
    }else{pb.classList.remove('show');ta.classList.remove('show')}
    if(s.errors.length){document.getElementById('errors-card').style.display='block';
      document.getElementById('errors').innerHTML=s.errors.slice(-5).map(e=>
        '<div class="error-card"><span class="slug">'+e.slug+'</span> <span style="color:#888">'+e.time+'</span><div class="msg">'+e.error+'</div></div>'
      ).join('')}
  }).catch(()=>{});
  fetch('/api/events').then(r=>r.text()).then(t=>{
    const box=document.getElementById('log');
    const lines=t.trim().split('\\n').filter(Boolean).slice(-50);
    box.innerHTML=lines.map(l=>{try{const e=JSON.parse(l);const cls=e.type==='error'?'error':e.type==='success'?'success':'info';
      return '<div class="log-line '+cls+'"><span style="color:#555">'+e.time+'</span> ['+e.type+'] '+e.data+'</div>'}catch{return ''}}).join('');
    box.scrollTop=box.scrollHeight;
  }).catch(()=>{});
}
function submitToken(){
  const key=document.getElementById('new-token').value.trim();
  if(!key)return alert('Vui lòng nhập API key');
  fetch('/api/resume',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({key})})
    .then(r=>r.json()).then(d=>{if(d.ok)location.reload()}).catch(e=>alert('Error: '+e));
}
setInterval(poll,2000);poll();
</script></body></html>"""

class DashboardHandler(SimpleHTTPRequestHandler):
    state_mgr = None
    resume_callback = None

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(DASHBOARD_HTML.encode())
        elif self.path == '/api/state':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            try:
                with open(STATE_FILE, 'r') as f:
                    self.wfile.write(f.read().encode())
            except:
                self.wfile.write(b'{}')
        elif self.path == '/api/events':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            try:
                with open(EVENTS_FILE, 'r') as f:
                    self.wfile.write(f.read().encode())
            except:
                self.wfile.write(b'')
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/api/resume':
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length))
            new_key = body.get('key', '')
            if new_key and DashboardHandler.resume_callback:
                DashboardHandler.resume_callback(new_key)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"ok": True}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, *args):
        pass  # Suppress server logs

def start_dashboard(state_mgr, resume_cb):
    DashboardHandler.state_mgr = state_mgr
    DashboardHandler.resume_callback = resume_cb
    import socket
    for port in [DASHBOARD_PORT, DASHBOARD_PORT + 1, DASHBOARD_PORT + 2]:
        try:
            server = HTTPServer(('0.0.0.0', port), DashboardHandler)
            server.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            t = threading.Thread(target=server.serve_forever, daemon=True)
            t.start()
            return server, port
        except OSError:
            continue
    print("⚠️ Could not start dashboard (ports 5050-5052 busy)")
    return None, 0

# ─── System Prompt for Gemini ───
SYSTEM_PROMPT = """Bạn là content writer chuyên nghiệp cho HoChieuGap — dịch vụ hộ chiếu gấp uy tín tại Việt Nam.

RULES:
1. Viết bài tiếng Việt, 1200-2000 từ
2. Tone: chuyên nghiệp, ấm áp, đáng tin cậy
3. CẤU TRÚC BẮT BUỘC:
   - Mở đầu hấp dẫn (2-3 câu)
   - ## Tổng quan, ## Đối tượng áp dụng
   - ## Hồ sơ cần chuẩn bị (bảng markdown)
   - ## Quy trình thực hiện (4 bước)
   - ## Chi phí (bảng markdown với giá: Gấp 24h từ 2.3-5.5tr, 48h từ 1.6-4.5tr, 72h từ 1.1-4tr)
   - ## Câu hỏi thường gặp (3+ câu hỏi dạng H3)
   - ## Kết luận + CTA
4. CTA cuối bài:
   - 📞 Hotline: **0909 123 456**
   - 💬 Zalo: [Nhắn tin ngay](https://zalo.me/0909123456)
   - 📝 [Gửi yêu cầu online](https://hochieugap.vn/#contact)
5. KHÔNG dùng: lorem ipsum, {{}}, TODO, FIXME
6. KHÔNG lặp nội dung y hệt giữa các bài
7. Tự nhiên, hữu ích, không spam keyword
8. Internal link tới /passport-photo/ khi nhắc đến ảnh HC
9. CHỈ output markdown body (KHÔNG output frontmatter)"""

# ─── Article Generator ───
def generate_article(topic, api_key):
    """Call Gemini API to generate article content. Returns (body, input_tokens, output_tokens)."""
    from google import genai
    client = genai.Client(api_key=api_key)

    prompt = f"""Viết bài SEO cho HoChieuGap:
TITLE: {topic['title']}
DESCRIPTION: {topic['description']}
CLUSTER: {topic['cluster']}
KEYWORDS: {', '.join(topic['keywords'])}
CONTEXT: {topic.get('prompt_context', '')}

Viết bài markdown đầy đủ theo cấu trúc đã quy định. CHỈ output nội dung markdown body."""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config={"system_instruction": SYSTEM_PROMPT}
    )
    body = response.text.strip()

    # Extract token usage
    usage = response.usage_metadata
    in_tok = usage.prompt_token_count or 0
    out_tok = usage.candidates_token_count or 0
    return body, in_tok, out_tok

def build_frontmatter(topic):
    slug = topic['slug']
    related = []  # Will be filled by crosslinks script
    fm = {
        "title": topic['title'],
        "description": topic['description'][:160],
        "pubDate": "2026-03-07",
        "cluster": topic['cluster'],
        "keywords": topic['keywords'],
        "isPillar": topic.get('isPillar', False),
        "readingTime": topic.get('readingTime', 5),
        "relatedSlugs": related
    }
    lines = ["---"]
    lines.append(f"title: '{fm['title']}'")
    lines.append(f"description: '{fm['description']}'")
    lines.append(f"pubDate: {fm['pubDate']}")
    lines.append(f"cluster: '{fm['cluster']}'")
    lines.append(f"keywords: {json.dumps(fm['keywords'], ensure_ascii=False)}")
    lines.append(f"isPillar: {'true' if fm['isPillar'] else 'false'}")
    lines.append(f"readingTime: {fm['readingTime']}")
    lines.append(f"relatedSlugs: {json.dumps(related)}")
    lines.append("---")
    return '\n'.join(lines)

def audit_article(body):
    """Simple audit. Returns list of issues."""
    issues = []
    for pattern in ['lorem ipsum', '{{', '}}', 'TODO', 'FIXME']:
        if pattern.lower() in body.lower():
            issues.append(f"Contains forbidden pattern: {pattern}")
    headings = re.findall(r'^##\s', body, re.MULTILINE)
    if len(headings) < 3:
        issues.append(f"Too few headings: {len(headings)} (min 3)")
    if '## Câu hỏi thường gặp' not in body and '## FAQ' not in body:
        issues.append("Missing FAQ section")
    if '0909 123 456' not in body and 'hochieugap' not in body.lower():
        issues.append("Missing CTA")
    return issues

# ─── Main Pipeline ───
def main():
    parser = argparse.ArgumentParser(description='HoChieuGap Content Factory')
    parser.add_argument('--batch', type=int, default=0, help='Limit articles per run')
    parser.add_argument('--priority', choices=['P0','P1','P2'], help='Filter by priority')
    parser.add_argument('--cluster', help='Filter by cluster')
    parser.add_argument('--dry-run', action='store_true', help='Validate topics only')
    parser.add_argument('--audit-only', action='store_true', help='Audit existing articles')
    parser.add_argument('--no-dashboard', action='store_true', help='Disable dashboard')
    args = parser.parse_args()

    # Load topics
    with open(TOPICS_FILE, 'r', encoding='utf-8') as f:
        topics = json.load(f)

    # Filter
    if args.priority:
        topics = [t for t in topics if t['priority'] == args.priority]
    if args.cluster:
        topics = [t for t in topics if t['cluster'] == args.cluster]

    # Skip already generated
    existing = set()
    if os.path.isdir(BLOG_DIR):
        existing = {f.replace('.md','') for f in os.listdir(BLOG_DIR) if f.endswith('.md')}
    pending = [t for t in topics if t['slug'] not in existing]

    if args.batch > 0:
        pending = pending[:args.batch]

    # Dry run
    if args.dry_run:
        print(f"📋 Topics loaded: {len(topics)} total, {len(pending)} pending")
        collisions = [t['slug'] for t in topics if t['slug'] in existing]
        if collisions:
            print(f"⚠️  Collisions with existing posts: {collisions[:10]}")
        print("✅ Dry run complete.")
        return

    # Audit only
    if args.audit_only:
        print("🔍 Auditing existing articles...")
        issues_count = 0
        for f in sorted(os.listdir(BLOG_DIR)):
            if not f.endswith('.md'): continue
            with open(os.path.join(BLOG_DIR, f), 'r', encoding='utf-8') as fh:
                content = fh.read()
            body = content.split('---', 2)[2] if content.count('---') >= 2 else content
            issues = audit_article(body)
            if issues:
                issues_count += 1
                print(f"  ❌ {f}: {', '.join(issues)}")
        print(f"\n{'✅ All clean!' if not issues_count else f'❌ {issues_count} articles with issues'}")
        return

    # Get API key
    api_key = os.environ.get('GEMINI_API_KEY', '')
    if not api_key:
        api_key = input("🔑 Nhập GEMINI_API_KEY: ").strip()
    if not api_key:
        print("❌ Cần GEMINI_API_KEY để chạy pipeline.")
        sys.exit(1)

    # State manager
    state = StateManager()
    state.update(phase="writing", total=len(pending), started_at=_now())
    state.log_event("info", f"Pipeline started: {len(pending)} articles to write")

    # Resume callback for dashboard
    resume_event = threading.Event()
    new_key_holder = [api_key]

    def on_resume(new_key):
        new_key_holder[0] = new_key
        state.update(paused=False, pause_reason="")
        state.log_event("info", f"▶ Resumed with new API key")
        resume_event.set()

    # Start dashboard
    if not args.no_dashboard:
        srv, actual_port = start_dashboard(state, on_resume)
        dash_url = f"http://{DASHBOARD_HOST}:{actual_port}" if actual_port else "N/A"
        if srv:
            print(f"🌐 Dashboard: {dash_url}")
            state.log_event("info", f"Dashboard started at {dash_url}")

    print(f"🏭 Starting pipeline: {len(pending)} articles")
    print(f"   Model: {MODEL} | Rate limit: {RATE_LIMIT_SLEEP}s sleep")

    consecutive_errors = 0
    MAX_CONSECUTIVE_ERRORS = 5

    for i, topic in enumerate(pending):
        slug = topic['slug']
        state.update(current_article=slug)
        state.log_event("info", f"[{i+1}/{len(pending)}] Writing: {slug}")
        print(f"  ✍️  [{i+1}/{len(pending)}] {slug}...", end=" ", flush=True)

        try:
            body, in_tok, out_tok = generate_article(topic, new_key_holder[0])
            state.add_tokens(in_tok, out_tok)

            # Audit
            issues = audit_article(body)
            if issues:
                state.log_event("warning", f"{slug}: {', '.join(issues)}")

            # Write file
            fm = build_frontmatter(topic)
            filepath = os.path.join(BLOG_DIR, f"{slug}.md")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(fm + '\n\n' + body + '\n')

            state.state["completed"] += 1
            state._write_state()
            state.log_event("success", f"✅ {slug} ({in_tok}+{out_tok} tokens)")
            print(f"✅ ({in_tok}+{out_tok} tok)")
            consecutive_errors = 0

        except Exception as e:
            err_str = str(e)
            state.add_error(slug, err_str)
            state.log_event("error", f"❌ {slug}: {err_str[:100]}")
            print(f"❌ {err_str[:80]}")
            consecutive_errors += 1

            # Token/quota/auth error → pause for new key
            is_token_error = any(k in err_str.lower() for k in
                ['api key', 'quota', 'rate limit', '429', '403', 'invalid', 'exhausted', 'permission'])

            if is_token_error or consecutive_errors >= MAX_CONSECUTIVE_ERRORS:
                reason = "API key hết quota hoặc không hợp lệ" if is_token_error else f"{consecutive_errors} lỗi liên tiếp"
                state.update(paused=True, pause_reason=f"⚠️ {reason} — Vui lòng nhập token mới trên Dashboard")
                state.log_event("error", f"⏸ Pipeline paused: {reason}")
                print(f"\n⏸ PAUSED: {reason}")
                print(f"   → Mở Dashboard {DASHBOARD_URL} để nhập token mới")
                print(f"   → Hoặc nhấn Enter sau khi set GEMINI_API_KEY mới trong env")

                # Wait for resume via dashboard or stdin
                resume_event.clear()
                if not args.no_dashboard:
                    # Also allow stdin input
                    def stdin_wait():
                        new = input("   🔑 Hoặc paste API key mới tại đây: ").strip()
                        if new:
                            on_resume(new)
                    stdin_thread = threading.Thread(target=stdin_wait, daemon=True)
                    stdin_thread.start()
                    resume_event.wait()  # Block until resume
                else:
                    new = input("   🔑 Nhập API key mới: ").strip()
                    if new:
                        new_key_holder[0] = new
                    else:
                        print("❌ Không có key mới, dừng pipeline.")
                        break

                consecutive_errors = 0
                continue

        # Rate limiting
        if i < len(pending) - 1:
            time.sleep(RATE_LIMIT_SLEEP)

    # Final summary
    s = state.state
    state.update(phase="done", current_article="")
    state.log_event("info", f"🏁 Pipeline complete: {s['completed']}/{s['total']} articles, {s['failed']} failed")

    print(f"\n{'='*50}")
    print(f"🏁 Pipeline hoàn thành!")
    print(f"   ✅ Thành công: {s['completed']}/{s['total']}")
    print(f"   ❌ Thất bại: {s['failed']}")
    print(f"   💰 Token: {s['token_usage']['input']:,} in + {s['token_usage']['output']:,} out")
    print(f"   💵 Chi phí: ${s['token_usage']['cost_usd']:.4f}")
    print(f"\n📌 Bước tiếp:")
    print(f"   1. python3 blog/scripts/generate-crosslinks.py")
    print(f"   2. cd blog && npm run build")
    if not args.no_dashboard:
        print(f"\n🌐 Dashboard vẫn mở tại {DASHBOARD_URL}")
        input("   Nhấn Enter để thoát...")

if __name__ == '__main__':
    main()
