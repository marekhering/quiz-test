import os.path
import time
from random import shuffle


QUIZ_FILENAME = 'szum-2022.txt'


def create_token(offset: int):
    return chr(ord("A") + offset)


def load_questions(filename: str, number_of_answers: int):
    _questions = []
    with open(filename, "r", encoding="utf8") as f:
        for _text in f:
            _answers = [f"{create_token(i)}) {f.readline().strip()}" for i in range(number_of_answers)]
            _correct_answers = f.readline().strip()
            _questions.append([_text.strip(), *_answers, _correct_answers])
    shuffle(_questions)
    return _questions


if __name__ == '__main__':
    test_questions = load_questions(os.path.join('data', QUIZ_FILENAME), 4)
    for question, *answers, correct_answer in test_questions:
        print("".join(["-"] * 50))
        print(question)
        print("\n".join(answers))
        user_answer = input()
        if correct_answer.replace(" ", "").upper() == user_answer.replace(" ", "").upper():
            print("Correct!")
        else:
            print(f"Wrong! Correct answer is: {correct_answer}")
            test_questions.append([question, *answers, correct_answer])
        time.sleep(1)
