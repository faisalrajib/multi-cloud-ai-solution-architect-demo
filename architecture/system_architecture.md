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
