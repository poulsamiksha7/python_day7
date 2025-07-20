#Q1 Create Dictionary

dict={'a':"Samiksha",'b':"samiksha"}
print(dict)

#Q2 Frquency of letters
dict={'a':"Samiksha",'b':"Dnyanoba",'c':"Poul"}

all_txt="".join(dict.values())

freq={}

for char in all_txt:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(f"The frequency of letters is:",freq)     

# Merge two dictionaries
dict1={'a':1,'b':2}
dict2={'c':3,'d':4}

dict1.update(dict2)
print(dict1)
# Key exists in dict

dict={'name':"samiksha", 'age':22}
if 'name' in dict:
    print("The key exists in dict")
else:
    print("The key does'nt exists in dict")

#Set operations: union, intersection
set1={1,2,3,4}
set2={5,6,7,8}
union_set=set1.union(set2)
print("Union set",union_set)

intersection_set=set1.intersection(set2)
print("Intersection set",intersection_set)

# Remove duplicates using set
lst=[1,2,1,3,2,4,564,3,2]

dup_set=list(set(lst))
print(dup_set)

# Convert list to dict
pairs=[('a',1),('b',2)]
my_dict=dict(pairs)
print(my_dict)

#Sort dict by value

my_dict={'a':1,'b':2,'c':3}
sort_dict=dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sort_dict)

# Dict with list values
stu_sub={
    "Samiksha":["English","Biology"],
    "Suraj":["Geography","History"]
}
print(stu_sub["Samiksha"])

##- Convert dict to list of tuples
my_dict={'a':1,'b':2,'c':3}
my_tup=list(my_dict.items())
print(my_tup)