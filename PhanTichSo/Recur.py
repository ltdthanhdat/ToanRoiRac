def find_all_sum_combinations(target, numbers, partial=[]):
    s = sum(partial)

    # Kiểm tra nếu tổng của các số trong partial bằng với target
    if s == target:
        print("Tổng các số:", partial)
    if s >= target:
        return
    for i in range(len(numbers)):
        remaining = numbers[i:]
        find_all_sum_combinations(target, remaining, partial + [numbers[i]])

# Sử dụng hàm với số 3 và tập hợp các số từ 1 đến 3
target_number = 5
available_numbers = list(range(1, target_number + 1))
find_all_sum_combinations(target_number, available_numbers)
