def threeSum(nums):
    arr = []
    for i, _ in enumerate(nums):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    arr.append(sorted([nums[i], nums[j], nums[k]]))
    return [list(x) for x in list(set(map(tuple, arr)))]
