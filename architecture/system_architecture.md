flowchart LR
    User[Client / Application] --> APIGW[API Gateway]

    APIGW -->|Authenticated Requests| API[AI API Service]

    API --> RAG[RAG Orchestration Layer]

    RAG --> VS[Vector Database]
    VS --> OBJ[Object Storage]

    RAG --> LLM[LLM Provider]

    subgraph Security
        APIGW
    end

    subgraph AI_Processing
        API
        RAG
    end

    subgraph Data_Layer
        VS
        OBJ
    end

    subgraph External_Services
        LLM
    end

## Architecture Overview

1. Clients interact with the system through a REST API.
2. The API Gateway enforces authentication, rate limiting, and request validation.
3. The AI API Service handles request orchestration and business logic.
4. The RAG layer retrieves relevant documents from the vector database.
5. Retrieved context is combined with the user query and sent to the LLM provider.
6. Object storage is used for raw document persistence and re-indexing workflows.

This architecture is cloud-agnostic and can be deployed across AWS, Azure, or GCP
using managed services.

