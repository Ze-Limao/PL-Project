class Function:
    def __init__(self, name, index, parameters, body):
        self.index = index
        self.name = name
        self.parameters = parameters # [-1] is the return
        self.code = body
