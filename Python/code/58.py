'''58)Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, o {'item': 'item1', 'amount': 750}]
Expected Output:
• Counter ({'item1': 1150, 'item2': 300})'''

data=[{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
d={}

d[data[0]['item']]=data[0]['amount']+data[2]['amount']
d[data[1]['item']]=data[1]['amount']

print(d)
