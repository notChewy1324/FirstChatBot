from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import requests

chatbot = ChatBot("FirstChatBot")

chatbotConversation = []
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

def adviceInfo():
    try:
        adviceAPI = requests.get("https://api.adviceslip.com/advice")
    except:
        print("")  
        
    advice = adviceAPI.json()["slip"]
    advice = advice["advice"]
    chatbotConversation.append(advice)

print("Loading Chatbot...")
while (len(chatbotConversation) <= 5): #this controls the length of the list
    adviceInfo()
    
trainer = ListTrainer(chatbot)

trainer.train(conversation)

def responsePicker(usr):
    if (len(usr) <= 19):
        print("ChatBot: " + str(chatbot.get_response(f"{usr}")))
    elif (len(usr) >= 20):
        print("ChatBot: " + str(chatbot.get_response(f"{chatbotConversation}")))


while True:

    usr = input("What advice would you like... ")
    print(f"{responsePicker(usr)}")
response = chatbot.get_response("Good morning!")
print("ChatBot: " + response)
