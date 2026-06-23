class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Create a dictionary to store each number and its index
        seen = {}

        # Loop through the list with both index and number
        for index, current_number in enumerate(numbers):
            # Calculate the number we need to reach the target
            needed_number = target - current_number

            # Check if we've already seen the needed number
            if needed_number in seen:
                # If yes, return the index of the needed number and the current index
                return [seen[needed_number], index]

            # Otherwise, store the current number with its index
            seen[current_number] = index
