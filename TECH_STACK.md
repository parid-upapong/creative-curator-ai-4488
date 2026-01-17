# Recommended Tech Stack: Creative Unlock AI

## Frontend
- **Framework:** Next.js 14 (App Router) for SEO and performance.
- **Styling:** Tailwind CSS + Framer Motion (for high-end creative feel).
- **State Management:** TanStack Query (React Query) for data fetching.

## Backend & AI
- **Primary Language:** Python (FastAPI) for AI services.
- **Orchestration:** Node.js (TypeScript) for main API and user logic.
- **AI Models:** 
    - **Vision:** GPT-4o or Claude 3.5 Sonnet (for portfolio analysis).
    - **Text:** GPT-4-Turbo (for dynamic pitch generation).
    - **Vector DB:** Pinecone or Milvus (for style similarity search).

## Infrastructure
- **Database:** PostgreSQL (Supabase) for relational data.
- **Storage:** AWS S3 (with CloudFront) for high-res portfolio assets.
- **Compute:** Vercel (Frontend) + Render/AWS (Backend).