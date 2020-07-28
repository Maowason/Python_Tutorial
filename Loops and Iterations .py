nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)
print('\n')
# break - completely breaks out of loop
# continue - will continue to the next iteration

for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

print('\n')

for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)

print('\n')

for num in nums:
    for letter in 'abc':
        print(num, letter)  # We get every combination

print('\n')

# range
for i in range(1, 11):
    print(i)

print('\n')

# while - will keep going till certain condition is met or we hit a break
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

print('\n')

# infinite Loop
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1
