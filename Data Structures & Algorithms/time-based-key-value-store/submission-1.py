class TimeMap:

    def __init__(self):
        # Dictionary to store the key and a list of [value, timestamp] pairs
        self.keyStore = {}  # key: List of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If key is not in the dictionary, initialize an empty list
        if key not in self.keyStore:
            self.keyStore[key] = []
        # Append the [value, timestamp] pair to the list
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Get the list of [value, timestamp] for the key
        # If key does not exist, default to an empty list
        values = self.keyStore.get(key, [])
        
        res = ""  # Store the best candidate result
        l, r = 0, len(values) - 1

        # Binary search for the largest timestamp ≤ given timestamp
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                # Valid candidate — try to find a later valid one
                res = values[m][0]
                l = m + 1
            else:
                # Current timestamp too big → search left
                r = m - 1

        return res  # Return the most recent valid value or ""
