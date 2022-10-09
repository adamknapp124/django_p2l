<template>
	<div>
		<label :for="id">{{ label }}</label>
		<select
			:id="id"
			:value="currentValue"
			@input="$emit('input', $event.target.value)"
		>
			<option
				v-for="option in options"
				:key="option[1]"
				:value="option[1]"
			>
				{{ option[0] }}
			</option>
		</select>
	</div>
</template>

<script>
export default {
	name: 'SelectInput',
	props: {
		id: String,
		label: String,
		options: Array,
		currentValue: String,
	},
};
</script>
