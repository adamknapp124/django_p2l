<template>
	<div class="row mx-1 my-3">
		<label :for="id" class="col font-weight-bold">{{ label }}</label>
		<input
			:id="id"
			:value="currentValue"
			@input="$emit('input', $event.target.value)"
			class="col"
		/>
			<option
				v-for="option in options"
				:key="option[1]"
				:value="option[1]"
			>
				{{ option[0] }}
			</option>
	</div>
</template>

<script>

</script>