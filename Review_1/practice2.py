nums = [1, 2, 4, 5]

nums_sum= sum(nums)

maxi= max(nums)

total= maxi * (maxi + 1) /2
missing_number = int(total- nums_sum)

print(missing_number)

l1= [1,2,3,4,5]

dict_comp = {x : x**2 for x in l1}
# print(dict_comp)

