import random

# Fruit Quiz using OOP

class FruitQuiz:

    # Constructor
    def __init__(self):
        # Dictionary of fruits and their colors
        self.fruits = {
            "apple": "red",
            "orange": "orange",
            "watermelon": "green",
            "banana": "yellow",
            "grapes": "purple",
            "mango": "yellow"
        }

    # Quiz method
    def quiz(self):
        while True:
            # Select a random fruit
            fruit, color = random.choice(list(self.fruits.items()))

            # Ask the question
            print("\nWhat is the color of", fruit + "?")
            user_answer = input("Your answer: ")

            # Check the answer
            if user_answer.lower() == color:
                print("✅ Correct Answer!")
            else:
                print("❌ Wrong Answer!")
                print("The correct answer is:", color)

            # Ask if the user wants to continue
            choice = input("\nDo you want to play again? (yes/no): ").lower()

            if choice == "no":
                print("\nThank you for playing the Fruit Quiz!")
                break


# Main Program
print("=== Welcome to the Fruit Quiz ===")

fq = FruitQuiz()
fq.quiz()