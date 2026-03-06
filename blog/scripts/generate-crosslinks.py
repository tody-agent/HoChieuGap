#!/usr/bin/env python3
"""Generate cross-links between articles based on cluster membership."""
import os, re, json, random

DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'content', 'blog')

def parse_frontmatter(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not m: return None, content
    fm_text = m.group(1)
    slug = os.path.basename(path).replace('.md','')
    cluster = ''
    is_pillar = False
    for line in fm_text.split('\n'):
        if line.startswith('cluster:'): cluster = line.split("'")[1] if "'" in line else ''
        if line.startswith('isPillar: true'): is_pillar = True
    return {'slug': slug, 'cluster': cluster, 'isPillar': is_pillar, 'path': path}, content

def set_related_slugs(path, content, slugs):
    new_val = json.dumps(slugs, ensure_ascii=False)
    content = re.sub(r'relatedSlugs:.*', f'relatedSlugs: {new_val}', content)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Parse all articles
articles = []
for f in sorted(os.listdir(DIR)):
    if not f.endswith('.md'): continue
    info, content = parse_frontmatter(os.path.join(DIR, f))
    if info: articles.append((info, content))

# Group by cluster
clusters = {}
for info, _ in articles:
    c = info['cluster']
    if c not in clusters: clusters[c] = []
    clusters[c].append(info)

# Generate cross-links
updated = 0
for info, content in articles:
    c = info['cluster']
    slug = info['slug']
    siblings = [a for a in clusters.get(c, []) if a['slug'] != slug]

    # Prioritize pillar article
    related = []
    pillar = [a for a in siblings if a['isPillar']]
    non_pillar = [a for a in siblings if not a['isPillar']]

    if pillar:
        related.extend([p['slug'] for p in pillar])

    # Add 3-4 random siblings
    random.seed(slug)  # deterministic
    random.shuffle(non_pillar)
    related.extend([a['slug'] for a in non_pillar[:4]])

    # Add 1 cross-cluster article (from a related cluster)
    cross_map = {
        'gap-khan-cap': 'mat-hc', 'mat-hc': 'gap-khan-cap',
        'cap-moi': 'gia-han', 'gia-han': 'cap-moi',
        'tre-em': 'cap-moi', 'du-lich': 'gap-khan-cap',
        'chi-phi': 'gap-khan-cap', 'phap-ly': 'cap-moi',
        'nghe-nghiep': 'du-lich', 'meo': 'cap-moi',
        'dia-phuong': 'gap-khan-cap', 'visa': 'du-lich',
        'gia-dinh': 'tre-em', 'doanh-nghiep': 'chi-phi',
        'cong-nghe': 'phap-ly', 'an-ninh': 'meo',
        'seasonal': 'du-lich', 'faq': 'cap-moi',
    }
    cross_cluster = cross_map.get(c, 'gap-khan-cap')
    cross_opts = [a for a in clusters.get(cross_cluster, []) if a['isPillar']]
    if cross_opts:
        related.append(cross_opts[0]['slug'])

    # Deduplicate, limit to 5
    seen = set()
    final = []
    for s in related:
        if s not in seen:
            seen.add(s)
            final.append(s)
    final = final[:5]

    set_related_slugs(info['path'], content, final)
    updated += 1

print(f"✅ Updated cross-links for {updated} articles")
print(f"   Clusters: {len(clusters)}")
for c, arts in sorted(clusters.items()):
    print(f"   {c}: {len(arts)} articles")
