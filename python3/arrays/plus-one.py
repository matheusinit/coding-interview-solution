#!/usr/bin/env python3

from typing import List

def solution(digits: List[int]) -> List[int]:
    # Current index (starts at the last digit - higher index)
    current_index = len(digits) - 1
    
    # Run until the first index
    while current_index >= 0:
        
        # Look up the current digit to analyze
        current_digit = digits[current_index]
        
        if current_digit < 9:
            digits[current_index] += 1
            break
        elif current_digit == 9:
            digits[current_index] = 0
            current_index -= 1
        
        # If the array goes pass the first index, in cases of [9, 9, ...]
        # Insert a leading 0 at first index
        # Increment current index by to go to first index
        if current_index < 0:
            digits.insert(0, 0)
            current_index += 1
    
    return digits

def solve():
    cases = [
        [1, 2, 3],
        [4, 3, 2, 1],
        [9]
    ]
    
    for case in cases:
        print(solution(case))

solve()
