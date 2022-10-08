import { createWebHistory, createRouter } from 'vue-router';

import AnagramGame from './apps/AnagramGame.vue';
import MathGame from './apps/MathGame.vue';
import HomeView from './apps/HomeView';


const routes = [
    {
        path: '/anagram-game',
        component: AnagramGame
    },
    {
        path: '/math-game',
        component: MathGame
    },
    {
        path: '',
        component: HomeView
    },
    {
        path: '/home',
        component: HomeView
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});


export default router;