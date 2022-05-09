from typing import List
from pydantic import BaseModel


class MealBase(BaseModel):
    name: str
    season: str
    category: str
    ingredients: List[str]
    url: str
    last_suggested: int


class Meal(MealBase):
    id: int

    class Config:
        orm_mode = True


class MealCreate(MealBase):
    pass


class Menu(BaseModel):
    meals: List[Meal]
    ingredients: List[str]
