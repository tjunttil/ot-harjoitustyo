import unittest
from services.menuloop import MenuLoop
from tests.loop_test import StubRenderer, StubEventHandler, StubClock

class TestMenuLoop(unittest.TestCase):
    def setUp(self):
        self.menuloop = MenuLoop(StubRenderer(), StubEventHandler(), StubClock())
        self.commands1 = {"start game": False, "start score list": False}
        self.commands2 = {"start game": True, "start score list": False}
        self.commands3 = {"start game": False, "start score list": True}
        self.commands4 = {"start game": True, "start score list": True}
        for commands in [self.commands1, self.commands2, self.commands3, self.commands4]:
            commands["quit"] = False

    def test_handle_commands_throws_exception_if_commands_fields_wrong(self):
        self.assertRaises(KeyError, self.menuloop._handle_commands, {"banana":"yes"})

    def test_handle_commands_returns_the_correct_view(self):
        self.assertEqual(self.menuloop._handle_commands(self.commands3), "score list")
        self.assertEqual(self.menuloop._handle_commands(self.commands2), "game")

    def test_handle_commands_returns_true_when_commands_false(self):
        self.assertEqual(self.menuloop._handle_commands(self.commands1), True)
