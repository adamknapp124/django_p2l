<template>
	<div>Score: {{ score }}</div>
</template>

<script>
export default {
	name: 'GameScore',
	props: {
		Score: Number,
	},
};
</script>
