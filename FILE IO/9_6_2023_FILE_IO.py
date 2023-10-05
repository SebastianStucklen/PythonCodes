import random

myfile = open("FILE IO\scores.txt", "r")
print("Current scores in the file:")
myfile.read()




guesses = 0
correct = False
min1 = random.randint(-50,0)
max2 = random.randint(0,100)
answer = random.randint(min1,max2)
int(answer)
while correct == False:
    while True:
        userAnswer = int(input(f"Guess a number between {min1} and {max2}     "))
        try:
            int(userAnswer)
            break
        except ValueError:
            print("thats not a number dummy")
        
    if userAnswer < answer:
        print("Wrong!!!!!!! Too low!")
        guesses +=1
    if userAnswer > answer:
        print("Wrong!!! TOO HIGH!")
        guesses +=1
    if userAnswer == answer:
        guesses+=1
        print("DING DING DING!!! YOURE CORRECT")
        print(f"it took you {guesses} guesses to get the right answer")
        name = str(input("whats your name"))
        score = f"{guesses}, {name}"
        str(score)
        myfile.write(score)
        list1 = list(myfile)
        myfile.close()
        list1.sort()
        print(list1)
        correct = True
print(f"Right Answer: {answer}")
