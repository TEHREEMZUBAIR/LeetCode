class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # Initialize an empty list to store the result
        result = []
        # Find the maximum number of candies any kid has
        max_candies = max(candies)
        
        # Loop through each kid's candy count
        for candy in candies:
            # Check if giving extraCandies makes the current kid have the most or equal to the most
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result
