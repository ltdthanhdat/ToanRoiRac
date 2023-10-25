def generate_combinations(arr, r, index, combination, result):
    if r == 0:
        result.append(list(combination))
        return
    if index >= len(arr):
        return
    combination.append(arr[index])
    generate_combinations(arr, r - 1, index + 1, combination, result)
    combination.pop()
    generate_combinations(arr, r, index + 1, combination, result)

def get_all_combinations(arr):
    result = []
    for r in range(1, len(arr) + 1):
        generate_combinations(arr, r, 0, [], result)
    return result

# Sử dụng ví dụ
input_list = [1, 2, 3]
combinations = get_all_combinations(input_list)
print("Tất cả các tổ hợp của", input_list, "là:", combinations)
