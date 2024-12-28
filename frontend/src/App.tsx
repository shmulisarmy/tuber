import { createEffect, createResource, createSignal, For, type Component } from 'solid-js';

import logo from './logo.svg';
import styles from './App.module.css';
import { AllRecipes } from './RecipeList';
import AvailibleIngredients from './components/availibleIngredients';
import RecipePlanner from './components/recipie_planner';
import Nav from './components/Nav';
import Toaster, { addToast } from './lightning/toast';
import Letter_animator from './lightning/letter_animator';

import kitchen_chaos_1 from "./assets/images/kitchen-chaos-1.webp"
import kitchen_chaos_2 from "./assets/images/kitchen-chaos-2.webp"
import { Image_toggler } from './components/image_toggler';
import { ThemeToggle } from './components/ThemeToggle';


import Blog_card from './lightning/blog-card';
import { recipeData } from './data/all_recipies';



function Debug(){
  return (
    <div>
      {JSON.stringify(recipeData())}
    </div>
  )
}

async function sleep(ms: number){
  return new Promise(resolve => setTimeout(resolve, ms))
}


const App: Component = () => {
  const [users, prefetch] = createResource(async () => {
    await sleep(1000)
    if (window.cache.has('users')){
      return window.cache.get('users')
    }
    const response = await fetch("http://localhost:8000/api/users")
    return response.json()
  })

  createEffect(() => {
    if (users()){
      const first_show = document.getElementById("first-show-users")
      first_show!.remove()
    }
  })
  return (
    <div class={styles.App}>
      <For each={users()}>
        {(user) => (
          <div>
            <h1>{user.name}</h1>
            <p>{user.email}</p>
            <p>{user.phone}</p>
            <p>{user.address}</p>
          </div>
        )}
      </For>
    </div>
  );
};

export default App;
