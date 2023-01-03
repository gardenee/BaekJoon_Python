room_num = str(input())
numbers = [0] * 10

for num in room_num:
    numbers[int(num)] += 1

rotatable = numbers[6] + numbers[9]
if rotatable % 2 == 1:
    rotatable += 1

numbers[6], numbers[9] = rotatable//2, rotatable//2

print(max(numbers))
