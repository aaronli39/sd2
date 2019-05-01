import random

def make_greeting(f):
    ret = f()
    def inner():
        return "<h1>" + ret + "</h1>"
    return inner

@make_greeting
def greet():
    greetings = ["Hello", "Welcome","AYO", "Hola", "Bonjour", "Word Up"]
    return random.choice(greetings)
print(greet())