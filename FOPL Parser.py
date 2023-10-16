import re

class FOLParser:
    def __init__(self):
        self.variables = set()

    def parse(self, expression):
        # Tokenize the expression
        tokens = re.findall(r"\(|\)|NOT|AND|OR|[A-Z]", expression)

        # Remove whitespace
        tokens = [token for token in tokens if not token.isspace()]

        # Initialize the index
        self.index = 0

        # Parse the expression
        result = self.parse_expression(tokens)

        # Check for leftover tokens
        if self.index != len(tokens):
            raise SyntaxError("Invalid expression")

        return result

    def parse_expression(self, tokens):
        stack = []

        while self.index < len(tokens):
            token = tokens[self.index]

            if token == "(":
                self.index += 1
                subexpression = self.parse_expression(tokens)
                stack.append(subexpression)
            elif token == ")":
                self.index += 1
                break
            elif token == "AND":
                self.index += 1
                if not stack:
                    raise SyntaxError("Invalid expression")
                left = stack.pop()
                right = self.parse_expression(tokens)
                stack.append(("AND", left, right))
            elif token == "OR":
                self.index += 1
                if not stack:
                    raise SyntaxError("Invalid expression")
                left = stack.pop()
                right = self.parse_expression(tokens)
                stack.append(("OR", left, right))
            elif token == "NOT":
                self.index += 1
                if not stack:
                    raise SyntaxError("Invalid expression")
                operand = self.parse_expression(tokens)
                stack.append(("NOT", operand))
            else:
                self.index += 1
                stack.append(token)
                self.variables.add(token)

        if not stack:
            raise SyntaxError("Invalid expression")

        while len(stack) > 1:
            operator = stack.pop()
            if operator in {"AND", "OR"}:
                left = stack.pop()
                right = stack.pop()
                stack.append((operator, left, right))
            elif operator == "NOT":
                operand = stack.pop()
                stack.append(("NOT", operand))

        return stack[0]

    def evaluate(self, model):
        return self.evaluate_expression(model, self.parse_expression)

    def evaluate_expression(self, model, expression):
        if isinstance(expression, tuple):
            if expression[0] == "AND":
                left = self.evaluate_expression(model, expression[1])
                right = self.evaluate_expression(model, expression[2])
                return left and right
            elif expression[0] == "OR":
                left = self.evaluate_expression(model, expression[1])
                right = self.evaluate_expression(model, expression[2])
                return left or right
            elif expression[0] == "NOT":
                operand = self.evaluate_expression(model, expression[1])
                return not operand
        else:
            return model.get(expression, False)

# Example usage
parser = FOLParser()
expression = "(P AND Q) OR (NOT R)"
model = {"P": True, "Q": False, "R": True}

result = parser.evaluate(model)
print(f"Result: {result}")
