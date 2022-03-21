from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("FirstChatBot")

chatbotConversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer = ListTrainer(chatbot)

trainer.train(chatbotConversation)

while True:

    usr = input("What would you like to say... ")
    response = chatbot.get_response(f"{usr}")
    print(f"ChatBot: {response}")