<template>
    <div class="write">
        <p class="question">Qual palavra completa melhor a frase?</p>
        <div class="error-message" v-if="show_error">
            <p>Erro: {{ error_message }}</p>
        </div>
        <p class="phrase">{{ sentence.phrase }}
            <button type="button" class="microphone-button" v-on:click="toggleRecording">
                <img src="../assets/Img/mic.png" style="width:30px;height:30px; padding-left: 25%;">
            </button>
        </p>
        <p class="question">Escolha a palavra correta:</p>
        <button class="item" v-for="item in items"
            v-bind:class="{ 'bg-green': is_correct && item === sentence.correct_word, 'bg-red': is_incorrect && item === current_text }">{{ item }}</button>
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
            items: ['table', 'join', 'force', 'cat'],
            sentence: [],
            show_error: false,
            error_message: "Error",
            is_correct: false,
            is_incorrect: false,
            current_text: ""
        }
    },
    mounted() {
        $.ajax({
            url: 'http://localhost:5000/api/question',
            method: 'GET',
            dataType: 'json',
            success: (data) => {
                // Armazena a sentença (pergunta e resposta certa na variavel sentence)
                this.sentence = data[0];
                // Armazena as alternativas nos itens
                this.items = data[1];

                // Faz o tratamento na frase da sentença para apresentar ____ em fez de $
                this.sentence.phrase = this.sentence.phrase.replace(/\$/g, '___')
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

                    this.stopRecordingAfterDelay(5000);
                });
            }
        },
        stopRecordingAfterDelay(delayMs) {
            setTimeout(() => {
                if (this.isRecording) {
                    this.recorder.stopRecording(() => {
                        this.audioBlob = this.recorder.getBlob();
                        this.recorder.destroy();
                        this.recorder = null;
                        this.isRecording = false;
                        this.saveRecording();
                    });
                }
            }, delayMs);
        },
        saveRecording() {
            // envia a gravação para o servidor ou salva localmente
            const formData = new FormData();
            formData.append('audio', this.audioBlob, 'recording.webm');
            // faça uma requisição AJAX para enviar o arquivo para o servidor

            $.ajax({
                url: 'http://localhost:5000/api/recognition',
                type: 'POST',
                data: formData,
                processData: false,
                contentType: false,
                success: (data) => {
                    console.log('Arquivo enviado com sucesso!');
                    this.judgeQuestion(data)
                },
                error: (error) => {
                    console.error('Erro ao enviar arquivo:', error);
                },
            });
        },
        judgeQuestion(text) {
            if (this.items.includes(text)) { // Significa que a palavra está incluída entre as 4 opções
                // Reseta as mensagens de erro
                this.show_error = false
                this.error_message = "Error"

                if (text.toLowerCase() == this.sentence.correct_word.toLowerCase()) { // Verifica se valou a palavra certa
                    this.is_correct = true;
                    this.is_incorrect = false;
                } else {
                    this.is_correct = false;
                    this.is_incorrect = true;
                    this.current_text = text;
                    console.log(false)
                }
            } else {
                this.show_error = true
                this.error_message = "Palavra não identificada"
            }
        }
    },
}
</script>



<style>
.write {
    padding-top: 200px;
    color: rgb(96, 100, 100);
    font-size: 40px;
}

.question {
    font-size: 50px;
}

.phrase {
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

.error-message {
    background-color: #ffcccc;
    border: 2px solid #ff0000;
    color: #ff0000;
    padding: 10px;
    border-radius: 5px;
    font-size: 30px;
}

.bg-green {
    background-color: green;
    color: white;
}

.bg-red {
    background-color: red;
    color: white;
}
</style>