import unittest

def solution(A, K):
    N = len(A)
    if N == 0:
        return A
    K = K % N
    if K == 0:
        return A
    else:
        B = A[-K:] + A[:-K]
        return B
    
class TestRotation(unittest.TestCase):

    def test_rotation(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])
        self.assertEqual(solution([0, 0, 0], 1), [0, 0, 0])
        self.assertEqual(solution([1, 2, 3, 4], 4), [1, 2, 3, 4])
        self.assertEqual(solution([1, 2, 3, 4, 5, 6], 2), [5, 6, 1, 2, 3, 4])
        self.assertEqual(solution([1, 2, 3, 4, 5, 6], 7), [6, 1, 2, 3, 4, 5])
        self.assertEqual(solution([1, 2, 3, 4, 5, 6], 0), [1, 2, 3, 4, 5, 6])
        self.assertEqual(solution([], 10), [])
        self.assertEqual(solution([1], 1), [1])


if __name__ == '__main__':
    unittest.main()