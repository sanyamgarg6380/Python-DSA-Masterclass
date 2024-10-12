def isPalindrome(x: int) -> bool:
    rev=0
    temp=x 

    if x<0:
        return False
    else:
        while(x>0):
            lastDigit = x % 10
            rev = (rev * 10) + lastDigit
            x = x//10
            
        if(rev == temp):
            return True 
        else:    
            return False

# Calling of the functiona
x = int(input("x = "))
print(isPalindrome(x))