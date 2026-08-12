class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        thought process

        for each car (sorted by position descending)
            find hourtime at which car arrives at the target
                if hourtime is smaller or equal to than the previous car
                    this cannot be so this car will join previous car
                        (remove car from stack)

                if hourtime is bigger than previous car
                    this will be a new fleet
                        (add car to stack)

        return len(stack)
        '''
        rel = {}
        for index, position in enumerate(position):
            rel[position] = index

        rel = sorted(rel.items(), reverse=True)

        stack = []   # stack top holds latest arrival time

        for car in rel:
            carposition = car[0]
            carspeed = speed[car[1]]

            arrival = (target - carposition) / carspeed
            if not stack:
                stack.append(arrival)

            elif arrival <= stack[-1]:
                continue

            else:
                stack.append(arrival)

        return len(stack)


