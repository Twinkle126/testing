from flask import Flask, render_template, request
from chat_bot import bot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import speech_recognition as sr
import nltk

nltk.download('punkt')

# training chatbot on wine related questions
trainer = ListTrainer(bot)
trainer.train(["Can you tell me about wine",
               "Give me wine name"]
              )
trainer = ListTrainer(bot)
trainer.train(["tell me about wine",
               "Give me wine name"]
              )
# training chatbot on greetings and conversations
_trainer = ChatterBotCorpusTrainer(bot)
_trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)
app = Flask(__name__)


# function for the render chatbot template
@app.route("/")
def index():
    return render_template("index.html")


# function for the text conversation response
@app.route("/get_response")
def get_bot_response():
    text = request.args.get('msg')
    bot_response = bot.get_response(text)
    return str(bot_response)


# function  for the voice enabled conversation response
@app.route("/mic_recognition")
def mic_input():
    bot_response = 'Thankyou for visit'
    response = recognize_speech_from_mic()
    voice = response['transcription']
    if response['transcription'] != None:
        bot_response = bot.get_response(voice)
        bot_response = str(voice) + ',' + str(bot_response)
        return str(bot_response)
    else:
        bot_response = str(voice) + ',' + str(bot_response)
        return str(bot_response)


# function is used to for voice recognition
def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(mic, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")
    with mic as source:
        print('speak..')
        recognizer.adjust_for_ambient_noise(source)  # #  analyze the audio source for 1 second
        audio = recognizer.listen(source)
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable/unresponsive"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"
    return response


if __name__ == "__main__":
    app.run()
