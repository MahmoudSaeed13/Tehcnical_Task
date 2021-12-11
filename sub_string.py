# Taking the user input for two strigs
S1 = input('S1: ')
S2 = input('S2: ')

# Check if the two strings share a common substring
def check_common_substring(x, y):
    check = 0
    for i in x:
        for j in y:
            # Compare all characters case insensitively 
            if i.lower() == j.lower():
                check += 1
                # Return 'YES' if two characters are equal 
                return 'YES'
    # Return 'NO' if there are no common substrings
    if check == 0:
        return 'NO'

# Printing the function return
print(check_common_substring(S1,S2))
