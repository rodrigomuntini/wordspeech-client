<template>
    <div class="write">
    <p class="question">Qual palavra completa melhor a frase?</p>
    <p class="phrase">{{sentence.phrase}}
        <button type="button" class="microphone-button" v-on:click="toggleRecording">
            <img src="../assets/Img/mic.png" style="width:30px;height:30px; padding-left: 25%;">
        </button>
    </p>
    <p class="question">Escolha a palavra correta:</p>
        <button class="item">{{sentence.correct_word}}</button>
        <button class="item">table</button>
        <button class="item">jojo</button>
        <button class="item">baby</button>
    </div>
</template>

<script>
import $ from 'jquery'
import RecordRTC from 'recordrtc'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';

export default {
    name: 'LifeCycle',
    data() {
        return {
            phrase: "join the darkside of the ___",
            items: ['table', 'join', 'force', 'cat'],
            sentence: [],
        }
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
    methods: {
        toggleRecording() {
            if (this.isRecording) {
                // parar a gravação
                this.recorder.stopRecording(() => {
                    this.audioBlob = this.recorder.getBlob();
                    this.recorder.destroy();
                    this.recorder = null;
                    this.isRecording = false;
                    this.saveRecording();
                });
            } else {
                // iniciar a gravação
                navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
                    this.recorder = RecordRTC(stream, {
                        type: 'audio',
                        mimeType: 'audio/webm',
                        recorderType: RecordRTC.StereoAudioRecorder,
                        desiredSampRate: 16000,
                    });
                    this.recorder.startRecording();
                    this.isRecording = true;
                });
            }
        },
        saveRecording() {
            // envia a gravação para o servidor ou salva localmente
            const formData = new FormData();
            formData.append('audio', this.audioBlob, 'recording.webm');
            // faça uma requisição AJAX para enviar o arquivo para o servidor

            $.ajax({
                url: 'http://localhost:5000/upload',
                type: 'POST',
                data: formData,
                processData: false,
                contentType: false,
                success: (data) => {
                    console.log('Arquivo enviado com sucesso!');
                    console.log(data)
                },
                error: (error) => {
                    console.error('Erro ao enviar arquivo:', error);
                },
            });
        },
    },
}
</script>



<style>
.write {
    padding-top: 200px;
    color: rgb(96, 100, 100);
    font-size: 40px;
}

.question{
    font-size: 50px;
}

.phrase{
    border-radius: 10px;
    box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.5);
}

.item {
    flex-direction: row;
    display: inline-block;
    margin-right: 50px;
    font-size: 50px;
    color: rgb(8, 68, 151);
    border-radius: 10px;
	box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);
    background-color: #fff;
}

.microphone-button {
    border-radius: 999px;
}

button {
    cursor: pointer;
}
</style>