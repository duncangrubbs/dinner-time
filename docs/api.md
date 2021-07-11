# 🔧 API Documentation

This is a simple REST api implementation. All body data should be sent like so.
```typescript
{
    body: {
        data: {}
    }
}
```

## Endpoints

### `POST /api/meals`
Body Data
```typescript
interface Meal {
    name: string;
    category?: string;
    url?: string;
    ingredients?: string[];
    season?: string;
}
```

---
### `GET /api/meals`
#### Parameters
- ?season=string
- ?category=string
- ?ingredients=string,string...

---
### `GET /api/meals/recommended`

---
### `GET /api/meals/random`

---
### `GET /api/menu`