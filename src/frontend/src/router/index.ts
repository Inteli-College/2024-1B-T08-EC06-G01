import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Home from '../views/Home.vue';
import About from '../views/About.vue';
import Control from '../views/Control.vue';
import Createacout from '../views/Createacount.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'CreateAcount',
    component: Createacout
  },
  {
    path: '/about',
    name: 'About',
    component: About
  },
  {
    path: '/control',
    name: 'Control',
    component: Control
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
