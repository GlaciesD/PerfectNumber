#Get Input
u_i = int(input("Enter a large integer: "))
#Perfect number List
p_list = []
divisors = {0}

#Create range from u_i
p_options = [*range(2, u_i, 1)]
#Get Number from range.
for n in p_options:
    # Find all whole divisors.
    divisors.clear()
    for d in p_options:
        r = n / d
        #print("r:", r)
        if r.is_integer():
            divisors.add(r)
            #print("Current Number;", n, "Whole divisors:", divisors)
        else:
            pass
    # Add all whole divisors and check if sum = Number.
    # If sum = Number add Number to p_list.
    if sum(divisors) == n:
        p_list.append(n)
    # If not discard.
    else:
        pass
    # Get next Number in range.

print("Perfect Numbers:", p_list)