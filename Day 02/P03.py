n = int(input("Enter n : "))
factoril_result = 1

result = 0
for i in range(1, n + 1):
    factoril_result *= i
    current_number = factoril_result
    result += current_number

result /= factoril_result

result += 1

print(result)