import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import Home from '../views/Home.vue';
import About from '../views/About.vue';
import Control from '../views/Control.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home
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
    }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
