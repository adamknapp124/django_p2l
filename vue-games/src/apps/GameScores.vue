<template>
	<div id="main-container">
		<h1>Game Scores</h1>
		<h2>Math Game</h2>
		<ol>
			<li v-for="score in math_scores" :key="score">
				{{ score.score }}: ({{ score.user_name }} - {{ score.created }})
			</li>
		</ol>
		<h2>Anagram Game</h2>
		<ol>
			<li v-for="score in anagram_scores" :key="score">
				{{ score.score }}: ({{ score.user_name }} - {{ score.created }})
			</li>
		</ol>
	</div>
</template>

<script>
	export default {
		name: 'GameScores',
		props: {
			score: Number,
		},
	};
</script>
