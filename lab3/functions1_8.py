def spygame(nums):
    x = len(nums)
    t = False
    for i in range(1, x - 1):
        if(nums[i] == nums[i - 1] and nums[i] == 0 and nums[i + 1] == 7):
            t = True
            break
    if(t):
        print("True")
    else:
        print("False")
spygame([1, 0, 0, 7])