# def generate_ordered_combinations(elements, length, prefix=[]):
#     if length == 0:
#         print(prefix)
#     else:
#         for element in elements:
#             generate_ordered_combinations(elements, length - 1, prefix + [element])

# # Sử dụng hàm để sinh tất cả các tổ hợp có thứ tự của [1, 2, 3]
# elements = [1, 2, 3]
# length = len(elements)
# generate_ordered_combinations(elements, length)
def generate_combinations(arr):
    all_combinations = [[]]

    for num in arr:
        new_combinations = [item + [num] for item in all_combinations]
        all_combinations.extend(new_combinations)

    # Lọc ra các tổ hợp có độ dài khác 0 (tức là không chứa phần tử rỗng)
    non_empty_combinations = [item for item in all_combinations if item]

    return non_empty_combinations

# Sử dụng ví dụ
input_list = [1, 2, 3]
combinations = generate_combinations(input_list)
print("Tất cả các tổ hợp của", input_list, "là:", combinations)
