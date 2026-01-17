# System Architecture: Global Creative Platform Standards

## 1. Architectural Principles
- **Event-Driven Media Processing:** High-resolution assets are processed asynchronously via message queues (RabbitMQ/Kafka).
- **AI-Orchestration Layer:** Decouples heavy AI model inference from the API Gateway.
- **Global Content Delivery:** Multi-region Object Storage with edge-compute resizing.
- **Polyglot Persistence:** PostgreSQL for relational data, MongoDB for flexible Creative Schema (JSON-C), and Pinecone/Milvus for Vector Search.

## 2. Microservice Decomposition
- **Gateway Service:** Authentication, rate limiting, and request routing (Kong/Go).
- **Profile & Portfolio Service:** Manages the Unified Creative Schema (Node.js/TypeScript).
- **Media Engine:** Handles transcoding, thumbnail generation, and watermarking (Go + FFmpeg).
- **AI Pitch Service:** Generates dynamic presentations using LLMs and Vision models (Python/FastAPI).
- **Matching Service:** Vector-based talent-to-job matching (Python).

## 3. High-Level Diagram
[Client] -> [Cloudflare/CDN] -> [API Gateway]
                                    |
            -------------------------------------------------
            |               |               |               |
    [Profile Svc]   [Media Svc]     [AI Pitch Svc]   [Matching Svc]
            |               |               |               |
      [PostgreSQL]    [S3 + Redis]    [GPU Worker]    [Vector DB]