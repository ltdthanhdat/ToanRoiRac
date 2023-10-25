def find_all_sum_combinations(target):
    combinations = [[] for _ in range(target + 1)]
    combinations[0].append([])

    for num in range(1, target + 1):
        for prev_num in range(num):
            for prev_combination in combinations[prev_num]:
                new_combination = prev_combination + [num - prev_num]
                combinations[num].append(new_combination)

    return combinations[target]

# Sử dụng hàm với số 3
target_number = 5
result = find_all_sum_combinations(target_number)
print("Tất cả các cách tạo ra số", target_number, "bằng tổng các số nguyên dương khác:")
print(result)
