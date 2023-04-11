<template>
    <div class="write">
    <p>Qual palavra completa melhor a frase?</p>
    <p class="phrase">{{ phrase }}
        <img src="../assets/Img/mic.png" style="width:30px;height:30px; padding-left: 25%;" >
    </p>
    <p class="item" v-for="(item, index) in items">{{ item }}</p>

</div>
</template>

<script>
export default{
    name:'LifeCycle',
    data(){
        return{
            phrase:"join the darkside of the ___",
            items:['table', 'join', 'force', 'cat']
        }
    }
}
</script>

<style>
.write{
    padding-top: 200px;
    color:rgb(96, 100, 100);
    font-size: 40px;
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

}
</style>