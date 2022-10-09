<template>
	<button class="btn btn-primary" @click="$emit('play-button-click')">
		Play!
	</button>
</template>

<script>
export default {
	name: 'PlayButton',
};
</script>
