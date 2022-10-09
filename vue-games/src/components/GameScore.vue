<template>
	<div>Score: {{ score }}</div>
</template>

<script>
export default {
	name: 'GameScore',
	props: {
		score: Number,
	},
};
</script>
