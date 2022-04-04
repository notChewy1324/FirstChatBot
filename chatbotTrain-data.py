from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Jackson")

testConvo_data = [
    "hi there",
    "hello"
]

ChatterBotCorpusTrainer.train("chatterbot.corpus.english")