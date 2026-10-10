def classify(value):
    if value<148:
        return "Below range"
    elif value>152:
        return "Above range"
    else:
        return "In range"
def calculate_average(total, count):
    average=total/count
    return average
bars=int(input("Enter the number of soap bars: "))
total=0
count=0
below=0
above=0
in_range=0
for bars in range(1, bars+1):
    value=int(input("Enter the soap bar weight: "))
    classification=classify(value)
    print(classification)
    total+=value
    count+=1
    if classification=="Below range":
        below+=1
    elif classification=="Above range":
        above+=1
    else:
        in_range+=1
avg=calculate_average(total, count)
print(f"Total weight: {total} g")
print(f"Average weight: {avg} g")
print(f"Below range: {below}")
print(f"In range: {in_range}")
print(f"Above range: {above}")