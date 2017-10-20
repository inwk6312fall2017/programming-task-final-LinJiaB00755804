import string
book1 = open('Book1.txt')
book2 = open('Book2.txt')
book3 = open('Book3.txt')
# grid all the words as string in the list
list1=[]
for line in book1:
 cleanline = line.strip(string.whitespace)
 new_cleanline = cleanline.strip(string.punctuation)
 list1.extend(new_cleanline.split())
list2=[]
for line in book2:
 cleanline = line.strip(string.whitespace)
 new_cleanline = cleanline.strip(string.punctuation)
 list2.extend(new_cleanline.split())
list3=[]
for line in book3:
 cleanline = line.strip(string.whitespace)
 new_cleanline = cleanline.strip(string.punctuation)
 list3.extend(new_cleanline.split())
#create a dictionary and put the length of word as value and get the biggest word in each word list 
def biggest(a):
 d = {}
 for i in a:
  if not "http" in i:
   d[i] = len(i)
 newlist = list(sorted([(v,k) for (k,v) in d.items()],reverse = True))
 return newlist[0]
#comparing the biggest words in three book and get the biggest one
big1 = biggest(list1)
big2 = biggest(list2)
big3 = biggest(list3)
t = (big1,big2,big3)
t = sorted(t)
print("The biggest word in each book are: ",t)
print("The biggest word in all three book is: ",t[-1][1])
