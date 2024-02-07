def has_33(nums):
    x = len(nums)
    t = False
    for i in range(0, x - 1):
        if(nums[i] == nums[i + 1] and nums[i] == 3):
            t = True
            break
    if(t):
        print("True")
    else:
        print("False")
has_33([1, 2, 3, 3])