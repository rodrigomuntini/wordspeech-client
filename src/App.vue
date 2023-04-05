<template>
<h1>WORDSPEECH</h1>
<div>
    <p>Message is: {{ message }}</p>
<input v-model="message" placeholder="digite palavra em ingles" />

</div>
</template>

<script>
    export default{
        name: 'App',
        data() {
            return{
            message: ""
            }
        }
    }
</script>

<style>
    body{
        background-color: rgb(60, 175, 237);
        color: #ffffff;
        align-items: center;
    }

</style>