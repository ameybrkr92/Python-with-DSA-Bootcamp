#O(n)
def print_items(n):
    for i in range(n):
        print(i)
        
print("O(n)")
print_items(5)


#O(2n)->O(n)
#Drop constants
def print_items_1(n):
    for i in range(n):
        print(i)
    
    for j in range(n):
        print(j)

print("----------")        
print("O(2n)->O(n)")
print_items_1(5)

#O(n*n)->O(n^2)
def print_items_2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print("----------")        
print("O(n^2")
print_items_2(5)

#O(n^2+n)->O(n^2)
#Drop Non-Dominant
def print_items_3(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
        
    for k in range(n):
        print(k)
        
print("----------")        
print("O(n^2+n)->O(n^2)")
print_items_3(5)

#O(1)

def add_items(n):
    return n+n

print("----------")
print("O(1)")
print(add_items(10))

#O(log(n))
#Devide & Conquer

#Different terms for inputs
#O(a)+O(b)->O(a+b)
#O(a)*O(b)->O(a*b)