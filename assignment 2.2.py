# -*- coding: utf-8 -*-
"""
Assignment 2.2
"""
#1.changing values in a tuple
l1=(10,20,30,40,50);
l1=list(l1);
l1.append(40);
l1=tuple(l1);


#2.creating dictionary with list and dictionary as values
dictionary={1:[[10,20],{'ten':10}],2:[[10,20],{'twenty':20}]};


#3.dictionary methods
dictionary1={1:[10,20],2:[30,40],3:[50,60],4:[70,80]};
dictionary2={'one':[1,2],'two':[3,4],'three':[5,6]};
dictionary3={'1','2','3'};
y=0;
dictionary2.clear();#clearing dictionary elements
dictionary2=dictionary1.copy();#copying dictionary elements
dictionary4=dict.fromkeys(dictionary3,y);#creates new dictionary
x=dictionary1.get(1);#gets value of dictionary1 with key value 1
l1=dictionary4.items();#
dictionary1.pop(1)#poping value from dictionary1 using key=1
dictionary1.popitem();#pops the last element
z=dictionary1.setdefault(4,[90,100]);#returns the value of the item with the specified key
dictionary1.update({5: [20,40]})#insert an item to the dictionary
w=dictionary1.values()#returns all the values


#4.String methods
string1='heLLo WorLd';
string2='B\tI\tG';
string3 = "The price of the ticket is{price:2f}"
t1=['apple','orange','mango'];
string4='pineapple,orange,mango,grapes'
txt='Hello world/nWelcome to python';
txt1='Bellows'
a=string1.capitalize();#first character gets capitalized and rest is lower case
b=string1.casefold();#Converts string into lower case
c=string1.center(11);#Returns a centered string
d=string1.count('L');#counts the number of times L occurs in the string
e=string1.encode();#encodes the text
f=string1.endswith('WorLd');#checks whether string 1 ends with WorLd
g=string2.expandtabs(2);#Sets the tab size of the string
h=string1.find('heLLo');#Searches the string for a specified value and returns the position of where it was found
i=string3.format(price=100);#Formats specified values in a string
j=string3.index('p');#Searches the string for a specified value and returns the position of where it was found
k=string1.isalnum();#Returns True if all characters in the string are alphanumeric
l=string1.isalpha();#Returns True if all characters in the string are in the alphabet
m=string1.isascii();#Returns True if all characters in the string are ascii characters
o=string1.isdecimal();#Returns True if all characters in the string are decimals
p=string1.isdigit();#Returns True if all characters in the string are digits
q=string1.isidentifier();#Returns True if the string is an identifier
r=string1.islower();#Returns True if all characters in the string are lower case
s=string1.isupper();#Returns True if all characters in the string are uppper case
u=' and '.join(t1);#Converts the elements of an iterable into a string
v=string1.ljust(20);#Returns a left justified version of the string
a1=string1.isnumeric()#Returns True if all characters in the string are numeric
b1=string1.isprintable()#Returns True if all characters in the string are printable
c1=string1.isspace()#Returns True if all characters in the string are whitespaces
d1=string1.istitle()#Returns True if the string follows the rules of a title
e1=string1.replace('WorLd','Earth')#Returns a string where a specified value is replaced with a specified value
f1=string1.rfind('WorLd')	#Searches the string for a specified value and returns the last position of where it was found
g1=string1.rindex('WorLd')#Searches the string for a specified value and returns the last position of where it was found
h1=string1.rjust(20)#Returns a right justified version of the string
i1=string3.rpartition('price')#Returns a tuple where the string is parted into three parts
j1=string4.rsplit(',')#Splits the string at the specified separator, and returns a list
k1=string1.rstrip()#Returns a right trim version of the string
m1=string4.split(',')#Splits the string at the specified separator, and returns a list
n1=txt.splitlines()#Splits the string at line breaks and returns a list
o1=string1.startswith('Hello')#Returns true if the string starts with the specified value
p1=string1.strip()#Returns a trimmed version of the string
q1=string4.swapcase()#Swaps cases, lower case becomes upper case and vice versa
r1=string4.title();#Converts the first character of each word to upper case
s1=string1.translate('h');#Returns a translated string
t1=string4.upper();#Converts a string into upper case
u1=txt1.zfill(10);#Fills the string with a specified number of 0 values at the beginning













