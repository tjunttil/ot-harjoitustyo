import unittest
from services.loop import Loop

class StubRenderer:
    def draw(self):
        pass

class StubEventHandler:
    def handle_event(self, event):
        pass

    def handle_events(self):
        pass

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
        