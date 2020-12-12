print("bijayghosh.email@gmail.com")

# Write Python code here 
class sampleclass: 
    count = 0     # class attribute 
  
    def increase(self): 
        sampleclass.count += 1
  
# Calling increase() on an object 
s1 = sampleclass() 
s1.increase()         
print(s1.count) 
  
# Calling increase on one more 
# object 
s2 = sampleclass() 
s2.increase() 
print(s2.count) 
  
print(sampleclass.count)

#this simple command is very special to hold the output screen *untill we press the enter key* .
input('Press enter to exit')