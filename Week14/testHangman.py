import unittest

from hangman import Hangman

class TestHangman(unittest.TestCase):
    def setUp(self):
        self.Hman = Hangman()
    def tearDown(self):
        pass

    def testDecreaseLife(self):
        self.assertTrue(self.Hman.remainingLives)

    def testCurrentShape(self):
        self.assertEqual(self.Hman.currentShape(),'''\
   ____
  |    |
  |
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''')


if __name__ == '__main__':
    unittest.main()
