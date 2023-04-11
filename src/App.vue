<template>
<div>
    <header>
        <h1>WordSpeech</h1>
    </header>
</div>

<div class="container">
    <div class="box">   
        <LifeCycle/>
    </div>
</div>

</template>

<script>
import LifeCycle from './components/LifeCycle.vue';
export default{
    name:'App',
    components:{
        LifeCycle
    }
}

</script>

<style>
body{
    background-color: #17a0e5;
    color: #fff;
    text-align: center;
    font-family: sans-seri;
    margin: 0px;

}

.container{
    width: 100%;
    height: 100%;
    background: #17a0e5;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: row;

}

.box{
    width: 800px;
    height: 800px;
    background-color: #fff;
    border-radius: 10px

    
}

</style>