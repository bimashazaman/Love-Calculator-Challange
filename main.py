print("Welcome to the Love Calculator!")

your_name = input("What is your name? \n")
their_name = input("What is their name? \n")

combined_string = your_name + their_name
lowar_case_string = combined_string.lower()

t = lowar_case_string.count('t')
r = lowar_case_string.count('r')
u = lowar_case_string.count('u')
e = lowar_case_string.count('e')

true = t + r + u + e

l = lowar_case_string.count('l')
o = lowar_case_string.count('o')
v = lowar_case_string.count('v')
e = lowar_case_string.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love)) 

if (love_score < 10) or (love_score > 90):
    print(f'your love score is {love_score}, you go together like coke and mentos!!!!')
elif (love_score >=  40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.") 
else:
    print(f"your love score is {love_score}!")        
    











