def generate_odd_series(a):
    result = []
    num = 1
    count = 0
    while count < a:
        result.append(str(num))
        num += 2
        count += 1

    return ",".join(result)

a = int(input())
series = generate_odd_series(a)
print("Odd number series:", series)
