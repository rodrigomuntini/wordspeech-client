<template>
    <div class="write">
    <p class="question">Qual palavra completa melhor a frase?</p>
    <p class="phrase">{{sentence.phrase}}
        <img src="../assets/Img/mic.png" style="width:30px;height:30px; padding-left: 25%;" >
    </p>
    <p class="question">Escolha a palavra correta:</p>
        <button class="item">{{sentence.correct_word}}</button>
        <button class="item">table</button>
        <button class="item">jojo</button>
        <button class="item">baby</button>

</div>
</template>

<script>
import $ from 'jquery';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';
export default {
    name:'LifeCycle',
    data() {
        return {
        sentence: [],
        };
    },
  mounted() {
        $.ajax({
        url: 'http://localhost:8000/api/sentences',
        method: 'GET',
        dataType: 'json',
        success:(data) => {
            this.sentence = data[0];
        },
        error: (error) => {
            console.log(error);
        },
        });
    },
};
</script>

<style>
.write{
    padding-top: 200px;
    color:rgb(96, 100, 100);
    font-size: 40px;
}

.question{
    font-size: 50px;
}

.phrase{
    border-radius: 10px;
	box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.5);
}

.item{
    flex-direction: row;
    display: inline-block;
    margin-right: 50px;
    font-size: 50px;
    color: rgb(8, 68, 151);
    border-radius: 10px;
	box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);
    background-color: #fff;

}
</style>