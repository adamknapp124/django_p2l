<template>
    <form>
        <div id="review">
            <p>Leave a review!</p>
            <label>First Name:</label>
            <input required v-model="fname">
            <label>Last Name:</label>
            <input required v-model="lname">
            <label>Email:</label>
            <input type="email" required v-model="email">
            <label>Rating:</label>
            <input type="range" v-model="value" min="1" max="5">
            <label>Review:</label>
            <textarea v-model="review" placeholder="Please type your review here" cols="30" rows="5"></textarea>
            <input type="submit" @click="logReview">
        </div>
    </form>
</template>

<script>
    export default {
        data() {
            return {
                fname: '',
                lname: '',
                email: '',
                review: '',
                value: 1,
            }
        },
        methods: {
            async logReview() {
				const data = {
                    fname: this.fname,
					lname: this.lname,
                    email: this.email,
                    review: this.review,
                    value: this.value,
				};
				const response = (await this.axios.post('/record-review/', data)).data;
				console.log(response);
            },
        }
    }
</script>

<style>
    form {
        max-width: 420px;
        margin: 30px auto;
        background: white;
        text-align: left;
        padding: 40px;
        border-radius: 10px;
    }
    label {
        color: #aaa;
        display: inline-block;
        margin: 25px 0 15px;
        font-size: 0.6em;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: bold;
    }
    input, select {
        display: block;
        padding: 10px 6px;
        width: 100%;
        box-sizing: border-box;
        border: none;
        border-bottom: 1px solid #ddd;
        color: #555;
    }
    textarea {
        margin-top: 15px;
        resize: None;
    }
    #review {
        border: 1px solid rgb(100, 100, 100);
        padding: 35px;
    }
    v-range-slider {
        max-width: 380px;

    }
</style>