# Flashcard Application using OOP

class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    # String representation of the object
    def __str__(self):
        return f"{self.word} ({self.meaning})"


# List to store flashcards
flashcards = []

print("=== Welcome to the Flashcard Application ===")

# Loop to add flashcards
while True:
    word = input("\nEnter the word: ")
    meaning = input("Enter its meaning: ")

    # Create a flashcard object and add it to the list
    flashcards.append(Flashcard(word, meaning))

    choice = input("Do you want to add another flashcard? (yes/no): ").lower()

    if choice == "no":
        break

# Display all flashcards
print("\n=== Your Flashcards ===")
for card in flashcards:
    print("•", card)