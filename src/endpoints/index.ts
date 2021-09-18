import express, { Router } from 'express';
import MealController from '../controllers/MealController';
import RestController from '../types/RestController';

function mapRequestsToController(controller: RestController, router: Router) {
  router.route(controller.endpoint)
    .get(controller.get)
    .delete(controller.delete)
    .put(controller.put)
    .post(controller.post);
}

const router = express.Router();

const mealController = new MealController('/meals', 'Meal Controller');

mapRequestsToController(mealController, router);

export default router;
