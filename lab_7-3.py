"""
Create a Python file named lab_7-3.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Copy your lab 7-1 code into the file
Add 4 test cases to the end of the file, with comments
Ensure your lab runs accurately

"""
def find_sum(num1,num2):
    """Finds the sum of the two inputed numbers"""
    num_sum = num1 + num2
    return num_sum
    
print(find_sum(111,222) == 333)
print(find_sum(1,2) == 3)
print(find_sum(1.5,1.5) == 3)
print(find_sum(2763,2763) == 5526)