num= int(input("print sum of even number till :"))
sum = 0
for i in  range  (1, num + 1):
    if i % 2 == 0 :
       sum = sum + i
print ("sum of even number form 1 to",num,"is", sum ) 