

class Command:

    def __init__(self, cmd, val1, val2):
        self.cmd = cmd
        self.val1 = val1
        self.val2 = val2
        return

    def __str__(self):
        return '{ "cmd": "' + self.cmd + '", "val1": "' + self.val1 + '", "val2": "' + '"}'

    @staticmethod
    def ConvertDictToObj(jsonObj):
            return Command(jsonObj['cmd'], jsonObj['val1'], jsonObj['val2'])