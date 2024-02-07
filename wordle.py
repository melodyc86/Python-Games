
import random

def choose_word():
    word_list = ["chery", "grape", "lemon","straw", "melon", "peach", "plums", "leash"]
    return random.choice(word_list)

def get_guess():
    guess = input("Enter your guess (5 letters): ").lower()
    if len(guess) != 5:
        print("Please enter a 5-letter word.")
        return get_guess()
    return guess

def check_guess(secret_word, guess):
    if guess == secret_word:
        return True

    result = list("-----")
    for i in range(5):
        if guess[i] == secret_word[i]:
            result[i] = guess[i]

    return "".join(result)

def main():
    print("Welcome to Wordle!")
    secret_word = choose_word() 
    attempts = 6

    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        guess = get_guess()
        result = check_guess(secret_word, guess)
        
        if result == True:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break
        else:
            print("Result: " + result)
            attempts -= 1
            if attempts == 0:
                print("Out of attempts! The word was: " + secret_word)

#if __name__ == "__main__":
main()



'''
import random

def choose_word():
    word_list = ["chery", "grape", "lemon", "straw", "melon", "peach", "plums", "leash"]
    return random.choice(word_list)

def get_guess():
    guess = input("Enter your guess (5 letters): ").lower()
    if len(guess) != 5:
        print("Please enter a 5-letter word.")
        return get_guess()
    return guess

def check_guess(secret_word, guess):
    if guess == secret_word:
        return True

    result = list("-----")
    correct_positions = []

    # Find correct letters in correct positions
    for i in range(5):
        if guess[i] == secret_word[i]:
            result[i] = guess[i]
            correct_positions.append(i)

    # Find correct letters in incorrect positions
    for i in range(5):
        if i not in correct_positions and guess[i] in secret_word and i not in correct_positions:
            result[i] = "?"
    
    return "".join(result)

def main():
    print("Welcome to Wordle!")
    secret_word = choose_word()
    attempts = 6

    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        guess = get_guess()
        result = check_guess(secret_word, guess)
        
        if result == True:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break
        else:
            print("Result: " + result)
            attempts -= 1
            if attempts == 0:
                print("Out of attempts! The word was: " + secret_word)

if __name__ == "__main__":
    main()

'''
'''
import random

def choose_word():
    with open("wordlist.txt", "r") as file:
        word_list = [line.strip() for line in file.readlines()]
    return random.choice(word_list)

def get_guess():
    guess = input("Enter your guess (5 letters): ").lower()
    if len(guess) != 5:
        print("Please enter a 5-letter word.")
        return get_guess()
    return guess

def check_guess(secret_word, guess):
    if guess == secret_word:
        return True

    result = list("-----")
    correct_positions = []

    # Find correct letters in correct positions
    for i in range(5):
        if guess[i] == secret_word[i]:
            result[i] = guess[i]
            correct_positions.append(i)

    # Find correct letters in incorrect positions
    for i in range(5):
        if i not in correct_positions and guess[i] in secret_word and secret_word.index(guess[i]) not in correct_positions:
            result[correct_positions.pop(0)] = "?"
    
    return "".join(result)

def main():
    print("Welcome to Wordle!")
    secret_word = choose_word()
    attempts = 6

    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        guess = get_guess()
        result = check_guess(secret_word, guess)
        
        if result == True:
            print(f"Congratulations! You guessed the word: {secret_word}")
            break
        else:
            print("Result: " + result)
            attempts -= 1
            if attempts == 0:
                print("Out of attempts! The word was: " + secret_word)

if __name__ == "__main__":
    main()
'''

