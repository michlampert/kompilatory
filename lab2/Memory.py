class Memory:

    def __init__(self, name="Interpreter"): # memory name
        self.name = name
        self.memory_dict = dict()

    def has_key(self, name):  # variable name
        return name in self.memory_dict
        
    def get(self, name):         # gets from memory current value of variable <name>
        return self.memory_dict[name]
    def put(self, name, value):  # puts into memory current value of variable <name>
        self.memory_dict[name] = value

class MemoryStack:
                                                                             
    def __init__(self, memory=None): # initialize memory stack with memory <memory>
        memory_stack = [] if memory is None else [memory]
        self.memory_stack = memory_stack

    def get(self, name):             # gets from memory stack current value of variable <name>
        for memory in self.memory_stack[::-1]:
            if memory.has_key(name): return memory.get(name)
        return None

    def insert(self, name, value): # inserts into memory stack variable <name> with value <value>
        memory = self.memory_stack[-1]
        memory.put(name, value)
        
    def set(self, name, value): # sets variable <name> to value <value>
        for memory in self.memory_stack[::-1]:
            if memory.has_key(name): 
                memory.put(name, value)
                return None
        self.insert(name, value)

    def push(self, memory): # pushes memory <memory> onto the stack
        self.memory_stack.append(memory)

    def pop(self):          # pops the top memory from the stack
        return self.memory_stack.pop()