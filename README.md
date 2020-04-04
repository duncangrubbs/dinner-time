# 🍽 dinner-time
> A resource for helping find meals to cook for dinner

--- 
## 🙌Current Features:
- Add to database
- Query by SEASON or CATEGORY in DB
- Get random meal
- Get recommended meal (not a great algorithm as of now)

## 📓Future Features/TODO:
- [ ] REST API Support
- [ ] Better Suggested meals (use AI)
- [ ] Generate Shopping List
- [ ] Support real DB system
- [ ] Update time last suggested

---

##  🔨Stack
1. Python 3.8.0
2. Flask
3. JSON

## 🖋Specifications

### Meal Object Specification
- tags: Array: String
- time: String
- id: Integer
- last_suggested: Integer
- name: String
- category: String
- season: String
- location: String

### Region Specification
- __AMERICAN__
- __ASIAN__
- __ITALIAN__
- __MEXICAN__
- __INDIAN__

### Main Ingredient Specification
- __CHICKEN__
- __BEEF__
- __PORK__
- __TURKEY__
- __BEANS__
- __TOMATOES__
- __FISH__
- __PASTA__

### Specialty Specification
- __SOUP__
- __SALAD__

### Season Specification
- __WINTER__
- __SPRING__
- __SUMMER__
- __FALL__

### Time Specification
- __EASY__
- __MODERATE__
- __ELABORATE__

### Tags Specification
- __hearty__
- __fancy__
- __healthy__
- __staple__
- __vegetarian__

## API Reference
- `POST /api/meals/add`
- `GET /api/meals/all`
- `GET /api/meals?season=SEASON`
- `GET /api/meals?category=CATEGORY`
- `GET /api/meals/recommended`
- `GET /api/meals/random`
