list1=["a","b","c","d"]
list2=[1,2,4,6,]

list3=list1+list2
print(list3)

list1=["a","b","c","d"]
list2=[1,2,4,6,]

for x in list2:
    list1.append(x)

    print(list1)

# using append()
list1=["a","b","c","d"]
list2=[1,2,4,6,]

list1.extend(list2)
print (list1)

# example 2
list1=["a","b","c","d"]
list2=[1,2,4,6,]

list2.extend(list1)
print (list2)

