class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 2 pointers and sliding window of size len(s1) and hashmap to check if they are the same
        n,m = len(s1), len(s2)
        if n>m:
            return False

        # hash for s1 and hash for initial window of size(s1) from s2
        count1,count2 = {},{}
        for i in range(n):
            count1[s1[i]] = 1 + count1.get(s1[i],0)
            count2[s2[i]] = 1 + count2.get(s2[i],0)

        if count1 == count2: return True

        #compare all windows by sliding one element at a time and deleting the 1st element
        for j in range(n,m):
            count2[s2[j]] = 1 + count2.get(s2[j],0) 
            count2[s2[j-n]] -= 1

            # Make sure to delete the dictionaries with count 0
            if count2[s2[j-n]] == 0: del count2[s2[j-n]]

            if count2 == count1:
                return True
        return False 
        

        


        