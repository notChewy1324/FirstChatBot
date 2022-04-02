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

# untrained chatbot
while True:
    
     usr = input("type anything... ")
     TEST_response = chatbot.get_response(f"{usr}")
     print(f"Gracie: {TEST_response}")
     
     tts = gtts.gTTS(f"{TEST_response}", lang="en")
     tts.save("gracieBOT_test_response.mp3")
     playsound("gracieBOT_test_response.mp3")