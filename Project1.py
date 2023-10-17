# Project1.py
# Author: Nate Harris

def welcome():
    print("*************************************************************")
    print("\n               Welcome to Quizzo!            \n")
    print("You will be asked a series of multiple choice questions.")
    print("Answers are either A, B, C, or D.")
    print("You will get 1 point for each correct letter you choose!\n")
    print("           May the force be with you!        \n")
    print("*************************************************************")

def ready():
    ready = input("Are you ready to play? (y/n): ")
    if ready == "y" or ready == "Y":
        print("OK Let's Play! \n")
    else:
        print("Have a good day!")
        exit()

def ask_question(question: str, option_1: str, option_2: str, option_3: str, option_4: str, correct_answer: str) -> bool:
    print(question)
    print(option_1)
    print(option_2)
    print(option_3)
    print(option_4)
    answer = input("Answer: ")

    for i in range(0, 5):
        if answer == correct_answer:
            print("That is correct! \n")
            return True
        elif answer in ["a", "b", "c", "d"]:
            print("Sorry, the correct answer is " + correct_answer + " \n")
            return False
        else:
            print("\n Choices are a, b, c, or d. Please try again.\n")
            print(question)
            answer = input("Answer: ")


def main():

    score = 0

    welcome()
    ready()
    if ready:
        questions =[
         {
             "question": "What is the capital of California?",
             "option_1": "A. Sacramento", "option_2": "B. Los Angeles", "option_3": "C. San Francisco", "option_4": "D. San Diego",
             "correct_answer": "a"
         },
         {
             "question": "Who played Batman in the Dark Knight?",
             "option_1": "A. Robert Pattinson", "option_2": "B. Ben Affleck", "option_3": "C. Christian Bale", "option_4": "D. Jim Carey",
             "correct_answer": "c"
         },
         {
             "question": "What planet is knows as the red planet?",
                "option_1": "A. Jupiter", "option_2": "B. Mars", "option_3": "C. Saturn", "option_4": "D. Venus",
                "correct_answer": "b"
         },
         {
             "question": "What is the largest ocean?",
                "option_1": "A. Atlantic", "option_2": "B. Indian", "option_3": "C. Pacific", "option_4": "D. Arctic",
                "correct_answer": "c"
         },
         {
             "question": "How many continents are there?",
                "option_1": "A. 5", "option_2": "B. 6", "option_3": "C. 8", "option_4": "D. 7",
                "correct_answer": "d"
         }
    ]
        
    for question in questions:
        if ask_question(question ["question"], question ["option_1"], question ["option_2"], question ["option_3"], question ["option_4"], question ["correct_answer"]):
            score +=1
        else:
            score +=0
    print("Your score is " + str(score) + " out of 5!")
    print("Thanks for playing! \n")
    exit()

if __name__ == "__main__":
    main()