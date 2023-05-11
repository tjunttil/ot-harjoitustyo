import unittest
from services.menuloop import MenuLoop
from tests.loop_test import StubRenderer, StubEventHandler, StubClock, pad_to_n

class TestMenuLoop(unittest.TestCase):
    def setUp(self):
        self.menuloop = MenuLoop(StubRenderer(), StubEventHandler(), StubClock())
        self.commands = self.__initialise_commands()
        self.non_quitting_commands = list(filter(
            lambda x: not x["quit"] and not x["return to menu"],self.commands))

    def __initialise_commands(self):
        keys = ["return to menu", "quit", "start game", "start score list"]
        commands = []
        for i  in range(16):
            command = {}
            truth_values = pad_to_n(bin(i)[2:], 4)
            for index, value in enumerate(truth_values):
                command[keys[index]] = value == "1"
            commands.append(command)
        return commands

    def test_handle_commands_throws_exception_if_commands_fields_wrong(self):
        self.assertRaises(KeyError, self.menuloop._handle_commands, {"banana":"yes"})

    def test_handle_commands_returns_the_correct_view(self):
        for commands in self.non_quitting_commands:
            if commands["start game"]:
                self.assertEqual(self.menuloop._handle_commands(commands), "game")
            elif commands["start score list"]:
                self.assertEqual(self.menuloop._handle_commands(commands), "score list")

    def test_handle_commands_returns_true_when_commands_false(self):
        false_commands = list(filter(
            lambda x: list(x.values()) == [False,False,False,False],self.commands))[0]
        self.assertEqual(self.menuloop._handle_commands(false_commands), True)
