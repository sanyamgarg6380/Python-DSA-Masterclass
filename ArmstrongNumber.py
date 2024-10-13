def armstrongNumber (n):
        right="true"
        wrong="false"
        ams=0
        temp=n
        while(n>0):
            lastDigit=n%10
            ams=ams+lastDigit**3
            n=n//10
        if(ams==temp):
            return right
        else:
            return wrong 

n=int(input("n="))
print(armstrongNumber(n))