from collections import defaultdict

class Distance(object):
    def __init__(self):
        self.count = 0
        self.distance_sum = float('inf')
        self.second_last = -1
        self.last = -1

    def add_distance(self, index):
        self.count += 1
        if self.count == 1:
            self.last = index
        elif self.count == 2:
            self.second_last = self.last
            self.last = index
        else:
            # המרחק של השלשה האחרונה (a, b, c) הוא 2 * (c - a)
            self.distance_sum = min(self.distance_sum, 2 * (index - self.second_last))
            self.second_last = self.last
            self.last = index

class Solution(object):
    def minimumDistance(self, nums):
        positions = defaultdict(Distance)
        minimum = float('inf')

        for i, num in enumerate(nums):
            positions[num].add_distance(i)

        for dist in positions.values():
            if dist.count >= 3:
                minimum = min(minimum, dist.distance_sum)

        return -1 if minimum == float('inf') else minimum