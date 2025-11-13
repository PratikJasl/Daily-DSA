# // Tere’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. 
# // Without altering the relative order of positive and negative elements, you must return
# // an array of alternately positive and negative values.
# // Note: Start the array with positive elements

# //Example:
# // Input: arr[] = {1,2,-4,-5}, N = 4
# // Output: 1 -4 2 -5
#Given: array(nums), even length, equal +ve/-ve.
#Approach:
#Step1: Create a positive and negative array.
#Step2: If the index is even fill with positive elements, else negative.
def rearrangeArray(nums):
        positive = []
        negative = []
        pos_idx = 0
        neg_idx = 0
        output = [0] * len(nums) #FIll output with zero till nums(len)

        for i in range(len(nums)):
            if(nums[i] > 0):
                positive.append(nums[i])
            else:
                negative.append(nums[i])
        
        for i in range(len(nums)):
            if i % 2 == 0:
                output[i] = positive[pos_idx]
                pos_idx += 1
            else:
                output[i] = negative[neg_idx]
                neg_idx += 1

        return output

rearrangeArray([3,1,-2,-5,2,-4])