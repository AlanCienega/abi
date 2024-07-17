from parser import AssignmentNode, PrintNode, RepeatNode, AddNode, SubtractNode

class Interpreter:
  def __init__(self, ast):
    self.ast = ast
    self.variables = {}

  def interpret(self):
    for node in self.ast:
      if isinstance(node, AssignmentNode):
        self.execute_assignment(node)
      elif isinstance(node, PrintNode):
        self.execute_print(node)
      elif isinstance(node, RepeatNode):
        self.execute_repeat(node)
      elif isinstance(node, AddNode):
        self.execute_add(node)
      elif isinstance(node, SubtractNode):
        self.execute_substract(node)
      else:
        raise RuntimeError(f"Unknown node type: {type(node)}")

  def execute_assignment(self, node):
    if node.value_type == "NUMBER":
      self.variables[node.variable_name] = int(node.value)
    elif node.value_type == "EMPTY":
      self.variables[node.variable_name] = []
    else:
      self.variables[node.variable_name] = node.value.strip('"')

  def execute_add(self, node):
    if node.value_type == "NUMBER":
      self.variables[node.variable_name] += int(node.value)
    elif node.value_type == "STRING":
      if isinstance(self.variables[node.variable_name], str):
        self.variables[node.variable_name] += node.value.strip('"')
      else:
        self.variables[node.variable_name].append(node.value.strip('"'))
    else:
      self.variables[node.variable_name] += int(self.variables[node.value])

  def execute_substract(self, node):
    if node.value_type == "NUMBER":
      self.variables[node.variable_name] -= int(node.value)
    elif node.value_type == "SOMETHING":
      self.variables[node.variable_name].pop()
    elif node.value_type == "STRING":
      self.variables[node.variable_name] = self.variables[node.variable_name].replace(node.value.strip('"'), '')
    else:
      self.variables[node.variable_name] -= int(self.variables[node.value])

  def execute_print(self, node):
    value = node.value
    if value in self.variables:
      print(self.variables[value])
    else:
      print(value.strip('"'))

  def execute_repeat(self, node):
    times = self.variables[node.times] if node.times in self.variables else int(node.times)
    for _ in range(times):
      if isinstance(node.statement, PrintNode):
        self.execute_print(node.statement)
      elif isinstance(node.statement, AddNode):
        self.execute_add(node.statement)
      elif isinstance(node.statement, SubtractNode):
        self.execute_substract(node.statement)
      else:
        raise RuntimeError(f"Unsupported statement in repeat: {type(node.statement)}")