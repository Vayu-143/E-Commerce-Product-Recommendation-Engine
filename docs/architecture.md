# Architecture

## Flow

User Activity
↓
Data Storage (HashMap)
↓
Similarity Service
↓
Recommendation Service
↓
Heap Ranking
↓
Top Recommendations
↓
Report Generation

## Layers

Models
- Product
- User

Storage
- JSON Data Loader

Services
- Similarity Service
- Recommendation Service
- Analytics Service
- Report Service

Utilities
- Logger
- Constants