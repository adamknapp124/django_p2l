<template>
	<footer class="fixed-bottom bg-light row">
		<div class="col">
			<div class="float-right m-1 mr-2">
				Copyright &copy; 2020 Play to Learn.
			</div>
			<nav>
				<ul class="nav">
					<li class="nav-item">
						<a class="nav-link" href="{% url 'pages:contact' %}">
							Contact
						</a>
					</li>
					{% if user.is_staff %}
					<li class="nav-item">
						<a class="nav-link" href="/admin/">Admin</a>
					</li>
					{% endif %}
				</ul>
			</nav>
		</div>
	</footer>
</template>

<script>
export default {
	name: 'DjangoFooter',
};
</script>
