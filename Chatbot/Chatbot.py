from __future__ import print_function
from nltk.chat.util import Chat, reflections

pairs = (
    (r'I need (.*)',
    ( "Why do you need %1?",
      "Would it really help you to get %1?",
      "Are you sure you need %1?")),
    
    (r'Why don\'t you (.*)',
    ( "Do you really think I don't %1?",
      "Perhaps eventually I will %1.",
      "Do you really want me to %1?")),
    
    (r'(.*)\?',
    ( "Why do you ask that?",
      "Please consider whether you can answer your own question.",
      "Perhaps the answer lies within yourself?",
      "Why don't you tell me?")),
    
    (r'quit',
    ( "Thank you for talking with me.",
      "Good-bye.",
      "Thank you, that will be $150.  Have a good day!")),

    (r'(.*)',
    ( "Please tell me more.",
      "Let's change focus a bit... Tell me about your family.",
      "Can you elaborate on that?",
      "Why do you say that %1?",
      "I see.",
      "Very interesting.",
      "%1.",
      "I see.  And what does that tell you?",
      "How does that make you feel?",
      "How do you feel when you say that?"))
)

eliza_chatbot = Chat(pairs, reflections)

def eliza_chat():
    print("Therapist\n---------")
    print("Talk to the program by typing in plain English, using normal upper-")
    print('and lower-case letters and punctuation. Enter "quit" when done.')
    print('='*72)
    print("Hello. How are you feeling today?")

eliza_chatbot.converse()
def demo():
     eliza_chat()
if __name__ == "__main__":
    demo()
