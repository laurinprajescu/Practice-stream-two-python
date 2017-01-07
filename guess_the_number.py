import random

NUMBER_OF_GUESSES_FROM_USER = 10
RANGE_TOP = 10

while True:
    # generate the random number
    random_number = random.randint(0, RANGE_TOP)

    # give the user a certain amount of guesses
    for i in range(NUMBER_OF_GUESSES_FROM_USER):
        guess = int(raw_input('guess the number: '))

        # counts the number of guesses left
        guesses_left = NUMBER_OF_GUESSES_FROM_USER - i

        if guess == random_number:
            print 'well done'
            break
        elif guess > random_number:
            print "too high"
            print "Guesses left: " + str(guesses_left)
        else:
            print "too low"
            print "Guesses left: " + str(guesses_left)

    print "let's try a new number ! "

    print "Your number should be in range: " + str(RANGE_TOP)