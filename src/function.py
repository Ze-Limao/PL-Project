class Function:
    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters # [-1] is the return
        self.code = body
