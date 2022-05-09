from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


from . import models, schemas, crud
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/meals/{meal_id}", response_model=schemas.Meal) 
def read_meal(meal_id: int, db: Session = Depends(get_db)):
    db_meal = crud.get_meal(db, meal_id=meal_id)
    if db_meal is None:
        raise HTTPException(status_code=404, detail="Meal not found")
    return db_meal


@app.get("/meals", response_model=List[schemas.Meal]) 
def read_meals(db: Session = Depends(get_db)):
    db_meals = crud.get_meals(db)
    if db_meals is None:
        raise HTTPException(status_code=404, detail="No meals found")
    return db_meals


@app.post("/meals", response_model=schemas.Meal)
def create_meal(meal: schemas.MealCreate, db: Session = Depends(get_db)):
    return crud.create_meal(db=db, meal=meal)


@app.get("/menu", response_model=schemas.Menu)
def read_menu(days: int, db: Session = Depends(get_db)):
    db_meals = crud.get_meals(db, limit=days)
    if len(db_meals) < days:
        raise HTTPException(status_code=400, detail="Not enough meals")
    ingredients = list(set([x for meal in db_meals for x in meal.ingredients]))
    menu = schemas.Menu(meals=db_meals, ingredients=ingredients)
    return menu
