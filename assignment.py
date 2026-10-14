""" Assalomu Aleykum
This is my Computer Programming (CP) Assignment 2
---------------------------
Name: Boltayev Yodgorbek
Group: FMC05
Assignment Variant: 9
---------------------------
"""

num_packet = int(input("Enter the number of coffee packets: "))


def classify(value):
    total = 0
    count = 0
    below = 0
    inside = 0
    above = 0
    for i in range(1,value+1):
        num_coffee = int(input("Enter the coffee packet weight:  "))
        total += num_coffee
        count += 1
        if num_coffee < 998:
            print("Below range")
            below += 1
        elif num_coffee in range(998,1001):
            print("In range")
            inside += 1
        else:
            print("Above range")
            above += 1
    return total, count, below, inside, above
        
total, count, below, inside, above = classify(num_packet)

def calculate_average(tot, cot):
    average = tot / cot
    return f"Average weight: {float(average)} g"


print(f"Total weight: {total} g")
print(calculate_average(total,count))
print(f"Below range: {below}")
print(f"In range: {inside}")
print(f"Above range: {above}")

