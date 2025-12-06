def ran_check(num,low,high):
    if num in range(low,high):
        return f"{num} is in the range of {low} and {high}"
    else: return f"{num} is not in the range of {low} and {high}"
    
print(ran_check(9,2,7))