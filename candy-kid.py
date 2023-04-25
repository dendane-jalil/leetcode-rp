#The problem can be found at leet code : 1431. Kids With the Greatest Number of Candies
# the problem is considered easy 

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        List = []
        for candy in candies : 
            if candy + extraCandies >=maxi:
                List.append(True)
            else :
                List.append(False)
        return(List)
            