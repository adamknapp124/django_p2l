<template>
	<main>
		<div id="equation" class="row">
			<div class="col-6">{{ question }}</div>
			<div class="col-6">{{ wordsRemaining }}</div>
		</div>
		<hr />
		<div class="row">
			<div class="col-12">
				<input
					ref="userInput"
					id="userInput"
					v-model="input"
					class="form-control text-center"
					autocomplete="off"
					type="text"
					placeholder="type here"
					v-on:keyup.enter="checkAnswer"
				/>
			</div>
		</div>
		<hr />
		<div v-for="words in this.correctGuesses" :key="words">{{ words }}</div>
		<div class="form-group">
			<div class="row justify-content-center m-auto">
				<div class="col-12 mt-3" id="submitButton">
					<button
						type="button"
						class="btn btn-primary form-control m-1"
						id="startButton"
						@click="this.checkAnswer"
					>
						Enter
					</button>
				</div>
			</div>
		</div>
	</main>
</template>

<script>
export default {
	mounted() {
		this.$refs.userInput.focus();
	},
	data: function () {
		return {
			correctGuesses: [],
			input: '',
		};
	},
	name: 'WordEquation',
	props: {
		question: String,
		wordsRemaining: Number,
		newBaseArray: Array,
		index: Number,
	},
	methods: {
		checkAnswer() {
			if (this.newBaseArray.includes(this.input)) {
				this.correctGuesses.push(this.input);
				this.$emit('test-click', this.input);
				this.input = '';
				this.$refs.userInput.focus();
			} else {
				this.input = '';
				this.$refs.userInput.focus();
			}
		},
	},
};
</script>

<style scoped>
#equation {
	font-size: 1.6em;
	margin: auto;
	width: 90%;
}
</style>
