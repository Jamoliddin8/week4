def replace_value(values, index, new_value):
    values[index]=new_value
    return None
def find_first(values, target):
    for index in range(len(values)):
        if values[index]==target:
            return index
    return -1
def summarize(values):
    m=min(values)
    n=max(values)
    s=sum(values)
    return (m, n, s)
days=int(input("Enter the number of days: "))
original=[]
for i in range(days):
    cooking=int(input("Enter cooking time in minutes: "))
    original.append(cooking)
updated=original[:]
ind=int(input("Enter the index to correct: "))
new=int(input("Enter the new cooking time: "))
replace_value(updated, ind, new)
search=int(input("Enter the cooking time to search for: "))
target=search
find_first(updated, target)
many=updated.count(target)
minimum, maximum, total = summarize(updated)
d=sorted(updated)
print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {d}")
print(f"Minimum cooking time: {minimum} minutes")
print(f"Maximum cooking time: {maximum} minutes")
print(f"Total cooking time: {total} minutes")
found=find_first(updated, target)
if found!=-1:
    print(f"First matching index: {found}")
else:
    print("Target not found")
print(f"Matching values: {many}")


