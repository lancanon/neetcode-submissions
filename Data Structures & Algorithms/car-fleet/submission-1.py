class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Step 1: Pair up position and speed for each car
        pair = [(p, s) for p, s in zip(position, speed)]
        
        # Step 2: Sort cars by position in reverse (start from car closest to target)
        pair.sort(reverse=True)

        stack = []  # Will store times to reach target for fleets

        # Step 3: Process each car from closest to furthest from target
        for p, s in pair:
            # Calculate time it takes for this car to reach the target
            time = (target - p) / s
            stack.append(time)

            # Step 4: If this car catches up to the car before it,
            # they form a fleet → remove the current one from stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # Merge the fleet

        # Step 5: Remaining entries in stack = number of fleets
        return len(stack)
