lower_range = int(input("Enter a lower range- "))
upper_range = int(input("Enter a upper range- "))
list = []
even_list = []
odd_list = []   
try:
    if upper_range == lower_range:
        raise Exception("The numbers are equal. Restart the program")
    elif upper_range < lower_range:
        raise Exception("The upper range is smaller than the lower range. Restart the program")
    elif upper_range <= 0:
        raise Exception("Upper range can not be less than or equal to 0. Restart the program")
    else:
        for i in range(lower_range,upper_range + 1,1):
            num = i**2
            list.append(num)
            if(num%2==0):
                even_list.append(i*i)
            else:
                odd_list.append(i*i)
        
except Exception as ex:
    print("Error",ex)
print("The square values of numbers between the range ",lower_range,"and",upper_range,"are",list) 
print("Even values within the range is : ", even_list)
print("Odd values within the range is : ", odd_list)
     
        