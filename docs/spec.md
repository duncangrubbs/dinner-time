# 🖋 Specification

### Meal Object Specification
```sql
id SERIAL PRIMARY KEY,
name VARCHAR (60) NOT NULL,
season VARCHAR (30),
category VARCHAR (30),
main_ingredient VARCHAR (30),
is_vegetarian BOOLEAN NOT NULL,
ingredients TEXT [],
url VARCHAR (30),
last_suggested BIGINT NOT NULL
```

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