<template>
	<main id="main-container">
		<div v-if="screen === 'config'" id="config-container">
			<h1>Math Facts</h1>
			<SelectInput
				:currentValue="operation"
				label="Operation"
				id="operation"
				v-model="operation"
				:options="operations"
				@input="changeOperation"
			/>
			<SelectInput
				:currentValue="maxNumber"
				label="Maximum Number"
				id="max-number"
				v-model="maxNumber"
				:options="numbers"
				@input="changeMaxNumber"
			/>
			<PlayButton @play-button-click="play" />
		</div>
		<div
			v-else-if="screen === 'play'"
			id="game-container"
			class="text-center"
		>
			<button class="btn btn-success" @click="config">Change Game</button>
		</div>
	</main>
</template>

<script>
import SelectInput from '../components/SelectInput.vue';
import PlayButton from '../components/PlayButton.vue';

export default {
	name: 'MathGame',
	components: {
		SelectInput,
		PlayButton,
	},
	data() {
		return {
			operations: [
				['Addition', '+'],
				['Subtraction', '-'],
				['Multiplication', 'x'],
				['Division', '/'],
			],
			userName: '',
			score: 0,
			operation: 'x',
			maxNumber: '10',
			screen: 'config',
		};
	},
	methods: {
		config() {
			this.screen = 'config';
		},
		play() {
			this.screen = 'play';
		},
		async recordScore() {
			const data = {
				'user-name': this.userName,
				score: this.score,
				game: 'MATH',
			};
			const response = (await this.axios.post('/record-score/', data))
				.data;
			console.log(response);
		},
		changeOperation(eventName) {
			console.log(eventName.target.value);
			this.operation = eventName.target.value;
		},
		changeMaxNumber(eventName) {
			console.log(eventName.target.value);
			this.maxNumber = eventName.target.value;
		},
	},
	computed: {
		numbers: function () {
			const numbers = [];
			for (let number = 2; number <= 100; number++) {
				numbers.push([number, number]);
			}
			return numbers;
		},
	},
};
</script>

<style scoped>
#main-container {
	margin: auto;
	width: 380px;
}
</style>
