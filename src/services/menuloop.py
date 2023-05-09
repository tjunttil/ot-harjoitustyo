from services.loop import Loop
class MenuLoop(Loop):
    def _handle_commands(self, commands):
        if commands["start game"]:
            return "game"
        if commands["start score list"]:
            return "score list"
        return super()._handle_commands(commands)
