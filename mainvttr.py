import unittest
from tracker_logic import LectureLogic

class TestlectureLogic(unittest.TestCase):
    def setUp(self):
        self.logic = LectureLogic()
        self.logic.add_lecture("Mathe")#offen
        self.logic.add_lecture("Informatik", "besucht")
        
    def test_status_setzen(self):
        result = self.logic.set_status("Mathe", "gesehen")
        self.assertTrue(result)
        
    def test_offene_vorlesungen_zaehlen(self):
        self.assertEqual(self.logic.count_open_lectures(),1)
        
    def test_fortschritt_berechnen(self):
        # 1 von 2 erledigt (informatik besucht) => 0.5
        progress = self.logic.calculate_progress()
        self.assertEqual(progress, 0.5)
        
        
        
    if __name__ == "__main__":
        unittest.main()