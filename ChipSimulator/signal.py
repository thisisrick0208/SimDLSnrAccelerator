class Signal(object):
    def __init__(self):
        self.data = []
        self.width = 16
        pass

    def send(self, port, data):
        pass

    def recv(self, port, data):
        pass

    def wait(self, port, exp):
        pass

    def notify(self, port, data):
        pass

    def clean(self, port, data):
        pass