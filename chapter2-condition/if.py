__author__ = 'lch'
number = 23
guess = int(raw_input('Enter an integer : '))
if guess == number:
    print 'Congratulations, you guessed it.' # New block starts here
    print "(but you do not win any prizes!)" # New block ends here
elif guess < number:
    print 'No, it is a little higher than that' # Another block
else:
    print 'No, it is a little lower than that'

print 'Done'