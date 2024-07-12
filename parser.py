class ASTNode:
    pass

class AssignmentNode(ASTNode):
    def __init__(self, variable_name, value):
        self.variable_name = variable_name
        self.value = value

    def __repr__(self):
        return f"AssignmentNode(variable_name={self.variable_name}, value={self.value})"

class PrintNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"PrintNode(value={self.value})"

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        nodes = []
        while self.pos < len(self.tokens):
            node = self.parse_statement()
            if node:
                nodes.append(node)
        return nodes

    def parse_statement(self):
        token = self.tokens[self.pos]

        if token[0] == 'A':
            return self.parse_assignment()
        elif token[0] == 'PRINT':
            return self.parse_print()
        elif token[0] in ['NEWLINE', 'COMMENT']:
            self.pos += 1
            return None
        else:
            raise SyntaxError(f"Unexpected token: {token}")

    def parse_assignment(self):
        self.consume('A')
        variable_name = self.consume('VAR')
        self.consume('ASSIGN')
        value = self.consume_value()
        return AssignmentNode(variable_name[1], value[1])

    def parse_print(self):
        self.consume('PRINT')
        value = self.consume_value()
        return PrintNode(value[1])

    def consume_value(self):
        token = self.tokens[self.pos]
        if token[0] in ['NUMBER', 'STRING', 'VAR']:
            self.pos += 1
            return token
        else:
            raise SyntaxError(f"Expected NUMBER or STRING but got {token}")

    def consume(self, token_type):
        token = self.tokens[self.pos]
        if token[0] == token_type:
            self.pos += 1
            return token
        else:
            raise SyntaxError(f"Expected token {token_type} but got {token}")
