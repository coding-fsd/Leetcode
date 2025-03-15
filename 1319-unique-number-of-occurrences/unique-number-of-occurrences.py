class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]] = 1
            else:
                x = d.get(arr[i])
                x += 1
                d.update({arr[i] : x})

        li = d.values()
        return len(li) == len(set(li))