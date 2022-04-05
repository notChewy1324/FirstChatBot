from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("TrainData")
trainer = ChatterBotCorpusTrainer(chatbot)