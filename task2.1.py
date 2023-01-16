number = int(input())
number_1 = number
def is_square(n):
     if n==0:
         return False
     else:
         if int(int(number ** (0.5)) ** 2) == number_1:
                 return True
         return False

print(is_square(number))