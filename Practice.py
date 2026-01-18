nums = [1,3,1,2,4,4]
count = {}
least_value = None
least_count = float('inf')

for item in nums:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

for value, cnt in count.items():
    if cnt < least_count:
        least_count = cnt
        least_value = value

print(least_value)
