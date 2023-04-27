import unittest
from services.group_handler import GroupHandler

class StubGroup:
    def __init__(self):
        self.__elements = []

    def add(self, element):
        self.__elements.append(element)

    def sprites(self):
        return self.__elements

    def __eq__(self, other):
        return self.__elements == other.sprites()

class TestGroupHandler(unittest.TestCase):
    def setUp(self):
        self.group_handler = GroupHandler()
        self.group = StubGroup()

    def test_group_returns_empty_group(self):
        group = self.group_handler.group()
        self.assertEqual(group, self.group)

    def test_elements_returns_empty_list_for_new_group(self):
        self.assertEqual(self.group_handler.elements(self.group), [])

    def test_elements_returns_list_of_added_elements(self):
        elements = ["element 1", "element 2", "element 3"]
        for element in elements:
            self.group.add(element)
        group_elements = self.group_handler.elements(self.group)
        self.assertEqual(group_elements, elements)

    def test_add_adds_element_to_group(self):
        self.group_handler.add("element", self.group)
        element_group = StubGroup()
        element_group.add("element")
        self.assertEqual(self.group, element_group)
