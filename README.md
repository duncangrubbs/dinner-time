# 🍽 dinner-time
> A resource for helping find meals to cook for dinner

--- 
## Current Features:
- Add to database
- Query by label in DB
- Get random meal

## Future Features:
- Suggested meals
- Generate Shopping List

---

## Stack
1. Python 3
2. Flask
3. JSON

## Meal Object Spec
- ingredients: Array: String
- tags: Array: String
- time: Integer
- id: Integer
- last_suggested: Integer
- name: String
- category: String
- season: String
- location: String

## Category Spec
- __SALAD__
- __PAN/BULK__
- __MEXICAN__
- __ITALIAN__
- __SOUP__
- __ASIAN__
- __AMERICAN__

## Season Spec:
- __WINTER, SPRING, SUMMER, FALL__

## Sample Tags:
- __hearty, quick, easy, fancy, healthy, staple__

## API Reference
- `POST /api/meals/add`
- `GET /api/meals/all`
- `GET /api/meals/:query`
- `GET /api/meals/recommended`
- `GET /api/meals/random`