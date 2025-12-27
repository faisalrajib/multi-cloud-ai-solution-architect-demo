[ Client / App ]
        |
        v
[ API Gateway ]
  (Auth, Rate Limits)
        |
        v
[ AI API Service ]
  - Prompt orchestration
  - RAG logic
        |
   ----------------
   |              |
   v              v
[ Vector DB ]   [ LLM Provider ]
   |              |
   v              v
[ Object Storage ] 
