try:
    number = int(input("Type a number between 1 and 100: "))
    guessing_number= 50

    min_number=1
    max_number=100
    easy_guess= number == min_number or number == max_number or number == guessing_number
    number_of_guesses= 0

    if number > max_number or number < min_number:
            print("Number out of range. Type between 1 and 100!")

    else:
        while guessing_number != number:
            number_of_guesses += 1
            if easy_guess: break
            if number > guessing_number:
                print(f"AI guess {guessing_number}.Number is higher")
                min_number = guessing_number
                guessing_number= round((max_number+min_number)/2)
            elif number < guessing_number:
                print(f"AI guess {guessing_number}.Number is lower")
                max_number = guessing_number
                guessing_number= round((min_number+max_number)/2)
            print(f"AI guess your number {guessing_number} in {number_of_guesses} tries")

except ValueError:
    print("Type a number between 1 and 100!")

