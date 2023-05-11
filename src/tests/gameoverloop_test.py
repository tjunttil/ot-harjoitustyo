import unittest
from services.gameoverloop import GameOverLoop
from services.space import Space
from services.collision_handler import CollisionHandler
from services.group_handler import GroupHandler
from services.coordinate_system import CoordinateSystem
from repositories.point_repository import PointRepository
from tests.loop_test import StubRenderer, StubEventHandler, StubClock

class TestGameOverLoop(unittest.TestCase):
    def setUp(self):
        self.space = Space(GroupHandler(), CollisionHandler(), CoordinateSystem(640,480))
        self.points = 5
        self.point_repository = PointRepository()
        self.gameoverloop = GameOverLoop(StubRenderer(), StubEventHandler(),
        StubClock(), self.points, self.space, self.point_repository)
        self.basic_commands = {"quit": False, "return to menu": False,
        "input": 'c', "save": False, "delete": False} 
        self.gameoverloop._handle_commands(self.basic_commands)

    def test_handle_commands_adds_character_if_command_is_input(self):
        self.assertEqual(self.gameoverloop.username, "c")

    def test_handle_commands_deletes_character_if_command_is_delete(self):
        delete = {"quit": False, "return to menu": False,
        "input": False, "save": False, "delete": True} 
        self.gameoverloop._handle_commands(delete)
        self.assertEqual(self.gameoverloop.username, "")

    def test_handle_commands_saves_non_empty_username_and_points(self):
        save = {"quit": False, "return to menu": False,
        "input": False, "save": True, "delete": False} 
        self.gameoverloop._handle_commands(save)
        entry = (self.point_repository.points_list())[0]
        self.assertEqual((entry[0], entry[1]),("c", 5))
