def solution(N):
    binary = bin(N)[2:]
    print(binary)
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


assert solution(1041) == 5
assert solution(529) == 4
assert solution(20) == 1
assert solution(15) == 0
assert solution(32) == 0
print("if non error shown so it pass the test case")