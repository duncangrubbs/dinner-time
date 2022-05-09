from unicodedata import category
from sqlalchemy.orm import Session

from . import models, schemas


def get_meal(db: Session, meal_id: int):
    return db.query(models.Meal).filter(models.Meal.id == meal_id).first()


def get_meals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Meal).offset(skip).limit(limit).all()


def create_meal(db: Session, meal: schemas.MealCreate):
    db_meal = models.Meal(
        name = meal.name,
        season = meal.season,
        category = meal.category,
        ingredients = meal.ingredients,
        url = meal.url,
        last_suggested = meal.last_suggested
    )
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal
