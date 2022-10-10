#    ....... list ......
...
list=['a','b','c','d','e',4,8,9]
print('list=',list)
#result : list= ['a', 'b', 'c', 'd', 'e', 4, 8, 9]

#......add a item.......
list.append('g')
print('After adding g the list is:', list)
#result : After adding g the list is: ['a', 'b', 'c', 'd', 'e', 4, 8, 9, 'g']

# .....add a list.....
list1=[5,3,'l']
list1.extend(list)
print('Two lists are appended:',list1)
#result: Two lists are appended: [5, 3, 'l', 'a', 'b', 'c', 'd', 'e', 4, 8, 9, 'g']

 # ......remove.....
list1.remove('e')
print('After removing e from list1 ', list1)
#result: After removing e from list1  [5, 3, 'l', 'a', 'b', 'c', 'd', 4, 8, 9, 'g']

#..... remove all same item....
list3=['a','b','c','c','a',4,2,4,4,7,8,4]
while 4 in list3:
    list3.remove(4)
print('After removing all 4 the list3 :',list3)
# result: After removing all 4 the list3 : ['a', 'b', 'c', 'c', 'a', 2, 7, 8]
...
 #   ...........tuple.....

 #tuple=('a','b','c',5,5,7,8)
 #print('tuple',tuple)

 #  ......set......
set1={'a','b','c','d','e',4,5,9,9,'a'}
print('The set1 is :',set1)
#result: The set1 is : {4, 5, 9, 'a', 'e', 'c', 'b', 'd'}
set1.add('f')
print('After adding f the set1:',set1)
#result: After adding f the set1: {'f', 4, 5, 'b', 'd', 9, 'e', 'c', 'a'}
set2={'z','y',11,'x',20}
set1.update(set2)
print('After updating set1 :',set1)
#result : After updating set1 : {4, 5, 'b', 9, 11, 'd', 'x', 'z', 'c', 'y', 20, 'a', 'e', 'f'}

set1.remove('y')
print(set1)


# .......... 1 to 100 addition.....
sum=0
for x in range(0,101,1):
    sum+=x
print('The sum is :',sum)

dic={'name':'asraf','sub':'cse','roll':1010}
print('The dictionary is:',dic)
#print(dic['roll'])
dic['number']=89
print(dic)



