class Tokenizer:
    def get(self):
        s = input()


class Calculator:
    def brackets(self, tokenizer):
        ...

    def multiplication(self, tokenizer):
        ...

    def addition(self, tokenizer):
        ...

    def calc(self, tokenizer):
        ...

def main():
    while True:
        Calculator.calc(Tokenizer.get())
