# Create a variable called 'price' as a string with the value '19.99'.
price = '19.99'
# Convert 'price' to a float and store it in a new variable called 'price_float'.
price_float = float(price)
# Create a variable called 'quantity' as an integer with a value 5.
quantity = 5
# Calculate the total cost by multiplying 'price_float' and 'quantity', and store it in a variable called 'total_cost'.
total_cost = price_float * quantity
# Convert 'total_cost' to an integer (round down) and store it in a variable called 'total_cost_int'.
total_cost_int = int(total_cost)
# Print out 'price', 'price_float', 'quantity', 'total_cost', 'total_cost_int' along with their types.
print(f"Price (string): {price}, Type: {type(price)}")
print(f"Price (float): {price_float}, Type: {type(price_float)}")
print(f"Quantity (integer): {quantity}, Type: {type(quantity)}")
print(f"Total Cost (likely float): {total_cost}, Type: {type(total_cost)}")
print(f"Total Cost (integer): {total_cost_int}, Type: {type(total_cost_int)}")


#Outputs

# C:\Users\MANVENDRA\PycharmProjects\pythonProject\.venv\Scripts\python.exe C:\Users\MANVENDRA\PycharmProjects\PythonLearning\Operators\type_conversion.py
# Price (string): 19.99, Type: <class 'str'>
# Price (float): 19.99, Type: <class 'float'>
# Quantity (integer): 5, Type: <class 'int'>
# Total Cost (likely float): 99.94999999999999, Type: <class 'float'>
# Total Cost (integer): 99, Type: <class 'int'>