export default class Meal {
  id: string;

  name: string;

  category: string;

  mainIngredient: string;

  isVegetarian: boolean;

  ingredients: string[];

  url: string;

  lastSuggested: Date;

  constructor(
    id: string,
    name: string,
    category: string,
    mainIngredient: string,
    isVegetarian: boolean,
    ingredients: string[],
    url: string,
    lastSuggested: Date,
  ) {
    this.id = id;
    this.name = name;
    this.category = category;
    this.mainIngredient = mainIngredient;
    this.isVegetarian = isVegetarian;
    this.ingredients = ingredients;
    this.url = url;
    this.lastSuggested = lastSuggested;
  }
}