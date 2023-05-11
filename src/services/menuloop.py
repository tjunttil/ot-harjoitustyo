from services.loop import Loop
class MenuLoop(Loop):
    """A loop for handling menu events

    Args:
        Loop (Loop): the parent class of MenuLoop, handling generic loop functions
    """
    def _handle_commands(self, commands):
        commands_keys = ["start game", "start score list"]
        for key in commands_keys:
            if key not in commands.keys():
                raise KeyError("The format of the commands is not applicable to menu events")
            if commands[key]:
                return key[6:]
        return super()._handle_commands(commands)
