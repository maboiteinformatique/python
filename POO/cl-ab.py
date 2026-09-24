
from abc import ABC, abstractmethod

class Question(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def check(self, a: str):
        pass

class YesNoQuestion(Question):
    def __init__(self, question: str, answer: bool):
        self.question = question
        self.answer = answer

    def print(self):
        print(f"[?] {self.question} (yes/no)")

    def check(self, reponse: str):
        return (reponse == "yes" and self.answer) or (reponse == "no" and not self.answer)    

class OpenQuestion(Question):
    def __init__(self, question: str, answers: list):
        self.question = question
        self.answers = answers
    def print(self):
        print(f"[?] {self.question}\n")
    def check(self, reponse: str):
        return reponse in self.answers

class MultiOptionsQuestion(Question):
    def __init__(self, question: str, options: list, answer_index: int):
        self.question = question
        self.options = options
        self.answer_index = answer_index

    def print(self):
        print(f"[?] {self.question}")
        for i, option in enumerate(self.options):
            print (f"[{i+1}] {option}")

    def check(self, reponse: str):
        return self.answer_index + 1 == int(reponse)

q = MultiOptionsQuestion('How many states are in the USA?',['49', '50', '51', '32'], 1)
q.print()
print(q.check("2"))