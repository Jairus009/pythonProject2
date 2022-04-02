# THIS IS A PROGRAM USING WHILE LOOP WITH IF STATEMENT
LUCKY_NUMBER = 63
i = 25
PIN = '0000'
GUESS_VALUE = str()
A_COPY = int()
Chances_left_for_PIN = 7
pin = '$%$%'
while GUESS_VALUE != 'EXIT' and GUESS_VALUE != 'exit' and Chances_left_for_PIN != 0 and i != 0 and A_COPY != LUCKY_NUMBER:
    while Chances_left_for_PIN >= 1 and pin != PIN:
        pin = input('PLEASE ENTER YOUR PIN : ')
        Chances_left_for_PIN = Chances_left_for_PIN - 1
        if pin != PIN and Chances_left_for_PIN >= 1:
            print('                                                 INCORRECT PIN  ')
            print('\n YOU HAVE ', Chances_left_for_PIN, 'MORE ATTEMPTS FROM LOSING YOUR ACCOUNT ')
        elif Chances_left_for_PIN == 0 and pin != PIN:
            print('                    ====> SUSPICIOUS BEHAVIOR DETECTED\n')
            print('*** YOU CAN NOT USE THIS ACCOUNT FURTHER BEFORE OFFLINE VERIFICATION OF YOUR IDENTITY ***')
        if pin == PIN:
            print('\n                                                   AUTHENTICATION ACCEPTED')
    if Chances_left_for_PIN != 0 and pin == PIN:
        try:
            print('\n                       -=+=- Please Guess a number between 1 to 100 -=+=- ')
            GUESS_VALUE = input('Enter Here: ')
            i = i - 1
            A_COPY = int(GUESS_VALUE)
            if A_COPY < -100 or A_COPY > 100:
                print('\n                                ---<<<  INVALID NUMBER   >>>---')
            elif A_COPY >= -100 and A_COPY < 0:
                A_COPY = A_COPY * -1
                print('\n                          ///     NEGATIVES NUMBER IS TURNED POSITIVE     ///')
#                           ---- VALID NUMBER RECEIVED ----
            if A_COPY >= 1 and A_COPY <= 100:
                if A_COPY == LUCKY_NUMBER:
                    print('                     ~~~ $$$ --++ CONGRATS YOU WON ++-- $$$ ~~~')
                else:
                    if A_COPY < LUCKY_NUMBER:
                        print('\n=+>', A_COPY, 'IS A LITTLE, " small " lol.')
                    elif A_COPY > LUCKY_NUMBER:
                        print('\n=+>', A_COPY, 'IS A LITTLE, " BIG " lol.')
        except Exception:
            if i > 0 and GUESS_VALUE != 'exit' and GUESS_VALUE != "EXIT":
                print('\nINVALID INPUT.\nYou have entered ' '"', GUESS_VALUE, '"' ' Only Numbers are allowed.')
        finally:
            if i > 0 and GUESS_VALUE != 'exit' or GUESS_VALUE != 'EXIT':
                print('\nNOTE: Enter "exit" at any time to leave the Game')
                print('You have', i, 'chances more to find the Correct Number')
                print('Give Another Shot,')
    if GUESS_VALUE == 'exit' or GUESS_VALUE == 'EXIT':
        print('You have entered ' '"', GUESS_VALUE, '"')
        print('\n    +==-->  THANK YOU, WE HOPE TO SEE YOU AGAIN   <--==+')
        print('  ===>}   -=+ PROGRAM TERMINATED AT YOUR REQUEST +=-   {<===')
    elif i == 0:
        print('\nYou ran out of your chances ')
print('\n                                                         THANK YOU FOR PLAYING :-) ', end='')
