

class Command:

    def __init__(self, cmd, permission, val1, val2):
        self.cmd = cmd
        self.permission = permission
        self.val1 = val1
        self.val2 = val2
        return

    def __str__(self):
        return '{ "cmd": "' + self.cmd + '", "permission": "' + self.permission + '", "val1": "' + self.val1 + '", "val2": "' + '"}'

    @staticmethod
    def ConvertDictToObj(jsonObj):
            return Command(jsonObj['cmd'], jsonObj['permission'], jsonObj['val1'], jsonObj['val2'])