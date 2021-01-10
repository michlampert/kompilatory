from dataclasses import dataclass

@dataclass
class Node:
    line: str

@dataclass
class Int(Node):
    value: int

@dataclass
class Float(Node):
    value: float

@dataclass
class String(Node):
    value: str

@dataclass
class ID(Node):
    id: str

@dataclass
class Block(Node):
    instructions: list

@dataclass
class ExpressionsBlock(Node):
    expressions: list

@dataclass
class Vector(Node):
    values: list

@dataclass
class Transposition(Node):
    expression: Node

@dataclass
class Opposite(Node):
    expression: Node

@dataclass
class Reference(Node):
    id: Node
    expressions: list

@dataclass
class Function(Node):
    function: str
    argument: Node

@dataclass
class Binary(Node):
    operator: str
    left: Node
    right: Node

@dataclass
class Assign(Node):
    type: str
    id: Node
    value: Node

@dataclass
class ListAssign(Node):
    type: str
    id: ID
    index: Node
    value: Node

@dataclass
class Return(Node):
    expression: Node

@dataclass
class Print(Node):
    expression: Node

@dataclass
class Break(Node):
    pass

@dataclass
class Continue(Node):
    pass

@dataclass
class Range(Node):
    first: Node
    last: Node

@dataclass
class For(Node):
    id: ID
    range: Node
    expression: Node

@dataclass
class While(Node):
    condition: Node
    expression: Node

@dataclass
class If(Node):
    condition: Node
    true: Node
    false: Node = Block(0, [])

@dataclass
class Error(Node):
    msg: str
    
