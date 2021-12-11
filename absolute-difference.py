# Prompt the user for the input
n = int(input()) # The legnth of the array
array = input() # The n space-seperated integers 


# Function to get the user input as an array of integers
def get_the_array(x):
    array_numbers = [int(s) for s in x.strip().split(' ') if s.lstrip('-').isnumeric()]
    return array_numbers

array_numbers = get_the_array(array)

# Check if the array is the same legnth the user enterd
if len(array_numbers) != n:
    print(f'The array must be {n} legnth')
    # Prompt the user for the input agin if the array legnth is not n
    n = int(input()) 
    array = input() 
    array_numbers = get_the_array(array)

# Claculate the absolute difference for each two numbers and check the minimum 
minimum = abs(array_numbers[0] - array_numbers[1])
for i in range(len(array_numbers)):    
    for j in array_numbers[i+1:]:
        if abs(array_numbers[i] - j) < minimum:
            minimum = abs(array_numbers[i] - j)
# Print the minimum absoulte difference value
print(minimum)