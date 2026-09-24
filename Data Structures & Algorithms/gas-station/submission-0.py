class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_cost = 0
        total_gas = 0

        current_gas = 0
        index = 0

        for i in range(len(gas)):
            total_cost += cost[i]
            total_gas += gas[i]

            current_gas += gas[i]
            if current_gas >= cost[i]:
                current_gas -= cost[i]
                print(current_gas)
                continue
            else:
                current_gas = 0
                index = i + 1


        if total_gas >= total_cost:
            return index

        else:
            return -1