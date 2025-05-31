import sys

questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['A) Paris', 'B) London', 'C) Rome', 'D) Berlin'],
        'answer': 'A'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['A) Earth', 'B) Mars', 'C) Jupiter', 'D) Venus'],
        'answer': 'B'
    },
    {
        'question': 'Who wrote the play "Romeo and Juliet"?',
        'options': ['A) Charles Dickens', 'B) William Shakespeare', 'C) Mark Twain', 'D) Jane Austen'],
        'answer': 'B'
    },
    {
        'question': 'What is the largest ocean on Earth?',
        'options': ['A) Atlantic Ocean', 'B) Indian Ocean', 'C) Arctic Ocean', 'D) Pacific Ocean'],
        'answer': 'D'
    },
    {
        'question': 'Which element has the chemical symbol O?',
        'options': ['A) Gold', 'B) Oxygen', 'C) Silver', 'D) Iron'],
        'answer': 'B'
    }
]

def run_quiz():
    score = 0
    print("Welcome to the Quiz Game!\n")
    for idx, q in enumerate(questions, 1):
        print(f"Q{idx}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
    print(f"Quiz finished! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz() 