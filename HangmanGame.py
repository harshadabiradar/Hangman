import random

def choose_word():
    word_list = ["hangman", "python", "programming", "developer", "challenge"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def main():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6  # You can adjust the number of attempts

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nAttempts left:", attempts)
        print("Word:", display_word(word_to_guess, guessed_letters))
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word_to_guess:
            print("Good guess!")
        else:
            print("Oops, that letter is not in the word.")
            attempts -= 1
        
        if set(word_to_guess).issubset(set(guessed_letters)):
            print("\nCongratulations! You guessed the word:", word_to_guess)
            break
    
    if attempts == 0:
        print("\nGame over! The word was:", word_to_guess)

if __name__ == "__main__":
    main()
