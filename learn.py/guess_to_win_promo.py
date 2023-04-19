import random

play = input('enter "y" to play or "q" to quit  the game: ')
gamer_choice = ['y', 'q']
for c in gamer_choice:
    if play == 'q':
        print('bye bye')
        break
    
    else:
        start = input('please enter the start of the range: ')
        while not start.isdigit():
            print('please enter a valid number')
            start = input('please enter the start of the range: ')

        end = input('please enter the end of the range: ')
        while not end.isdigit() or int(start) > int(end):
            print('please enter a valid number')
            end = input('please enter the end of the range: ')


    random_number = random.randint(int(start), int(end))
    guess = None
    attempts = 0
    while guess != random_number:
        guessed_number = input('Guess a number: ')
        if not guessed_number.isdigit():
            print('Enter a valid number')
            continue

        attempts += 1
        guess = int(guessed_number)


    suffix = ''
    if attempts > 1:
        suffix = "s" 

    message = { 1:'SUNDAY', 2:'MONDAY',3:'TUESDAY', 4:'WEDNESDAY', 5:'THURSDAY', 6:'FRIDAY',7:'SATURDAY'}
    promotion_giftS = ['BMW', 'KIA', 'TELEVISION', 'BLENDER', 'RICE_COKER', 'HOUSE', 'WATCH']
    guess_day = message[guess] 
    gift = promotion_giftS[guess]       
    print(f'You were born on "{guess_day}", you got it in {attempts} attempt{suffix}!')
    print(f'The promotional gift associated with your day born is a "{gift}"!')
    
    question = '''  Now enter "okay" if you cool with the promotional gift or enter "try again" to 
    to win a different gift'''
    print(question)
    break



choice = None    
while choice != 'okay' or choice != 'try again':
    another_chance = input('Please enter "okay" or "try again": ').lower()
    if another_chance.isdigit():
        print('enter a valid key')
 
    elif another_chance == 'okay':
        print('congratulation')
        break
    
    elif another_chance == 'try again':
        print('okay get ready to try again!')
    
    else:
        print('please choose "okay" or "try again"')
        

    choice = another_chance
    random_number = random.randint(int(start), int(end))
    guess = None
    second_attempt = 0
    while guess != random_number:
        guessed_number = input('Guess a number: ')
        if not guessed_number.isdigit():
            print('Enter a valid number')
            continue
        
        second_attempt += 1
        guess = int(guessed_number)
        suffix = ''
        if second_attempt > 1:
            suffix = "s" 
        
        message = { 1:'SUNDAY', 2:'MONDAY',3:'TUESDAY', 4:'WEDNESDAY', 5:'THURSDAY', 6:'FRIDAY',7:'SATURDAY'}
        promotion_giftS = ['BMW', 'KIA', 'TELEVISION', 'BLENDER', 'RICE_COKER', 'HOUSE', 'WATCH']
        guess_day = message[guess] 
        gift = promotion_giftS[guess]       
        print(f'Your born day on second attempt is "{guess_day}", you got it in {second_attempt} attempt{suffix}!')
        print(f'The promotional gift associated with your day born is a "{gift}"!')
        break
    break 

    
print('SEE YOU SOME OTHER TIME!!!!!!!!!!!!!!!!')

   
