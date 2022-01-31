class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while k > 0:
            num = nums.pop()
            nums.insert(0, num)
            k -= 1