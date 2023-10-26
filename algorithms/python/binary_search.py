import math

class BinarySearch:
    def search(self, arr, val):
        return self.recursive_search(arr, val, 0, len(arr) - 1)

    def recursive_search(self, arr, val, start, end):
        mid = math.floor((end + start) / 2)

        if start > end:
            return None

        if arr[mid] == val:
            return arr[mid]

        if arr[mid] < val:
            return self.recursive_search(arr, val, mid + 1, end)

        return self.recursive_search(arr, val, start, mid - 1)
