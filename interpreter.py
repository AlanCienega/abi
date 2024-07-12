from parser import AssignmentNode, PrintNode, RepeatNode

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
      else:
        raise RuntimeError(f"Unknown node type: {type(node)}")

  def execute_assignment(self, node):
    self.variables[node.variable_name] = node.value

  def execute_print(self, node):
    value = node.value
    if value in self.variables:
      print(self.variables[value])
    else:
      print(value.strip('"'))

  def execute_repeat(self, node):
    for _ in range(node.times):
      if isinstance(node.statement, PrintNode):
        self.execute_print(node.statement)
      else:
        raise RuntimeError(f"Unsupported statement in repeat: {type(node.statement)}")