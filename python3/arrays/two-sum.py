#!/usr/bin/env python3
from typing import List

def solution(nums: List[int], target: int) -> List[int]:
    hash = {}

    for i in range(len(nums)):
        subtraction = target - nums[i]

        if subtraction in hash:
            return [hash[subtraction], i]
        else:
            hash[nums[i]] = i


def solve():
    nums = [2, 7, 11, 15]
    target = 9

    print(solution(nums, target))

solve()
