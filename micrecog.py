from flask import Flask, request
from flask_cors import CORS
import speech_recognition as sr

app = Flask(__name__)
CORS(app)

# Inicializa o reconhecedor
r = sr.Recognizer()

# Rota que recebe o arquivo de áudio enviado pelo JavaScript
@app.route('/upload', methods=['POST'])
def upload():
    # Obtém o arquivo de áudio enviado pelo JavaScript
    audio_file = request.files['audio']

    # Salva o arquivo de áudio em um local específico
    audio_file.save('audio.webm')

    # Faz o reconhecimento da palavra
    text = make_speech_recognition()

    # Retorna uma resposta para o JavaScript
    return text

def make_speech_recognition():
    with sr.AudioFile('audio.webm') as source:
        # Lê o áudio do arquivo
        audio = r.record(source)

        try:
            # Usa o Google Speech Recognition para reconhecer a fala
            text = r.recognize_google(audio, language='en')
            return text
        except sr.UnknownValueError:
            return 'Não foi possível reconhecer a fala'
        except sr.RequestError as e:
            return 'Erro ao se comunicar com o serviço de reconhecimento de fala: {0}'.format(e)


if __name__ == '__main__':
    app.run(debug=True)
