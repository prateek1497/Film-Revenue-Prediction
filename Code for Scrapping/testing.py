row = 'row-'
for i in range(2, 83):
    className = row+str(i)+" "+ ("odd" if i%2 else "even")
    print(className)

