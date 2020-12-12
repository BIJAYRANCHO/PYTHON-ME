import time
#Import tells Python to load a module with the tools that I need for the task.
#Time is the name of the module. From that module, I’ll need a method called ‘sleep’ that I’ll use to pause the program for a set amount of time.
main()
{

#Step 1: Asking for reminder

reminder == user.Asking("What shall I remind you about?")
print(reminder)



text = str(input())

#Step 2: Asking for time

print("In how many minutes ?")
local_time = float(input())

#Step 3. Calculate timeout

local_time = local_time * 60

#Step 4. Wait
time.sleep(local_time)
#I have a number of seconds in ‘local_time’. I give that number to ‘Sleep,’ and the program sleeps for the specified number of seconds

#Step 5. Remind
print(text)
}

def __name__=="__main__": 
    main()


