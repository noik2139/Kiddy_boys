def decide(num):
    sum = 0
    for i in range(1,num):
        if num%i == 0:
            sum += i
    
    if sum == num:
        return str(num) + "is a perfect number." 
    elif sum < num:
        return str(num) + "is deficient."
    else:
        return str(num) + "is abundant."

print(decide(6))
