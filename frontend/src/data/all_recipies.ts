import { createEffect, createResource } from "solid-js";
import { Dish } from "../types/dish";


const app_url = "http://127.0.0.1:8000"

export const [recipeData, { refetch }]: any = createResource(async () => (await (await (fetch(`${app_url}/api/recipies/all`))).json()))



createEffect(() => {
    console.log("recipeData", recipeData())
})



