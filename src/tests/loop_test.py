import unittest
from services.loop import Loop

events = ["banana", "apple", "quitting"]

class StubRenderer:
    def draw(self):
        pass

class StubEventHandler:
    def handle_event(self, event):
        commands = {"banana": "yes", "apple": "no", "quit": False}
        if event != "quitting":
            commands[event] = event
        else:
            commands["quit"] =  True
        return commands

    def handle_events(self):
        commands = []
        for event in events:
            commands.append(self.handle_event(event))
        return commands

class StubClock:
    def tick(self, amount):
        pass

class TestLoop(unittest.TestCase):
    def setUp(self):
        self.loop = Loop(StubRenderer(), StubEventHandler(), StubClock())

    def test_handle_commands_returns_the_opposite_of_quit(self):
        commands = [{"quit": True}, {"quit": False}]
        for command in commands:
            self.assertEqual(self.loop._handle_commands(command), not command["quit"])

    def test_start_returns_list(self):
        return_value = self.loop.start()
        self.assertEqual(type(return_value), list)
