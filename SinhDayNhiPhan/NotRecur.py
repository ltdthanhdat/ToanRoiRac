# Chuyen day nhi phan tu list sang string
def binary_list_to_string(binary_list):
    return ''.join(binary_list)

# Chuyen day nhi phan tu string sang list
def binary_string_to_list(binary_string):
    return list(binary_string)

# Sinh so nhi phan ke tiep (list sequence)
def generate_next_binary_sequence(sequence):
    n = len(sequence)
    # Tim vi tri bang 0 dau tien tu ben phai
    for i in range(n - 1, -1, -1):
        if sequence[i] == '0':
            # Doi 0 thanh 1
            sequence[i] = '1'
            # Dat cac bien ben phai bang 0
            for j in range(i + 1, n):
                sequence[j] = '0'
            break
    return sequence


# Hàm sinh dãy nhị phân tiếp theo của một dãy cho trước
def generate_next_binary_sequence_from_string(binary_string):
    binary_list = binary_string_to_list(binary_string)
    next_sequence = generate_next_binary_sequence(binary_list)
    return binary_list_to_string(next_sequence)

def main():
    n = 3
    binary_sequence = "0"*n
    while binary_sequence != "1"*n:
        next_binary_sequence = generate_next_binary_sequence_from_string(binary_sequence)
        binary_sequence = next_binary_sequence
        print(binary_sequence)

if __name__ == "__main__":
    main()
