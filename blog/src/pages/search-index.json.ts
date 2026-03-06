import { getCollection } from 'astro:content';

// Cluster icon map
const CLUSTER_ICONS: Record<string, string> = {
	'gap-khan-cap': '🔥', 'cap-moi': '🆕', 'tre-em': '👶',
	'gia-han': '🔄', 'mat-hc': '🔍', 'du-lich': '✈️',
	'chi-phi': '💰', 'phap-ly': '📋', 'nghe-nghiep': '🎓', 'meo': '💡',
};

export async function GET() {
	const posts = await getCollection('blog');
	const index = posts.map((post) => ({
		slug: post.id,
		title: post.data.title,
		description: post.data.description,
		cluster: post.data.cluster || '',
		clusterIcon: CLUSTER_ICONS[post.data.cluster as string] || '',
		keywords: post.data.keywords || [],
	}));

	return new Response(JSON.stringify(index), {
		headers: { 'Content-Type': 'application/json' },
	});
}
