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

# displays response
TEST_response = chatbot.get_response("tell me something random") # the usr input as str for the chatbot
print(f"Gracie: {TEST_response}")

# voice
tts = gtts.gTTS(f"{TEST_response}", lang="en") # change the 'lang' to change the output language
tts.save("gracieBOT_test_response.mp3")
playsound("gracieBOT_test_response.mp3")