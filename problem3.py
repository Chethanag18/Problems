a = int(input("Enter a number: "))

if a % 2 == 0:
    x = a // 2
else:
    x = (a + 1) // 2


odd_numbers = []
for i in range(x):
    odd_numbers.append(str(2 * i + 1))


print(",".join(odd_numbers))
