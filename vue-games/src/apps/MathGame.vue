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
				@input="changeOperation" />
			<SelectInput
				:currentValue="maxNumber"
				label="Maximum Number"
				id="max-number"
				v-model="maxNumber"
				:options="numbers"
				@input="changeMaxNumber" />
			<PlayButton @play-button-click="play" />
		</div>
		<div v-else-if="screen === 'play'" id="game-container" class="text-center">
			<transition name="slide">
				<template v-if="timeLeft === 0">
					<div>
						<h2>Time's Up!</h2>
						<strong class="big">You answered</strong>
						<div class="huge">{{ score }}</div>
						<strong class="big">Questions Correctly</strong>
						<button
							class="btn btn-primary form-control m-1"
							@click="
								config();
								recordScore();
							">
							Play Again with Same Settings
						</button>
						<button
							class="btn btn-secondary form-control m-1"
							@click="
								config();
								recordScore();
							">
							Change Settings
						</button>
					</div>
				</template>
			</transition>
			<transition name="slide-right">
				<template v-if="timeLeft > 0">
					<div>
						<div class="row border-bottom" id="scoreboard">
							<div class="col px-3 text-left">
								<GameScore :score="score" />
							</div>
							<div class="col px-3 text-right">
								<GameTimer :timeLeft="timeLeft" />
							</div>
						</div>
						<div class="equationClass" id="equation">
							<GameEquation
								:question="question"
								:answer="input"
								:answered="answered" />
						</div>
						<div class="row" id="buttons">
							<div class="col">
								<button
									class="btn btn-primary number-button"
									v-for="button in buttons"
									:key="button"
									@click="setInput(button)">
									{{ button }}
								</button>
								<button
									class="btn btn-primary"
									id="clear-button"
									@click="clear">
									Clear
								</button>
							</div>
						</div>
					</div>
				</template>
			</transition>
		</div>
	</main>
</template>

<script>
	import SelectInput from '../components/SelectInput.vue';
	import PlayButton from '../components/PlayButton.vue';
	import GameScore from '../components/GameScore.vue';
	import GameTimer from '../components/GameTimer.vue';
	import GameEquation from '../components/GameEquation.vue';
	import { randInt } from '../helpers/helpers';

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
				input: '',
				operands: { num1: '1', num2: '1' },
				answered: false,
				gameLength: 10,
				timeLeft: 0,
			};
		},
		methods: {
			config() {
				this.screen = 'config';
			},
			play() {
				this.screen = 'play';
				this.newQuestion();
				this.startTimer();
			},
			async recordScore() {
				console.log(this.score);
				const data = {
					'user-name': this.userName,
					score: this.score,
					game: 'MATH',
				};
				const response = (await this.axios.post('record-score/', data)).data;
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
			setInput(value) {
				this.input += String(value);
				this.input = String(Number(this.input));
				this.answered = this.checkAnswer(
					this.input,
					this.operation,
					this.operands
				);
				if (this.answered) {
					setTimeout(this.newQuestion, 300);
					this.score++;
				}
			},
			clear() {
				this.input = '';
			},
			getRandNumbers(operator, low, high) {
				let num1 = randInt(low, high);
				let num2 = randInt(low, high);
				const numHigh = Math.max(num1, num2);
				const numLow = Math.min(num1, num2);

				if (operator === '-') {
					num1 = numHigh;
					num2 = numLow;
				}

				if (operator === '/') {
					if (num2 === 0) {
						num2 - randInt(1, high);
					}
					num1 = num1 * num2;
				}
				return { num1, num2 };
			},
			newQuestion() {
				this.input = '';
				this.answered = false;
				this.operands = this.getRandNumbers(this.operation, 0, this.maxNumber);
			},
			checkAnswer(userAnswer, operation, operands) {
				if (isNaN(userAnswer)) return false;

				let correctAnswer;
				switch (operation) {
					case '+':
						correctAnswer = operands.num1 + operands.num2;
						break;
					case '-':
						correctAnswer = operands.num1 - operands.num2;
						break;
					case 'x':
						correctAnswer = operands.num1 * operands.num2;
						break;
					default: //division
						correctAnswer = operands.num1 / operands.num2;
				}
				return parseInt(userAnswer) === correctAnswer;
			},
			startTimer() {
				window.addEventListener('keyup', this.handleKeyUp);
				this.timeLeft = this.gameLength;
				if (this.timeLeft > 0) {
					this.timer = setInterval(() => {
						this.timeLeft--;
						if (this.timeLeft === 0) {
							clearInterval(this.timer);
							window.removeEventListener('keyup', this.handleKeyUp);
						}
					}, 1000);
				}
			},
			restart() {
				this.score = 0;
				this.startTimer();
				this.newQuestion();
			},
			handleKeyUp(e) {
				e.preventDefault();
				if (e.keyCode === 32 || e.keyCode === 13) {
					this.clear();
				} else if (e.keyCode === 8) {
					this.input = this.input.substring(0, this.input.length - 1);
				} else if (!isNaN(e.key)) {
					this.setInput(e.key);
				}
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
			question: function () {
				const num1 = this.operands.num1;
				const num2 = this.operands.num2;
				const equation = `${num1} ${this.operation} ${num2}`;
				return equation;
			},
			equationClass: function () {
				if (this.answered) {
					return 'row text-primary my-2 fade';
				} else {
					return 'row text-secondary my-2';
				}
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

	.big {
		font-size: 1.5em;
	}

	.huge {
		font-size: 5em;
	}

	.slide-leave-active,
	.slide-enter-active {
		position: absolute;
		top: 56px;
		transition: 1s;
		width: 380px;
	}

	.slide-enter {
		transform: translate(-100%, 0);
		transition: opacity 0.5s;
	}

	.slide-leave-to {
		opacity: 0;
		transform: translate(100%, 0);
	}

	.slide-right-leave-active,
	.slide-right-enter-active {
		position: absolute;
		top: 56px;
		transition: 1s;
		width: 380px;
	}

	.slide-right-enter {
		transform: translate(100%, 0);
		transition: opacity 0.5s;
	}

	.slide-right-leave-to {
		opacity: 0;
		transform: translate(-100%, 0);
	}
</style>
