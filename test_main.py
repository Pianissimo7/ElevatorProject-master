import unittest
import main
from CallForElevator import CallForElevator
from Building import Building
from Elevator import Elevator


class test_main(unittest.TestCase):

    def test_allocate(self):
        elevator1 = Elevator(0, 10, 0, 10, 2, 2, 3, 3)
        elevator2 = Elevator(1, 5, 0, 10, 2, 2, 3, 3)
        building = Building(0, 10, [elevator1, elevator2])
        call1 = CallForElevator(0, 3, 5, 0, -1)
        call2 = CallForElevator(3, 0, 10, 0, -1)
        call1 = main.allocate(building, call1, 10)
        call2 = main.allocate(building, call2, 10)

        self.assertEqual(call1.elev, 1)
        self.assertEqual(call2.elev, 0)

    def test_min_calls(self):
        elevator1 = Elevator(0, 10, 0, 10, 2, 2, 3, 3)
        elevator2 = Elevator(1, 5, 0, 10, 2, 2, 3, 3)
        building = Building(0, 10, [elevator1, elevator2])
        call1 = CallForElevator(0, 4, 8, 0, -1)
        call2 = CallForElevator(0, 2, 9, 0, -1)
        call3 = CallForElevator(0, 3, 5, 0, -1)

        main.allocate(building, call1, 10)
        main.allocate(building, call2, 10)
        main.allocate(building, call3, 10)

        self.assertEqual(main.min_calls(building), 1)
