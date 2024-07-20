import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    (r'hi|hello|hey', ['Hello! How can I help you today?', 'Hi there! What can I do for you?']),
    (r'what is your name?', ['I am a chatbot created to assist you.', 'You can call me ChatBot.']),
    (r'how are you?', ['I am just a program, but I am doing great!', 'I am fine, thank you for asking.']),
    (r'what is coding?', ['Coding can be defined as writing instructions for computers and other hardware. The computer is then able to read the instructions (called “programs”) and do what you have asked it to do. Computer language is different from human language.']),
    (r'what is css?', ['CSS is the acronym of “Cascading Style Sheets”. CSS is a computer language for laying out and structuring web pages (HTML or XML). This language contains coding elements and is composed of these “cascading style sheets” which are equally called CSS files (. css).']),
    (r'what is html?', ['HTML stands for Hyper Text Markup Language. HTML is the standard markup language for creating Web pages. HTML describes the structure of a Web page. HTML consists of a series of elements. HTML elements tell the browser how to display the content.']),
    (r'quit', ['Bye! Have a great day!', 'Goodbye!']),
    (r'(.*)', ['I am sorry, I did not understand that.', 'Can you please rephrase your question?'])
]

def chatbot():
    chat = Chat(pairs, reflections)

    print("Hy! I am Chat Bot here to assist you, type quit to exit!")

    while True:
        user_input = input("You: ")
        response = chat.respond(user_input)
        print(f"ChatBot: {response}")

        if user_input == "quit":
            break

if __name__ == "__main__":
    chatbot()