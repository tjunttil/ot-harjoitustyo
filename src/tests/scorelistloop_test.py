import unittest
from services.scorelistloop import ScoreListLoop
from repositories.point_repository import PointRepository
from tests.loop_test import StubRenderer, StubEventHandler, StubClock, pad_to_n

class TestScoreListLoop(unittest.TestCase):
    def setUp(self):
        self.point_repository = PointRepository()
        self.scorelistloop = ScoreListLoop(StubRenderer(), self.point_repository,
        StubEventHandler(), StubClock())
        self.timeframes = ["week", "month", "all time"]
        self.commands = self.__initialise_commands()
        self.non_quitting_commands = list(filter(
            lambda x: not x["quit"] and not x["return to menu"],self.commands))

    def __initialise_commands(self):
        keys = ["return to menu", "quit", "last week", "last month", "all time"]
        commands = []
        for i  in range(32):
            command = {}
            truth_values = pad_to_n(bin(i)[2:], 5)
            for index, value in enumerate(truth_values):
                command[keys[index]] = value == "1"
            commands.append(command)
        return commands

    def test_default_timeframe_is_all_time(self):
        timeframe = self.scorelistloop._ScoreListLoop__current_timeframe
        self.assertEqual(timeframe, "all time")

    def test_get_rendering_params_returns_list(self):
        rendering_params = self.scorelistloop._get_rendering_params()
        self.assertEqual(type(rendering_params), list)

    def test_timeframe_changes_to_one_corresponding_to_command(self):
        timeframes = ["last week", "last month", "all time"]
        commands = [{"week": True, "month": False, "all": False}, 
        {"month": True, "week": False, "all": False},
        {"all": True, "week": False, "month": False}]
        for command in commands:
            command["return to menu"] = False
            command["quit"] = False
        for index, command in enumerate(commands):
            self.scorelistloop._handle_commands(command)
            timeframe = self.scorelistloop._ScoreListLoop__current_timeframe
            self.assertEqual(timeframe, timeframes[index])
 