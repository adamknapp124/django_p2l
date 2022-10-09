<template>
	<main id="main-container">
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
		<PlayButton />
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
		};
	},
	methods: {
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
