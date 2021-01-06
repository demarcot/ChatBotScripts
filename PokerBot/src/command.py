import src.command_dispatch as command_dispatch


class Command:

    def __init__(self, cmd, permission, dispatch):
        self.cmd = cmd
        self.permission = permission
        self.dispatch = getattr(command_dispatch, dispatch)
        return

    def __str__(self):
        return '{ "cmd": "' + self.cmd + '", "permission": "' + self.permission + '", "dispatch": "' + self.dispatch.__name__ + '"}'

    @staticmethod
    def ConvertDictToObj(jsonObj):
        return Command(jsonObj['cmd'], jsonObj['permission'], jsonObj['dispatch'])