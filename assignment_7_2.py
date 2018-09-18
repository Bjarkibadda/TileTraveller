def count_case(setning):
    upper = 0
    lower = 0
    for i in setning:
        if i.isupper():
            upper +=1
        if i.islower():
            lower +=1
    return upper,lower
    
user_input = input("Enter a string: ")

upper_lower = count_case(user_input)
upper = upper_lower[0]
lower = upper_lower [1]
print("Upper case count: ", upper)
print("Lower case count: ", lower)




