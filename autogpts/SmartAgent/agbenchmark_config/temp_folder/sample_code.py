# Function to find indices of three numbers

def three_sum(nums, target):
    result = []
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    result.append([i, j, k])
    return result