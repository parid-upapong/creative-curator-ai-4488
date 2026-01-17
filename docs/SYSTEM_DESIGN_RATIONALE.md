# System Design Rationale

## Why Microservices?
The "High-Volume Media" requirement dictates that media processing (which is CPU/GPU intensive) must be isolated from the API Gateway to prevent UI lag. Kubernetes allows us to scale the `media-processor` and `ai-engine` independently based on the queue length.

## Managing Global Standards
By utilizing **gRPC and Protobuf**, we enforce a strict contract between services. This ensures that the "Unified Creative Schema (JSON-C)" defined in the roadmap remains consistent across the entire ecosystem.

## AI Optimization
To achieve the "99% AI parsing accuracy" goal, the AI Engine uses a warm-pool of GPU workers. We use Redis for caching frequent AI-generated pitches to reduce latency and API costs for repetitive client queries.