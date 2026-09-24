class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        # print(count)

        for num in hand:
            start = num
            if start not in count:
                continue
            while (start-1) in count:
                start = start - 1

            for i in range(groupSize):
                if start not in count:
                    return False
                count[start] -= 1
                if count[start] == 0:
                    del count[start]
                start += 1
            if not count:
                return True

        return True