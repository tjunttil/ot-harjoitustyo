from services.loop import Loop
class MenuLoop(Loop):
    def _handle_commands(self, commands):
        if commands["start game"]:
            return "game"
        return super()._handle_commands(commands)
