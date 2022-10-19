<template>
	<main id="main-container">
		<div v-if="screen === 'config'" id="config-container">
			<h1>Anagram Hunt</h1>
			<div>Rearrange the letters to make new words</div>
			<hr />
			<div class="row mx-1 my-3">
				<label class="col" for="wordLength" id="wordLength">Word length:</label>
				<input
					@keyup.enter="play"
					ref="toggleFocus"
					class="col form-control"
					v-model="anagramLength"
					type="text"
					name="wordLength"
					placeholder="between 5 and 8"
					autocomplete="off"
					autofocus
					style="text-align: center" />
			</div>
			<hr />
			<template v-if="anagramLength > 4 && anagramLength < 9">
				<PlayButton @play-button-click="play" />
			</template>
			<template v-else>
				<button
					:disabled="''"
					class="btn btn-secondary form-control m-1 disabled">
					Play
				</button>
			</template>
		</div>
		<div v-else-if="screen === 'play'" id="game-container" class="text-center">
			<template v-if="this.randomChoice.length === 0">
				<div>
					<h2>Congratulations!</h2>
					<strong class="big">You Answered</strong>
					<div class="huge">{{ score }}</div>
					<strong class="big">Questions Correctly</strong>
					<button
						class="btn btn-primary form-control m-1"
						v-on:click="restart()">
						Play Again with Same Settings
					</button>
					<button
						class="btn btn-secondary form-control m-1"
						v-on:click="config()">
						Change Settings
					</button>
				</div>
			</template>
			<template v-else-if="timeLeft > 0">
				<h1>Anagram Hunt</h1>
				<hr />
				<div class="row border-bottom" id="scoreboard">
					<div class="col px-3 text-left">
						<GameScore :score="this.score" />
					</div>
					<div class="col px-3 text-right">
						<GameTimer :timeLeft="timeLeft" />
					</div>
				</div>
				<WordEquation
					v-on:test-click="incrementCounter"
					:index="this.randomIndex"
					:question="this.anagramWord"
					:wordsRemaining="possibilities"
					:newBaseArray="this.newBaseArray" />
			</template>
			<template v-else-if="timeLeft === 0">
				<div>
					<h2>Time's Up!</h2>
					<strong class="big">You Answered</strong>
					<div class="huge">{{ score }}</div>
					<strong class="big">Questions Correctly</strong>
					<button
						class="btn btn-primary form-control m-1"
						@click="recordScore(); restart();">
						Play Again with Same Settings
					</button>
					<button
						class="btn btn-secondary form-control m-1"
						@click="recordScore(); config();">
						Change Settings
					</button>
				</div>
			</template>
		</div>
	</main>
</template>

<script>
	const anagramData = {
		5: [
			['abets', 'baste', 'betas', 'beast', 'beats'],
			['acres', 'cares', 'races', 'scare'],
			['alert', 'alter', 'later'],
			['angel', 'angle', 'glean'],
			['baker', 'brake', 'break'],
			['bared', 'beard', 'bread', 'debar'],
			['dater', 'rated', 'trade', 'tread'],
			['below', 'bowel', 'elbow'],
			['caret', 'cater', 'crate', 'trace', 'react'],
		],
		6: [
			['arrest', 'rarest', 'raster', 'raters', 'starer'],
			['carets', 'caters', 'caster', 'crates', 'reacts', 'recast', 'traces'],
			['canter', 'nectar', 'recant', 'trance'],
			['danger', 'gander', 'garden', 'ranged'],
			['daters', 'trades', 'treads', 'stared'],
		],
		7: [
			['allergy', 'gallery', 'largely', 'regally'],
			['aspired', 'despair', 'diapers', 'praised'],
			['claimed', 'decimal', 'declaim', 'medical'],
			['dearths', 'hardest', 'hatreds', 'threads', 'trashed'],
			['detains', 'instead', 'sainted', 'stained'],
		],
		8: [
			['parroted', 'predator', 'prorated', 'teardrop'],
			['repaints', 'painters', 'pantries', 'pertains'],
			['restrain', 'retrains', 'strainer', 'terrains', 'trainers'],
			['construe', 'counters', 'recounts', 'trounces'],
		],
	};
	import PlayButton from '../components/PlayButton.vue';
	import GameTimer from '../components/GameTimer.vue';
	import GameScore from '../components/GameScore.vue';
	import WordEquation from '../components/WordEquation.vue';
	export default {
		name: 'AnagramGame',
		components: {
			PlayButton,
			GameTimer,
			GameScore,
			WordEquation,
		},
		data: function () {
			return {
				score: 0,
				userName: '',
				screen: 'config',
				gameLength: 3,
				timeLeft: 0,
				answered: false,
				length: 5,
				anagramLength: '',
				possibilities: '',
				inputIsVisible: false,
				userAnswer: [],
				newBaseArray: Array,
				anagramWord: '',
				randomIndex: '',
			};
		},
		methods: {
			config() {
                this.screen = 'config';
				this.configReset();
			},
			configReset() {
				this.anagramLength = '';
				this.$refs.toggleFocus.focus();
			},
			play() {
				this.screen = 'play';
				this.startTimer();
				this.gameGuts();
				this.possibilities = this.newBaseArray.length;
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
			showInput() {
				this.autofocus();
			},
			gameGuts() {
				this.newBaseArray = [];
				this.anagrams = JSON.parse(JSON.stringify(anagramData));
				this.randomChoice = this.anagrams[this.anagramLength];
				this.randomIndex = Math.floor(Math.random() * this.randomChoice.length);
				this.anagrandom = this.randomChoice[this.randomIndex];
				for (var i = 1; i < this.anagrandom.length; i++) {
					this.newBaseArray.push(this.anagrandom[i]);
				}
				this.anagramWord = this.anagrandom[0].toUpperCase();
				this.score = 0;
			},
			incrementCounter(correctGuess) {
				let index = this.newBaseArray.indexOf(correctGuess);
				this.newBaseArray.splice(index, 1);
				this.score++;
				this.possibilities--;
				if (this.possibilities === 0) {
					this.gameGutsPartDeux();
				}
			},
			gameGutsPartDeux() {
				this.randomChoice.splice(this.randomIndex, 1);
				this.randomIndex = Math.floor(Math.random() * this.randomChoice.length);
				if (this.possibilities === 0 && this.randomChoice.length === 0) {
					clearInterval(this.timer);
				} else {
					this.anagrandom = this.randomChoice[this.randomIndex];
					for (var i = 1; i < this.anagrandom.length; i++) {
						this.newBaseArray.push(this.anagrandom[i]);
						this.anagramWord = this.anagrandom[0].toUpperCase();
						this.possibilities = this.newBaseArray.length;
					}
				}
			},
			restart() {
				this.score = 0;
				this.startTimer();
				this.gameGuts();
				this.possibilities = this.newBaseArray.length;
			},
			async recordScore() {
				const data = {
					'user-name': this.userName,
					score: this.score,
					game: 'ANAGRAM',
				};

				const response = (await this.axios.post('/record-score/', data)).data;

				console.log(response);
			},
		},
	};
</script>

<style>
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
