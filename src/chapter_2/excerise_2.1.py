# Question:
"""
(Convert Celsius to Fahrenheit) 
    Write a program that reads a Celsius degree from
    the console and converts it to Fahrenheit and displays the result. The formula for
    the conversion is as follows:

fahrenheit = (9 / 5) * celsius + 32
"""

# Solution:
"""        
Algorithm:

    1.Recieve The celcuis value from the console(user)
    2. compute the value for fahrenheit using the formula above
    3. Display the output 
    
"""
celsius = eval(input("Enter a degree in Celsuis: "))

fahrenheit = (9 / 5) * celsius + 32

print(celsius, "Celsius is",  fahrenheit, "Fahrenheit")
