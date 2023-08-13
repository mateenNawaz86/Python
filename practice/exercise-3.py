# Write a code for performing KBC!!!

# Here we write all the questions
questions = [
    {
        "question": "What is capital of United Kingdom?", "answer": "London"
    },
    {
        "question": "What is the most beautiful place on earth?", "answer": "Switzerland"
    },
    {
        "question": "What is the most delicious food of Pakistan?", "answer": "Saag"
    },
    {
        "question": "Which language of computer is most used on frontend side?", "answer": "JavaScript"
    },
]


# here we can define the function for create question randomly
import random

def random_question():
    
    # Here we store the total_reward 
    total_reward = 0
    
    # Here we check that whether the answer is correct or wrong
    while True:
        random_questions = random.choice(questions)
        question_text = random_questions['question']
        correct_answer = random_questions['answer']
        
        # Here we input the answer from user
        user_answer = input(f"Question is: {question_text}\nType your answer here: ")
        
        if user_answer.lower() == correct_answer.lower():
            print("Correct! Your answer is correct.")
            total_reward += 100
            print("Your total Reward: ", total_reward)
        
        else:
            print("Wrong! Best of luck for the next time.")
            print("Your total Reward: ", total_reward)
            break
            

# Loop for play the game
while True:
    random_question()
    play_again = input("Do you want to play again? (yes/No): ")
    
    if play_again.lower != 'yes':
        print("Thank You for playing the game!")
        break