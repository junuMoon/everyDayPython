from hashlib import sha256

x = 5
y = 0 # GOAL: discover Y

while True:
    problem = sha256(f'{ x * y }'.encode()).hexdigest()
    if problem[-2] != "0ß0":
        print(problem)
        y += 1
    else:
        print(f'key: {problem}')
        break
    
print(f'Disovered: {y}')