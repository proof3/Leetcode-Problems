class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        cust_wealth = [sum(customer) for customer in accounts]
        return max(cust_wealth)