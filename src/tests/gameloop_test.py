import unittest
from services.gameloop import GameLoop
from services.space import Space
from services.collision_handler import CollisionHandler
from services.group_handler import GroupHandler
from services.coordinate_system import CoordinateSystem
from tests.loop_test import StubRenderer, StubEventHandler, StubClock

class FakeSpace:
    def __init__(self, group_handler, collision_handler, coordinate_system):
        self.group_handler = group_handler
        self.collision_handler = collision_handler
        self.coordinate_system = coordinate_system

    def change_ship_velocity(self, *args):
        pass

    def fire_ship_cannon(self):
        pass

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.fake_space = FakeSpace(GroupHandler(), CollisionHandler(), CoordinateSystem(640,480))
        self.space = Space(GroupHandler(), CollisionHandler(), CoordinateSystem(640,480))
        self.fakespace_gameloop = GameLoop(StubRenderer(), self.fake_space,
        StubEventHandler(), StubClock())
        self.gameloop = GameLoop(StubRenderer(), self.space,
        StubEventHandler(), StubClock())

    def test_handle_commands_returns_false_when_quitting(self):
        commands = []
        truth_values = [True, False]
        for value in truth_values:
            commands.append({"quit": True, "move": False, "return to menu": False, "fire": value})
        results = list(map(self.gameloop._handle_commands, commands))
        self.assertEqual(results, [False, False])

    def test_handle_commands_returns_true_when_not_quitting(self):
        commands = []
        truth_values = [True, False]
        for value in truth_values:
            commands.append({"quit": False, "move": ((value, not value, value)), "fire": value, "return to menu": False})
        results = list(map(self.fakespace_gameloop._handle_commands, commands))
        self.assertEqual(results, [True, True])

    def test_handle_commands_changes_ship_velocity_and_returns_true_if_commanded(self):
        commands = {"quit": False, "move": ((1,0),5), "fire": False, "return to menu": False}
        result = self.gameloop._handle_commands(commands)
        new_velocity = self.gameloop._GameLoop__space.ship.velocity
        self.assertEqual((new_velocity, result),(5,True))
