import unittest

def solution(N):
    binary = bin(N)[2:]
    max_gap = 0
    current_gap = 0

    for char in binary:
        if char == '0':
            current_gap += 1
        else:
            if current_gap > max_gap:
                max_gap = current_gap
            current_gap = 0

    return max_gap


class TestSolution(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solution(1041), 5)
        self.assertEqual(solution(529), 4)
        self.assertEqual(solution(20), 1)
        self.assertEqual(solution(15), 0)
        self.assertEqual(solution(32), 0)

if __name__ == '__main__':
    unittest.main()