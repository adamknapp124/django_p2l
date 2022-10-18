import { createWebHistory, createRouter } from 'vue-router';

import AnagramGame from './apps/AnagramGame.vue';
import GameScores from './apps/GameScores.vue';
import MathGame from './apps/MathGame.vue';
import ReviewForm from './apps/ReviewForm.vue';

const routes = [
	{
		path: '/anagram-game',
		component: AnagramGame,
	},
	{
		path: '/math-game',
		component: MathGame,
	},
	{
		path: '/game-scores',
		component: GameScores,
	},
	{
		path: '/review',
		component: ReviewForm,
	},
];

const router = createRouter({
	history: createWebHistory(),
	routes: routes,
});

export default router;
