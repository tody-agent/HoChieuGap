import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
	loader: glob({ base: './src/content/blog', pattern: '**/*.{md,mdx}' }),
	schema: ({ image }) =>
		z.object({
			title: z.string(),
			description: z.string().max(160),
			pubDate: z.coerce.date(),
			updatedDate: z.coerce.date().optional(),
			heroImage: image().optional(),
			// SEO fields
			cluster: z.string(), // e.g. 'gap-khan-cap', 'cap-moi'
			keywords: z.array(z.string()).default([]),
			// Content structure
			readingTime: z.number().optional(), // minutes
			isPillar: z.boolean().default(false),
			relatedSlugs: z.array(z.string()).default([]),
		}),
});

export const collections = { blog };
