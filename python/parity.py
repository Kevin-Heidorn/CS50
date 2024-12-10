def main():
    x = int(input("What's X: "))
    if is_even(x):
         print("EVEN")
    else:
        print("ODD")

def is_even(n):
  if n % 2 == 0:
    return True
  else:
   return False
  
  

main()