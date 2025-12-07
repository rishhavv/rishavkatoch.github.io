import { defineCollection, z } from 'astro:content';

const blogCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    date: z.coerce.date(),
    tags: z.array(z.string()).optional(),
    draft: z.boolean().optional().default(false),
    series: z.string().optional(),
    seriesOrder: z.number().optional(),
  }),
});

const readingCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    author: z.string(),
    description: z.string(),
    startDate: z.coerce.date(),
    status: z.enum(['reading', 'completed', 'paused']),
    rating: z.number().min(1).max(5).optional(),
    coverImage: z.string().optional(),
    tags: z.array(z.string()).optional(),
  }),
});

export const collections = {
  blog: blogCollection,
  reading: readingCollection,
};

