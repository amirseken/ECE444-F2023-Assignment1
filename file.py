class utils:

    def reversed(num):
        print("Hello")
        reversed_num = 0
        while num != 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10
        return reversed_num
        
   
    def formatter(num):
        return (bin(num), oct(num))

   
