print('ASCII Table')
start = 32
end = 127
for v in range(start, end + 1):
    if (start - v) % 10 == 0:
        print("")
    print(f'{v} - {chr(v)} |', end=' ')

print(ord('a'))