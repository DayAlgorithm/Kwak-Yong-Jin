class Solution:
    def dfs(self, num, cur, end, nums, answer, visited):
        if cur == end:
            answer.append(num)
            return

        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                self.dfs(num + [nums[i]], cur + 1, end, nums, answer, visited)
                visited.remove(i)

    def permute(self, nums: List[int]) -> List[List[int]]:
        end = len(nums)
        answer = []
        visited = set()
        self.dfs([], 0, end, nums, answer, visited)
        return answer
