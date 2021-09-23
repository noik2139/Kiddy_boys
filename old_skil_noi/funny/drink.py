def sum_of_factors(num):
    sum = 0
    for i in range(1,num):
        if num%i == 0:
            sum += i
    return sum


def decide(num):
    sum = sum_of_factors(num)
 
    if sum == num:
        return str(num) + " is a perfect number." 
    elif sum < num:
        return str(num) + " is deficient."
    else:
        return str(num) + " is abundant."
        


