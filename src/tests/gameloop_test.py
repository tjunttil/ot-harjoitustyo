import unittest
from services.gameloop import GameLoop
from services.space import Space
from services.collision_handler import CollisionHandler
from services.group_handler import GroupHandler
from services.coordinate_system import CoordinateSystem
from tests.loop_test import StubRenderer, StubEventHandler, StubClock

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.space = Space(GroupHandler(), CollisionHandler(), CoordinateSystem(640,480))
        self.gameloop = GameLoop(StubRenderer(), self.space,
        StubEventHandler(), StubClock())

    def test_handle_commands_returns_false_when_quitting(self):
        commands = []
        truth_values = [True, False]
        for value in truth_values:
            commands.append({"quit": True, "move": False, "fire": value})
        results = list(map(self.gameloop._handle_commands, commands))
        self.assertEqual(results, [False, False])

    def test_handle_commands_returns_true_when_not_quitting(self):
        commands = []
        truth_values = [True, False]
        for value in truth_values:
            commands.append({"quit": False, "move": False, "fire": value})
        results = list(map(self.gameloop._handle_commands, commands))
        self.assertEqual(results, [True, True])

    def test_handle_commands_changes_ship_velocity_and_returns_true_if_commanded(self):
        commands = {"quit": False, "move": ((1,0),5), "fire": False}
        result = self.gameloop._handle_commands(commands)
        new_velocity = self.gameloop._GameLoop__space.ship.velocity
        self.assertEqual((new_velocity, result),(5,True))
