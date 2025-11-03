def even (n):
    for i in range (n):
        if (i%2==0):
            yield i
display = even (100)
for i in display:
    print(i)