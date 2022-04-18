from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("TrainData")
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train(
   # "chatterbot.corpus.english",
    "corpusData/corupusTrain_test_2.json"
)