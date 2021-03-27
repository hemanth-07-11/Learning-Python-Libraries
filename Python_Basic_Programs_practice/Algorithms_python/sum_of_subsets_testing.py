def generate_sum_of_subsets_soln(nums, max_sum):
    result = []
    path = []
    num_index = 0
    remaining_nums_sum = sum(nums)
    create_state_space_tree(nums, max_sum, num_index, path, result, remaining_nums_sum)
    return result

def create_state_space_tree(nums, max_sum, num_index, path, result, remaining_nums_sum):

    if sum(path) > max_sum or (remaining_nums_sum + sum(path)) < max_sum:
        return
    if sum(path) == max_sum:
        result.append(path)
        return
    for num_index in range(num_index, len(nums)):
        create_state_space_tree(
            nums,
            max_sum,
            num_index + 1,
            path + [nums[num_index]],
            result,
            remaining_nums_sum - nums[num_index],
        )

nums = [3, 34, 4, 12, 5, 2]
max_sum = 9
result = generate_sum_of_subsets_soln(nums, max_sum)
print(*result)
