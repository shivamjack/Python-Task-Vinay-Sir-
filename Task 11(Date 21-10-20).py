#!/usr/bin/env python
# coding: utf-8

# ## Task 11

# In[ ]:





# In[5]:

number1 = int(input('Enter 1st number: '))
number2 = int(input('Enter 2nd number: '))
ans = int(input('press 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: '))


def addition(number1,number2):
    Jack = number1 + number2
    print('Addition is :',Jack)
def substraction(number1,number2):
    Jack = number1 - number2
    print('Substraction is :',Jack)
        
def multiplication(number1,number2):
    Jack = number1 * number2
    print('multiplication is :' ,Jack)
def division(number1,number2):
    Jack = number1 / number2
    print('Division is: ',Jack)
        
if ans == 1:
    addition(number1,number2)

elif ans == 2:
    substraction(number1,number2)
    
elif ans == 3:
    multiplication(number1,number2)
    
elif ans == 4:
    division(number1,number2)
else:
    print("Error press only 1,2,3,4")

    


# In[ ]:




