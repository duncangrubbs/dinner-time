import express, { Router } from 'express';
import MealController from '../controllers/meal.controller';
import MenuController from '../controllers/menu.controller';
import RestController from '../types/base.controller';

function mapRequestsToController(controller: RestController, router: Router) {
  router.route(controller.endpoint)
    .get(controller.get)
    .delete(controller.delete)
    .put(controller.put)
    .post(controller.post);
}

const router = express.Router();

const mealController = new MealController('/meals', 'Meal Controller');
const menuController = new MenuController('/menu', 'Menu Controller');
mapRequestsToController(mealController, router);
mapRequestsToController(menuController, router);

export default router;
