class Module:
    def __init__(self, name, type_module, outputs):
        self.name = name
        self.type = type_module
        self.outputs = outputs
        self.outgoing = "low"
        
        if type_module == "%":
            self.memory = "off"
        else:
            self.memory = {}

    def __repr__(self):
        return f"{self.name} [type={self.type}, outputs=({','.join(self.outputs)}),memory={str(self.memory)}]"
    
    def switchMemory(self):
        if self.type != "%": return
        if self.memory == "off":
            self.memory = "on"
            self.outgoing = "high"
        else:
            self.memory = "off"
            self.outgoing = "low"
    
    def updateMemory(self, origin, pulse):
        self.memory[origin] = pulse
        self.outgoing = "low" if all(x == "high" for x in self.memory.values()) else "high"