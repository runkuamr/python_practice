print("Wellcome to ABC Technologies quiz ")
print('NOTE: if your spelling is incorrect then it is considered as wrong answer')
score = 0
question_no = 0
playing = input('Do you want to play ? ').lower()
if playing == 'yes':
    question_no += 1
    ques = input(f'\n{question_no}. one plus one ? ').lower()
    if ques == 'two':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> two')

# ------1
    question_no += 1
    ques = input(f'\n{question_no}. who is the prime minister of india? ').lower()
    
    if ques == 'narendra modi':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is -->narendra modi ')

# -----2
    question_no += 1
    ques = input(f'\n{question_no}. who is cm of tamilnadu? ').lower()
    
    if ques == 'm.k.stalin':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> m.k.stalin')

# -----3
    question_no += 1
    ques = input(f'\n{question_no}. which country host g20 2023? ').lower()
    
    if ques == 'india':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> india')


# -----4
    question_no += 1
    ques = input(f'\n{question_no}. total number of TN MLA? ').lower()
    
    if ques == '234':
        score +=1
        print('correct! you got 1 point')
        
    else:
        print('Incorrect!')
        print(f'current answer is --> 234')


# ------5 

else:
    print('thankyou you are out of a game.')
    quit()

print(f'\nnumber of question is {question_no}')
print(f'your score is {score}')
try:
    percentage = (score *100)/question_no
except ZeroDivisionError:
    print('0% quetions are correct')

print(f'{percentage}% questions are correct.')