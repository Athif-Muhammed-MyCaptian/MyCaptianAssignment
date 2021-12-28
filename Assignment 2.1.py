# -*- coding: utf-8 -*-
"""
Assignment 2.1
"""
#1.Create a step function loop
a=int(input('Enter a:'))
b=int(input('enter b:'))
c=int(input('enter c:'))
choice='y'
x=lambda a:b+c;
while choice=='y':
    x1=x(a)
    print(x1);
    choice=input('Enter your choice:(y/n)');
    if choice=='n':
        break


    
    
    
#2.different methods of a list

l1=[10,20,30,40,40,40];
l2=['ten','twenty'];

l1.append(50);#adds 50 to the end of l1
l2.clear();#removes all elements from l2
l2=l1.copy();#copies elements of l1 to l4
x=l1.count(40);#x returns the number of times 40 has been counted
l2.extend(l1);#adds all the elements of l1 to l3
i=l1.index(10);#returns the index value of 10 in l1
l2.insert(3,10);#inserts 10 at index position 3 
l2.pop();#removes the end element of l2
l2.remove(40);#removes an element with the value 40
l1.reverse();#reverses the order of the elements in the list
l2.sort();#sorts the elements of l2




