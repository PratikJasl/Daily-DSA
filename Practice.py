# Top K frequent elements.

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    freq = {}
    bucket = []
    result = []

    # Step1: Freq map
    for i in range(n):
        if nums[i] in freq:
            freq[nums[i]] += 1
        else:
            freq[nums[i]] = 1
    
    print("frequency:", freq)

    # Step2: Create Empty Buckets
    for i in range(n):
        bucket.append([])
    
    print('Empty bucket', bucket)

    # Step3: Fill buckets
    for value, count in freq.items():
        bucket[count].append(value)
    
    print("Filled Bucket:", bucket)

    # Step4: Choose top k from bucket
    for i in range(n-1, -1, -1):
        for n in bucket[i]:
            result.append(n)
            if(len(result) == k):
                print("final Result:", result)
                return result

top_k_frequent([1,1,1,2,2,3], 2)