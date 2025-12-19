'''48)Write a Python script to sort (ascending and descending) a
dictionary by value.'''

d={"b":2,"d":4,"a":1,"c":3}
sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
sorted_dict1 = dict(sorted(d.items(), key=lambda item: item[1],reverse=True))

print(sorted_dict)
print(sorted_dict1)



