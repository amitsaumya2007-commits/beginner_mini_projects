def mean(x:list, round_to: int = 3) -> float:
    mn = sum(x)/len(x)
    return round(mn,round_to)

#print(mean([3,4,1,8,7,9],1))

def median(y:list) -> float:
    y.sort()
    mid= int(len(y)/2)
    if len(y)%2 == 0 :
        return y[mid], y[mid+1]
    else:
        return y[mid+1]
        
#print(median([3, 5, 7, 12, 13, 14, 20, 23, 29, 39, 40,24,43]))


def mode(z):
    if not z:
        return []
    
    # Step 1: Build a frequency dictionary manually
    frequency_dict = {}
    for num in z:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
            
    max_frequency = max(frequency_dict.values())
    modes = []
    for num, count in frequency_dict.items():
        if count == max_frequency:
            modes.append(num)
            
    return modes

nums1 = [3, 7, 7, 7, 14, 23, 23, 23, 40]
print("Modes for list 1:", mode(nums1))
# Output: Modes for list 1: [7, 23]

# Example 2: A single clear mode
nums2 = [1, 2, 2, 2, 3, 4, 5]
print("Modes for list 2:", mode(nums2))
# Output: Modes for list 2: [2]

z = [3, 7, 7, 7, 14, 23, 23, 23, 40]
frequency_dict = {}
for num in z:
    if num in frequency_dict:
        frequency_dict[num] += 1
    else:
        frequency_dict[num] = 1

print(frequency_dict)