import flask
from flask import request, jsonify, make_response
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = flask.Flask(__name__)
app.config["DEBUG"] = True

chatbot = ChatBot('takarai48')

trainer = ListTrainer(chatbot)

trainer.train([
    "apa itu cv",
    "Commanditer Vennootschap Adalah suatu bentuk badan usaha berupa persekutuan yang didirikan oleh dua orang atau lebih dimana sebagian para anggotanya memiliki tanggung jawab yang tak terbatas dan sebagian anggota lainnya memiliki tanggung jawab yang terbatas. Commanditer Vennootschap ( CV ) didirikan dengan Akta dan harus didaftarkan",
])

trainer.train([
    "apakah cv badan hukum",
    "Commanditer Vennootschap ( CV ) Bukan usaha yang berbadan hukum karena tidak ada regulasi yang mengaturnya. Sesuai dengan namanya, Commanditer V ennootschap ( CV )adalah bentuk badan usaha warisan Kolonial Belanda",
])


@app.route('/asistant', methods=['POST'])
def chat():
    data = request.get_json()

    response = chatbot.get_response(data['data'])
    return jsonify({
        'message' : str(response)
    })
    # return 

app.run()