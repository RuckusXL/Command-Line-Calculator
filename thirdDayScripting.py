print("Hello, World!")

#Back again, let's see what I remember

name = "Hadi"
age = 100
religion = "muslim"
answer = 100/20
god = "Allah SWT"
python = "Python is fun!"

if answer == 5:
    print(f"Good Morning, my name is {name} and I am {age} years old. I am a {religion} and I believe and love {god}.\nBecause of him I am able to learn how to code using python. {python}")
else:
	print("{p}".format(p = "Python is fun!"))
    
    
if answer > 15:
	print("The answer is {a:1.4f} for some weird reason. I used .format for this answer".format(a = answer))
else:
	print(f"Using fstring the answer is {answer:.3f}")
    
#You did well, they work every way. Try it out yourself if you don't believe me. 
#We'll do everything with if statements today

if answer > 3:
	print(f"{name} thinks {python}He is also", age , "years old.")
else:
	print(f"{god}will guide me along the way. InshaAllah")
    
#Let's try a random input. Hopefully it works InshaAllah.

import random

a = random.randrange(1,1000)

if a > 450:
	print(f"Holy it worked. {python}{god}is the greatest")
else:
	print(f"The random number is greater than 450. {name}is a {age} year old man trying his best")
	print(f"The random number is {a}")
    
#That worked I was able to create a dynamic condition. Hooray!
#Apply what you learned to your server. Make a script that will display CPU, USERS, and STATUS

import random

connections = random.randrange(1,100)
users = random.randrange(1,10)
status = random.randrange(0,2)
cpu = float(random.randrange(10,100))
media = "Plex"
up = "Online"
down = "Offline"

if connections > 0:
	print(f"Someone is watching {media}")
else:
	print(f"No one is watching {media}")
    
if users > 0:
	print(f"Active {users} users online")
else:
	print(f"Idle")
    
if status == 1:
	print(f"The {media} server is {up}")
else:
	print(f"The {media} server is {down}")
    
if cpu > 0:
	print(f"CPU usage {cpu:.3f}")
else:
	print(f"{cpu}")
    
#Let's mess around with loops. We have music playing Zensei & Delaney Kai - Sound Therapy
#Commands for loops and getting he loop
#Also for cleaner look (\n)to start a new line. Hint no parenthasis and no space
#The encoding didn't work

for x in god:
 	print(x)

print(len(python))

if a > 100:
	print(name.encode())
else:
	print(a)
    
print(name.upper())
  
