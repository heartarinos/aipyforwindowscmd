import random
import re
import string

class ComplexAI:
    def __init__(self):
        self.relevant_words = set()
        self.conversation = []

    def process_input(self, user_input):
        words = user_input.split()
        relevant_words = [word.lower() for word in words if word.isalpha()]
        self.relevant_words.update(relevant_words)

        # Convert to lowercase and remove punctuation
        user_input = re.sub('[^A-Za-z0-9\s]', '', user_input).lower()

        return user_input

    def generate_response(self, user_input):
        relevant_words = self.relevant_words
        conversation = self.conversation
        response = ' ' + user_input + ' '

        # Check for various user inputs and respond accordingly
        if 'hello' in relevant_words:
            response = "Hello there! I'm your friendly AI assistant. How can I help you today?"
        elif 'goodbye' in relevant_words:
            response = "Goodbye! Take care and have a great day!"
        elif 'joke' in relevant_words:
            response = self.tell_joke()
        elif any(word.startswith('how') for word in relevant_words):
            response = self.respond_to_how_question()
        elif any(word.startswith('who') for word in relevant_words):
            response = self.respond_to_who_question()
        elif any(word.startswith('what') for word in relevant_words):
            response = self.respond_to_what_question()
        else:
            response = self.continue_conversation()

        self.conversation.append(response)
        return response

    def tell_joke(self):
        jokes = [
            "Why did the chicken cross the road? To get to the other side! :)",
            "What do you call an angry turnip? A steamed veggie!",
            "I'm not sure, but I'll consult my magical AI powers and get back to you."
        ]
        return random.choice(jokes)

    def respond_to_how_question(self):
        return "That's a great question! I'll do my best to provide an answer."

    def respond_to_who_question(self):
        return "Hmm, let me think... That's a tricky one! I'll need more context."

    def respond_to_what_question(self):
        return "What do you want to know about? You're throwing me into the deep end here!"

    def continue_conversation(self):
        context_words = [word for word in self.relevant_words if word not in ['i', 'you', 'it', 'and', 'for']]
        response = "Sure, let's continue our conversation. Contextual words: {}".format(context_words)
        return response

if __name__ == "__main__":
    ai = ComplexAI()

    while True:
        user_input = input("> ")
        processed_input = ai.process_input(user_input)
        response = ai.generate_response(processed_input)

        print(response)
