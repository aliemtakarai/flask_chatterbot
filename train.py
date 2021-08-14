from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Charlie
chatbot = ChatBot('takarai48')

trainer = ListTrainer(chatbot)

trainer.train([
    "Apa itu CV",
    "Commanditer Vennootschap Adalah suatu bentuk badan usaha berupa persekutuan yang didirikan oleh dua orang atau lebih dimana sebagian para anggotanya memiliki tanggung jawab yang tak terbatas dan sebagian anggota lainnya memiliki tanggung jawab yang terbatas. Commanditer Vennootschap ( CV ) didirikan dengan Akta dan harus didaftarkan",
])

trainer.train([
    "Apa yang dimaksud CV",
    "CV Adalah",
])

while True:
    request = input('You : ')
    response = chatbot.get_response(request)
    print ('bot: ', response)