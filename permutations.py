    def permute(nums: List[int]) -> List[List[int]]:
        def backtrack(nums, seen, out, curr):
            if len(curr) == len(nums):
                out.append(curr)
            for num in nums:
                if num not in seen:
                    seen.add(num)
                    backtrack(nums, seen, out, curr + [num])
                    seen.remove(num)
        seen = set()
        out = []
        curr = []
        backtrack(nums, seen, out, curr)
        return out
