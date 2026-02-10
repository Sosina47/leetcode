class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n != 1:
            c = []
            for i in str(n):
                c.append(int(i) ** 2)
            n = sum(c)
            if n in s:
                return False

            s.add(n)

        return True

        























# class Solution:
#     def isHappy(self, n: int) -> bool:
#         nums = set()
#         while n not in nums:
#             nums.add(n)
#             temp = 0
#             while n != 0:
#                 temp += (n % 10) ** 2
#                 n //= 10
#             n = temp

#             if n == 1:
#                 return True

#         return False 