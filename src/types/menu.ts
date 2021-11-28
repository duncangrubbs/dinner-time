import Meal from '../model/meal';

export default interface Menu {
  meals: Meal[];
  shoppingList: string[];
}
