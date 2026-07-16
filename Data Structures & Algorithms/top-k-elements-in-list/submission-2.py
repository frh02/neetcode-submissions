class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNum = {}
        res = []
        ### [1,2,2,3,3,3]
        for idx, num in enumerate(nums):

            if num in countNum:
                countNum[num] +=1
            else:
                countNum[num] = 1 
                #countNum = {'1':0, '2':1,'3':2}
        #{'3':2,'2':1,'1':0}
        sortedByFreq = sorted(countNum, key=lambda x: countNum[x], reverse=True)

        # Step 3: Return top k elements
        return sortedByFreq[:k]
        