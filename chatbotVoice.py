from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from playsound import playsound
import requests
import gtts

chatbot = ChatBot("Gracie")

testConversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)
trainer.train(testConversation)

response = chatbot.get_response("how is your day")
print(f"Gracie: {response}")