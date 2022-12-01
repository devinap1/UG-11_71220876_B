y = input("masukkan kata: ")
palindrome = True

panjang_y = len(y)

for i in range(panjang_y//2):
    if (y[i] != y [panjang_y-i-1]):
        palindrome = False
        break
if palindrome:
    print ("yes")
    print ("jika dibalik: ",y)
else :
    print ("no")
    print ("jika dibalik: ", y)

y = input("masukkan kata: ")
palindrome = True 

panjang_y = len(y)

for i in range(panjang_y//2):
    if (y[i] != y[panjang_y-i-1]):
        palindrome = False
        break
if palindrome:
    print ("yes")
    print ("jika dibalik: ", y)
else :
    print ("no")
    print ("jika dibalik: ", y)