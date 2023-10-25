def generate_permutations(arr):
    if len(arr) <= 1:
        return [arr]
    else:
        permutations = []
        for i in range(len(arr)):
            first_element = arr[i]
            remaining_elements = arr[:i] + arr[i+1:]
            for p in generate_permutations(remaining_elements):
                permutations.append([first_element] + p)
        return permutations

# Sử dụng ví dụ
input_list = [1, 2, 3]
permutations = generate_permutations(input_list)
print("Tất cả các hoán vị của", input_list, "là:", permutations)
