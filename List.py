
###  NESTED LIST ADDITION ###

"""t = [[51, 36, 42], [65, 78, 92], [22, 69, 14]]
def nest(t):
    total = []
    for i in t:
        for j in i:
            total.append(j)
    print(total)        
    p = sum(total)
    print(p)




nest(t)"""

### CUMMULATIVE ADDITION OF SIMPLE LIST ###

"""t = [1, 2, 3, 4]

var1 = 0
for i in t:
    var1 = var1 + i

print(var1)"""






### REMOVING FIRST AND LAST ELEMENTS OF A LIST ###

"""t = [1, 2, 3, 4]

def middle(t):
    new = t[1:3]
    print(new)  
    
middle(t)"""  

### LIST SORTING ###

"""def is_sorted(t):
    t1 = sorted(t)
    if t == t1:
        print(t, "is sorted")
    else:
        print(t,"is unsorted")
    print(t1)
is_sorted([6,85,3])"""


###  DUPLICATE CHECKER ###

"""t = ["Vihaan", 1545, "Indy", 9, 1545, "Fortnite", 9, 333, 879]

newlist = []
duplist = []


for i in t:
    if i not in newlist:
        newlist.append(i)
    else:
        duplist.append(i)    


print("The duplicates are: ", duplist)
print("The non-duplicates are: ", newlist)"""







###