"""If you have a list x, write the code to safely remove
an item if—and only if—that value is in the list.
Modify that code to remove the element only if the item occurs in the list
more than once."""

x=[1,2,3,2,4,2]
if 6 in x:
    x.remove(6)    
if 1 in x:
    x.remove(1)
print(x)

'''if x.count(2)>1:
       x.remove(2)
print(x)'''

if x.count(2)>1:
    while 2 in x:
       x.remove(2)
print(x)       
