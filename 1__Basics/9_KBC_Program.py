# Kob Banega Karodpati Program
# NOTE User won some amount based on right answers

questions = [
    ["Who is PM of India", "Modi" , "Pukin" , "Trump" , "Jay Shah" , 1],
    ["Who is PM of USA", "Modi" , "Pukin" , "Trump" , "Jay Shah" , 3],
    ["Who is PM of Russia", "Modi" , "Pukin" , "Trump" , "Jay Shah" , 2],
    ["Who is Secretory of BCCI", "Modi" , "Pukin" , "Trump" , "Jay Shah" , 4]
]

money_BasedOn_Level = [5000,15000,25000,35000]

for i in range (0,len(questions)):

    # Show Questions & it's Options
    print(f"\n\n{questions[i][0]}")
    print(f"1. {questions[i][1]}  ,  2. {questions[i][2]}")
    print(f"3. {questions[i][3]}  ,  4. {questions[i][4]}")

    # Give User input for select option
    select_option = int(input('Select options from 1 to 4 :- '))

    # Based on answer defined result & Give Reward
    if(select_option == questions[i][-1]):
        print(f"Answer is Correct. \nYou won Rs. {money_BasedOn_Level[i]}")
    else:
        print(f"WRONG ANSWER")
        break
