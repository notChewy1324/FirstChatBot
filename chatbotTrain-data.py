from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Jackson")
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
    "chatterbot.corpus.english",
    "chatterbot.corpus.spanish",
    "corpusData/corupusTrain_test_2.json"
    )