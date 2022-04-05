from chatterbot import ChatBot
from playsound import playsound
import gtts

chatbot = ChatBot("Gracie")

# untrained chatbot
while True:
    
     usr = input("type anything... ")
     TEST_response = chatbot.get_response(f"{usr}")
     print(f"Gracie: {TEST_response}")
     
     tts = gtts.gTTS(f"{TEST_response}", lang="en")
     tts.save("gracieBOT_test_response.mp3")
     playsound("gracieBOT_test_response.mp3")