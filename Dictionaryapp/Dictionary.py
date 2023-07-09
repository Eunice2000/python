dictionary = {
    "apple": "A round fruit with red or green skin and a crisp flesh.",
    "banana": "A long curved fruit with a yellow skin.",
    "cat": "A small domesticated carnivorous mammal with soft fur.",
    "dog": "A domesticated carnivorous mammal with a wagging tail and a loyal nature.",
    "elephant": "A large mammal with a long trunk and tusks.",
    "flower": "The reproductive structure found in plants, often brightly colored.",
    "guitar": "A musical instrument with strings played by strumming or plucking.",
    "happiness": "A state of joy, contentment, or satisfaction.",
    "internet": "A global computer network providing information and communication.",
    "jazz": "A genre of music characterized by improvisation and syncopation.",
    "kangaroo": "A marsupial native to Australia with powerful hind legs.",
    "lamp": "A device that produces light, typically using electricity or gas.",
    "mountain": "A large natural elevation of the Earth's surface with steep sides.",
    "nightingale": "A small songbird known for its melodious singing.",
    "oxygen": "A chemical element necessary for respiration and combustion.",
    "pizza": "A savory dish typically made of a round flattened bread topped with cheese and various toppings.",
    "quantum": "In physics, the smallest discrete unit of any physical property.",
    "robot": "A machine capable of carrying out complex actions and tasks automatically.",
    "sunflower": "A tall plant with a large yellow flower that follows the movement of the sun.",
    "tiger": "A large carnivorous feline with a striped coat.",
    "umbrella": "A device used to protect against rain or sunlight, consisting of a collapsible canopy and a handle.",
    "violin": "A string instrument played with a bow, producing melodic sounds.",
    "waterfall": "A cascade of water falling from a height, often found in rivers or streams.",
    "xylophone": "A musical instrument consisting of a series of wooden bars played by striking with mallets.",
    "yoga": "A practice that combines physical postures, breathing exercises, and meditation for relaxation and well-being.",
    "zebra": "A wild animal with black and white stripes native to Africa.",
    "eunice": "A freelancer, devops engineer"
}

def prompt_user():
    print("Welcome to the Python Dictionary App! created by Adediran Eunice")
    print("Welcome to the Python Dictionary App! This command-line application is designed to help you quickly look up word definitions right from your terminal. Whether you're a student, a writer, or simply curious about the meaning of words, this app has got you covered.")
    print("To exit the app, enter 'exit' or press Ctrl+C.\n")

def lookup_word(word):
    if word in dictionary:
        print(f"\nDefinition of '{word}':")
        print(dictionary[word])
    else:
        print(f"\n'{word}' sorry! words not found in the dictionary.")

def run_dictionary_app():
    prompt_user()
    while True:
        user_input = input("Search for a word: ")
        if user_input.lower() == "exit":
            print("Thank you for using the Python Dictionary App! We hope it has been helpful in expanding your vocabulary and providing quick access to word definitions. If you have any further questions or need assistance in the future, feel free to come back and use the app again.Farewell for now, and may your journey with words\nbe filled with curiosity and discovery. Goodbye!")
            break
        lookup_word(user_input)

run_dictionary_app()
