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
			<div class="row border-bottom" id="scoreboard">
				<div class="col px-3 text-left">
					<GameScore />
				</div>
				<div class="col px-3 text-right">
					<GameTimer />
				</div>
			</div>
			<div class="row text-secondary my-2" id="equation">
				<GameEquation />
			</div>
			<div class="row" id="buttons">
				<div class="col">
					<button
						class="btn btn-primary number-button"
						v-for="button in buttons"
						:key="button"
					>
						{{ button }}
					</button>
					<button class="btn btn-primary" id="clear-button">
						Clear
					</button>
				</div>
			</div>
		</div>
	</main>
</template>

<script>
import SelectInput from '../components/SelectInput.vue';
import PlayButton from '../components/PlayButton.vue';
import GameScore from '../components/GameScore.vue';
import GameTimer from '../components/GameTimer.vue';
import GameEquation from '../components/GameEquation.vue';

export default {
	name: 'MathGame',
	components: {
		SelectInput,
		PlayButton,
		GameScore,
		GameTimer,
		GameEquation,
	},
	data() {
		return {
			buttons: [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
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

button.number-button {
	border-radius: 0.25em;
	font-size: 3em;
	height: 2em;
	margin: 0.1em;
	text-align: center;
	width: 2em;
}

#clear-button {
	border-radius: 0.25em;
	font-size: 3em;
	height: 2em;
	margin: 0.1em;
	text-align: center;
	width: 4.2em;
}

#scoreboard {
	font-size: 1.5em;
}
</style>
