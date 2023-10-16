class Parser:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def parse(self):
        return self.expression()

    def expression(self):
        result = self.term()
        while self.pos < len(self.text) and (self.text[self.pos] == '+' or self.text[self.pos] == '-'):
            operator = self.text[self.pos]
            self.pos += 1
            right = self.term()
            if operator == '+':
                result += right
            else:
                result -= right
        return result

    def term(self):
        result = self.factor()
        while self.pos < len(self.text) and (self.text[self.pos] == '*' or self.text[self.pos] == '/'):
            operator = self.text[self.pos]
            self.pos += 1
            right = self.factor()
            if operator == '*':
                result *= right
            else:
                result /= right
        return result

    def factor(self):
        if self.text[self.pos] == '(':
            self.pos += 1
            result = self.expression()
            if self.text[self.pos] == ')':
                self.pos += 1
            return result
        else:
            return self.number()

    def number(self):
        start = self.pos
        while self.pos < len(self.text) and self.text[self.pos].isdigit():
            self.pos += 1
        return int(self.text[start:self.pos])

# Usage
text = "3 + 5 * (7 - 2)"
parser = Parser(text)
result = parser.parse()
print(f"Result: {result}")
