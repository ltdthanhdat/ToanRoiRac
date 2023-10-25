
def generate_binary_sequences(n, prefix=""):
    if n == 0:
        print(prefix)
    else:
        generate_binary_sequences(n - 1, prefix + "0")
        print("xxx")
        generate_binary_sequences(n - 1, prefix + "1")
        print("xxx")

# Sử dụng hàm để sinh dãy nhị phân độ dài 3
generate_binary_sequences(3)

