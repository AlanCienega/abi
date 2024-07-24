class ASTNode:
    pass

class AssignmentNode(ASTNode):
    def __init__(self, variable_name, value, value_type):
        self.variable_name = variable_name
        self.value = value
        self.value_type = value_type

    def __repr__(self):
        return f"AssignmentNode(variable_name={self.variable_name}, value={self.value}, type={self.value_type})"

class PrintNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"PrintNode(value={self.value})"

class AddNode(ASTNode):
    def __init__(self, variable_name, value, value_type):
        self.variable_name = variable_name
        self.value = value
        self.value_type = value_type

    def __repr__(self):
        return f"AddNode(variable_name={self.variable_name}, value={self.value}, type={self.value_type})"

class SubtractNode(ASTNode):
    def __init__(self, variable_name, value, value_type):
        self.variable_name = variable_name
        self.value = value
        self.value_type = value_type

    def __repr__(self):
        return f"SubtractNode(variable_name={self.variable_name}, value={self.value}, type={self.value_type})"

class RepeatNode(ASTNode):
    def __init__(self, statement, times):
        self.statement = statement
        self.times = times

    def __repr__(self):
        return f"RepeatNode(statement={self.statement}, times={self.times})"

class IfNode(ASTNode):
    def __init__(self, condition, true_branch, false_branch=None):
        self.condition = condition
        self.true_branch = true_branch
        self.false_branch = false_branch

    def __repr__(self):
        return f"IfNode(condition={self.condition}, true_branch={self.true_branch}, false_branch={self.false_branch})"

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

        if token[0] == 'TO':
            return self.parse_assignment_or_operation()
        elif token[0] == 'PRINT':
            return self.parse_print()
        elif token[0] == 'REPEAT':
            return self.parse_repeat()
        elif token[0] == 'IF':
            return self.parse_if()
        elif token[0] in ['NEWLINE', 'COMMENT']:
            self.pos += 1
            return None
        else:
            raise SyntaxError(f"Sentencia no soportada: {token}")

    def parse_assignment_or_operation(self):
        self.consume('TO')
        variable_name = self.consume('VAR')
        operation_token = self.tokens[self.pos][0]
        if operation_token == 'ASSIGN':
            return self.parse_assignment(variable_name)
        elif operation_token == 'ADD':
            return self.parse_addition(variable_name)
        elif operation_token == 'SUB':
            return self.parse_subtraction(variable_name)
        else:
            raise SyntaxError(f"Operación no soportada: {operation_token}")

    def parse_assignment(self, variable_name):
        self.consume('ASSIGN')
        value = self.consume_value()
        return AssignmentNode(variable_name[1], value[1], value_type=value[0])

    def parse_addition(self, variable_name):
        self.consume('ADD')
        value = self.consume_value()
        return AddNode(variable_name[1], value[1], value_type=value[0])

    def parse_subtraction(self, variable_name):
        self.consume('SUB')
        value = self.consume_value()
        return SubtractNode(variable_name[1], value[1], value_type=value[0])
    
    def parse_print(self):
        self.consume('PRINT')
        value = self.consume_value()
        return PrintNode(value[1])

    def consume_value(self):
        token = self.tokens[self.pos]
        if token[0] in ['NUMBER', 'STRING', 'EMPTY', 'SOMETHING', 'VAR', 'TRUE', 'FALSE']:
            self.pos += 1
            return token
        else:
            raise SyntaxError(f"Esperaba un valor pero se encontró {token}")

    def parse_repeat(self):
        self.consume('REPEAT')
        statement = self.parse_statement()
        times = self.consume_value()
        self.consume('TIMES')
        return RepeatNode(statement, times[1])

    def parse_if(self):
        self.consume('IF')
        condition = self.parse_condition()
        self.consume('THEN')
        true_branch = self.parse_statement()

        false_branch = None
        if self.pos < len(self.tokens) and self.tokens[self.pos][0] == 'IF' and self.tokens[self.pos + 1][0] == 'NO':
            self.consume('IF')
            self.consume('NO')
            false_branch = self.parse_statement()

        return IfNode(condition, true_branch, false_branch)

    def parse_condition(self):
        left = self.consume('VAR')
        self.consume('IS')
        right = self.consume_value()
        return (left, right)

    def consume(self, token_type):
        token = self.tokens[self.pos]
        if token[0] == token_type:
            self.pos += 1
            return token
        else:
            raise SyntaxError(f"Esperaba un token {token_type} pero se encontró {token}")
