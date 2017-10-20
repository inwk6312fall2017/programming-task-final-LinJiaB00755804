import string
#part 1 code: replace interface '172' with '192'
'''create a new file named 'newconfig.cfg'
and copy all the configuration information from 'running-config.cfg'
except the ip address started with "172" and replaced them with "192".'''
fin = open('running-config.cfg')
new = open('newconfig.cfg','w')
mylist = []
'''The item in mylist points out the interface name with a vlan ID which is seperate by '.' '''
for line in fin:
 clean_line = line.strip(string.whitespace)
 new_clean_line = clean_line.strip(string.punctuation)
 word_list = new_clean_line.split()
 for i in range(len(word_list)):
     if '172' in word_list[i]:
         word = word_list[i].split('.')
         if word[0] =='172':
             del word[0]
             word = ['192']+word
         delimiter = '.'
         word_list[i]=delimiter.join(word)
 delimiter = ' '
 newline=delimiter.join(word_list)

 new.write(newline)
 
 print(newline)

#part 2: accesslist:
import string
fin = open('running-config.cfg')
mydic = {}
for line in fin:
 clean_line = line.strip(string.whitespace)
 new_clean_line = clean_line.strip(string.punctuation)
 word_list = new_clean_line.split()
 #grid all the object and the word after it as a key and the whole accesslist line as value
 if 'access-list' in word_list:
  l = []
  for i in range(len(word_list)-1):
   if word_list[i] == "object":
    l.extend([word_list[i],word_list[i+1]])
  name = " ".join(l)
  mydic[name] = new_clean_line

'''create a dictionary named mydic to store the access_list
name as key and the whole line as value and print all access_list
lines in the configuration.'''
for name,line in mydic.items():
    print(name,'       ',line)
