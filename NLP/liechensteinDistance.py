'''
In this problem, you need to implement a function that calculates the Optimal String Alignment (OSA) distance between two given strings. The OSA distance represents the minimum number of edits required to transform one string into another. The allowed edit operations are:

Insert a character
Delete a character
Substitute a character
Transpose two adjacent characters
Each of these operations costs 1 unit.

Your task is to find the minimum number of edits needed to convert the first string (s1) into the second string (s2).

For example, the OSA distance between the strings "caper" and "acer" is 2: one deletion (removing "p"), and one transposition (swapping "a" and "c").

'''

def OSA(s1: str, s2: str) -> int:
    """
	dynamic programming!
    """
    m, n = len(s1), len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]


    for i in range(m + 1):
        dp[i][0] = i  
    for j in range(n + 1):
        dp[0][j] = j  

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0 
            else:
                cost = 1 

            dp[i][j] = min(
                dp[i - 1][j] + 1,    
                dp[i][j - 1] + 1,      
                dp[i - 1][j - 1] + cost  
            )

    return dp[m][n]
