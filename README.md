# Dinner Time 🥖
> A resource for helping find meals to cook for dinner _(or really any meal)_

## 🙌 Current Features:
- Add to database
- Query by all specs
- Get a random meal
- Get recommended meal (not a great algorithm as of now)
- REST API for most routes

## 📓 Future Features/TODO:
- [ ] Better Suggested meals _(using AI?)_
- [ ] Generate Shopping List
- [ ] Support real database system
- [ ] Update time last suggested

##  🔨 Stack
1. Python 3.8.0
2. Flask
3. JSON

## 🖋 Specifications

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
- AMERICAN
- THAI
- CHINESE
- ASIAN
- JAPANESE
- KOREAN
- FRENCH
- GERMAN
- MIDDLE EASTERN
- ITALIAN
- MEXICAN
- INDIAN

### Main Ingredient Specification
- CHICKEN
- BEEF
- PORK
- TURKEY
- BEANS
- TOMATOES
- FISH
- PASTA
- TOFU

### Specialty Specification
- SOUP
- SALAD

### Season Specification
- WINTER
- SPRING
- SUMMER
- FALL

### Time Specification
- EASY
- MODERATE
- ELABORATE

### Tags Specification
- hearty
- fancy
- healthy
- staple
- vegetarian

## API Reference
- `POST /api/meals/add`
- `GET /api/meals/all`
- `GET /api/meals?season=SEASON`
- `GET /api/meals?category=CATEGORY`
- `GET /api/meals/recommended`
- `GET /api/meals/random`
