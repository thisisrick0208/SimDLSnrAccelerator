class Memory(object):
    def __init__(self, size):
        self.data = []
        self.size = size
        self.mutex = None   # TODO: define a mutex
        self.cond = None