import unittest
from services.menuloop import MenuLoop
from tests.loop_test import StubRenderer, StubEventHandler, StubClock

class TestMenuLoop(unittest.TestCase):
    def setUp(self):
        self.menuloop = MenuLoop(StubRenderer(), StubEventHandler(), StubClock())
