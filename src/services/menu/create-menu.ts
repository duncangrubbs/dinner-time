import MealDao from '../../model/meal.dao';
import Menu from '../../types/menu';
import database from '../db';

class CreateMenu {
  days: number;

  constructor(days: number) {
    this.days = days;
  }

  async buildMenu(): Promise<Menu> {
    const dao = new MealDao(database.pool);
    const meals = (await dao.getAllMeals()).splice(0, this.days);
    const shoppingList = meals.map(meal => meal.ingredients).flat();

    return {
      meals,
      // TODO: we might want to use fuzzy-match to remove duplicates
      shoppingList: Array.from(new Set(shoppingList)),
    };
  }
}

export default CreateMenu;
