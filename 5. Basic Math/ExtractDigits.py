#Concept 1: Extraction of digits.

#Input: 7789
#Objective: extract individual digits from 7789

#Approach1: Convert 7789 into a string, iterate over it and extract the digits and convert them back.
#Approach2: Use Math operations division and modolue to extract the digits.

#EXPLANATION:
# Step1: Modolue 7789 with 10 i.e 7789 % 10 = 9 
# Any number not ending with 0 module with 10 will give the last digit. Like in this case 9.
# Step2: Now divide 7789 with 10 and consider the integer part i.e 7789/10 = 778.9 = 778.
# Repeat Step1 and Step2 to extract all the digits out of 7789.

# 1) 7789 % 10 = 9
# 2) 7789 / 10 = 778.9
# 3) 778 % 10 = 8
# 4) 778 / 10 = 77.8
# 5) 77 % 10 = 7
# 6) 77 /10 = 7.7
# 7) 7 % 10 = 7 

# Hence we got 9,8,7,7 from N = 7789

def ExtractDigits(N):
    while(N > 0):
        lastDigit = N % 10
        print(lastDigit)
        N = int(N / 10)

ExtractDigits(7789)


#---------------------------------------------Questions-------------------------------------------------------
# Question: Count the number of digits in a given number.
def CountDigit():
    N = int(input('Enter a Number: '))
    count = 0
    while(N > 0):
        lastDigit = N % 10
        count += 1
        N = int(N / 10)
    print(f'Number of digits are: {count}')

CountDigit()