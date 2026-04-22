words = {"pair": 4, "hair": 4, "chair": 5}
score = 0

print("Welcome to word guessing game !")
print("Guess word from this letters : \"A, I, F, G, R, P, H\"")

while(len(words)>0):
    print(f"{len(words)} words left.")
    guess = input("Enter a guess: ")
    
    if guess.lower() in words.keys():
        print("Right !")
        score += words[guess.lower()]
        del words[guess.lower()]
    else:
        print("try again !")
    print(f"Score: {score}")
        
print("Complete.")