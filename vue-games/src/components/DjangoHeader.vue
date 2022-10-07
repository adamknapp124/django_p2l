<template>
	<header>
		<nav
			class="navbar navbar-expand-sm navbar-dark bg-dark fixed-top"
			id="topNav"
		>
			<div class="container-fluid">
				<a class="navbar-brand" href="">LTP</a>
				<button
					class="navbar-toggler"
					type="button"
					data-toggle="collapse"
					data-target="#navbarResponsive"
				>
					<span class="navbar-toggler-icon"></span>
				</button>
				<div class="collapse navbar-collapse" id="navbarResponsive">
					<ul class="navbar-nav ml-auto">
						<li class="nav-item active">
							<a class="nav-link" href="">Home</a>
						</li>
						{% if not user.is_authenticated %}
						<li class="nav-item">
							<a
								class="nav-link"
								href="{% url 'account_login' %}"
							>
								Log in
							</a>
						</li>
						<li class="nav-item">
							<a
								class="nav-link"
								href="{% url 'account_signup' %}"
							>
								Sign up
							</a>
						</li>
						{% else %}
						<li class="nav-item dropdown" id="navDropdown">
							<a
								href="#"
								class="nav-link dropdown-toggle"
								data-toggle="dropdown"
								aria-haspopup="true"
								aria-expanded="false"
							>
								Games
							</a>
							<ul
								class="dropdown-menu"
								aria-labelledby="navDropdown"
							>
								<li class="nav-item dropdown">
									<a
										class="dropdown-item"
										href="/anagram-game"
									>
										Anagram Hunt
									</a>
								</li>
								<li class="nav-item dropdown">
									<a class="dropdown-item" href="/math-game">
										Math Facts Practice
									</a>
								</li>
								<li class="nav-item dropdown">
									<a
										href="/game-scores"
										class="dropdown-item"
									>
										Game Scores
									</a>
								</li>
							</ul>
						</li>
						<li class="nav-item dropdown">
							<a
								class="nav-link dropdown-toggle"
								href="#"
								id="navbarDropdown"
								role="button"
								data-toggle="dropdown"
								aria-haspopup="true"
								aria-expanded="false"
							>
								Profile
							</a>
							<div
								class="dropdown-menu"
								aria-labelledby="navbarDropdown"
							>
								<a
									class="dropdown-item"
									href="{% url 'my-account' %}"
								>
									My Account
								</a>
								<a class="dropdown-item" href="#">My Scores</a>
								<div class="dropdown-divider"></div>
								<form
									method="post"
									action="{% url 'account_logout' %}"
								>
									{% csrf_token %}
									<button class="btn dropdown-item">
										Log out
									</button>
								</form>
							</div>
						</li>
						{% endif %}
						<li class="nav-item">
							<a
								class="nav-link"
								href="{% url 'pages:about-us' %}"
							>
								About
							</a>
						</li>
					</ul>
				</div>
			</div>
		</nav>
	</header>
</template>

<script>
export default {
	name: 'DjangoHeader',
};
</script>
