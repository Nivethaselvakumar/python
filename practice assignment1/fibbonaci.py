nterms=int(input("enter a number"))
n1 = 0
n2 = 1
l=[]
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       l.append(n1)
       nth = n1 + n2
       
       n1 = n2
       n2 = nth
       count += 1
       
   print(l)
      
       
