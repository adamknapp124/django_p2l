<template>
	<main class="m-4 pb-5">
		<div class="home row align-items-center m-auto pb-5">
			<div class="bg-warning w-100">
				<div class="home-title text-center text-dark">
					Welcome to Play to Learn
				</div>
				<div class="home-title-caption lead text-center">
					your number one source for free online learning!
				</div>
			</div>
			<div
				id="myCarousel"
				class="carousel border-dark"
				data-ride="carousel"
				data-interval="10000">
				<ol class="carousel-indicators carousel-indicator-important">
					<li
						data-target="#myCarousel"
						data-slide-to="0"
						class="active"></li>
					<li data-target="#myCarousel" data-slide-to="1"></li>
					<li data-target="#myCarousel" data-slide-to="2"></li>
				</ol>
				<div class="carousel-inner">
					<div class="carousel-item active">
						<div class="carousel-darkening-overlay"></div>
						<img
							src="static/image/carouselImage1Cropped.jpg"
							id="firstCarouselImage"
							alt="First Slide"
							class="d-block w-100" />
						<div
							class="carousel-caption carousel-caption-important lead m-auto">
							"By far the easiest way to learn!"
						</div>
					</div>
					<div class="carousel-item">
						<div class="carousel-darkening-overlay"></div>
						<img
							src="static/image/carouselImage2Cropped.jpg"
							id="SecondCarouselImage"
							alt="Second Slide"
							class="d-block w-100" />
						<div
							class="carousel-caption carousel-caption-important lead m-auto">
							"These games make me want to learn!"
						</div>
					</div>
					<div class="carousel-item">
						<div class="carousel-darkening-overlay"></div>
						<img
							src="static/image/carouselImage3Cropped.jpg"
							id="thirdCarouselImage"
							alt="Third Slide"
							class="d-block w-100" />
						<div
							class="carousel-caption carousel-caption-important lead m-auto">
							"Easy to play on mobile or on desktop!"
						</div>
					</div>
					<a
						href="#myCarousel"
						class="carousel-control-prev"
						role="button"
						data-slide="prev">
						<span class="carousel-control-prev-icon"></span>
					</a>
					<a
						href="#myCarousel"
						class="carousel-control-next"
						role="button"
						data-slide="next">
						<span class="carousel-control-next-icon"></span>
					</a>
				</div>
			</div>
			<div class="row pt-1 w-100 m-auto">
				<div class="col-sm-12 col-md-6 card text-center border-0">
					<img
						src="static/image/anagram.png"
						class="card-img-top"
						alt="..." />
					<div class="card-body">
						<h5 class="card-body-title">Anagram Hunt</h5>
						<p class="card-body-caption">
							In exchange for clicking the button below, you will
							be given a word. You will choose the length of the
							word. From that word, you will birth new words. At
							the end there will be a giant billboard that tells
							your how good (or bad) you did!
						</p>
					</div>
					<a href="/anagramhunt" class="btn btn-warning m-3">
						Play this one!
					</a>
				</div>
				<div class="col-sm-12 col-md-6 card text-center border-0">
					<img
						src="static/image/mathfacts.jpg"
						class="card-img-top"
						alt="..." />
					<div class="card-body">
						<h5 class="card-body-title">Math Facts Practice</h5>
						<p class="card-body-caption">
							But if you were to click THIS button (look down) You
							will have 30 seconds to rapidly come up with the
							answer to 10 extremely simple math equations. If you
							can master all 4 operations offered to you, you will
							be the recipient of the most bragging rights you
							have ever had to the right to. Ever. Oh and see a
							scoreboard.
						</p>
					</div>
					<a href="/mathfacts" class="btn btn-warning m-3">
						No, play this one!
					</a>
				</div>
				<button class="m-auto">This is HomeVue.vue</button>
			</div>
		</div>
	</main>
</template>

<script>
	export default {
		name: 'AnagramGame',
		data() {
			return {
				userName: '',
				score: 0,
			};
		},
		methods: {
			async recordScore() {
				const data = {
					'user-name': this.userName,
					score: this.score,
					game: 'ANAGRAM',
				};

				const response = (await this.axios.post('/record-score/', data))
					.data;

				console.log(response);
			},
		},
	};
</script>

<style scoped>
	div,
	label {
		padding: 0.2rem;
	}
</style>
