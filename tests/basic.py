import unittest
import tictactoe


class PlayerTest(unittest.TestCase):
    def test(self):
        player = tictactoe.Player()
        self.assertEqual(player.take_action(), 4)


if __name__ == '__main__':
    unittest.main()
