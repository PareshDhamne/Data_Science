questions = [
            ['Which of these planets does not have rings?',
            'Jupiter',
            'Saturn',
            'Neptune',
            'Venus',4],
            ['Which of these planets does not have rings?',
            'Jupiter',
            'Saturn',
            'Neptune',
            'Venus',3],
            ['Which of these planets does not have rings?',
            'Jupiter',
            'Saturn',
            'Neptune',
            'Venus',4],
            ['Which of these planets does not have rings?',
            'Jupiter',
            'Saturn',
            'Neptune',
            'Venus',4],
            ['Which of these planets does not have rings?',
            'Jupiter',
            'Saturn',
            'Neptune',
            'Venus',4],
            ['Which of these planets does not have rings?',
            'Jupiter',
            'Saturn',
            'Neptune',
            'Venus',4],
            ['Which of these planets does not have rings?',
            'Jupiter',
            'Saturn',
            'Neptune',
            'Venus',4],
            ['Which of these planets does not have rings?',
            'Jupiter',
            'Saturn',
            'Neptune',
            'Venus',4],
            ['Which of these planets does not have rings?',
            'Jupiter',
            'Saturn',
            'Neptune',
            'Venus',4],
            ['Which of these planets does not have rings?',
            'Jupiter',
            'Saturn',
            'Neptune',
            'Venus',4],
            ['Which of these planets does not have rings?',
            'Jupiter',
            'Saturn',
            'Neptune',
            'Venus',4],
            ['Which of these planets does not have rings?',
            'Jupiter',
            'Saturn',
            'Neptune',
            'Venus',4],
            ['Which of these planets does not have rings?',
            'Jupiter',
            'Saturn',
            'Neptune',
            'Venus',4],
            ['Which of these planets does not have rings?',
            'Jupiter',
            'Saturn',
            'Neptune',
            'Venus',4]
            ]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1200000,2500000,
          10000000]

money = 0
for  i in range(0,len(questions)):
    question = questions[i]
    print(f'Question for Rs. {levels[i]} is \n A. {question[0]}')
    print(f'1. {question[1]}               2. {question[2]}')
    print(f'3. {question[3]}               4. {question[4]}')
    
    ans = input(f'Enter your Answer \n (Enter ''Quit'' if you dont want to play further ) :: ')
    if ans == 'Quit' or ans == 'QUIT' or ans == 'quit':
        print(f'You won Rs. {money} \n Thank you !! \n All the Best for better future')
        break 
    elif int(ans) == question[-1]:
        money = levels[i]
        print(f"Correct Answer! You won {money}")
        
    else :
        print(f"Option {ans} is Wrong, Correct Answer is {question[-1]}")
        if levels[i] in levels[4:9]:
            money = 10000
        elif levels[i] in levels[9:14]:
            money = 320000
                
        print(f'You won Rs. {money} \n Thank you !! \n All the Best for better future')
        break   
    
