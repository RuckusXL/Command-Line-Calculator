#DAY 3 Continued

print("Python Day 3".upper())

name = "Hadi"
age = 1000
a = 100
b = 1
d = "HELL YEA"
e = "AWW MAN"
music = "Zensei - Stay"
omg = "AllahSWT"
server = "Plex"
status = ("Online", "Offline")
x, y = status
free = "Everybody loves free!"
games = "Learning Python is my new game?"
message = "You are loved. Even when times are hard and you feel alone, you are not alone. \nI love you and I always will love you. This quote stuck with me and I want to share it with you. \n'If one million people love you I am one of them. \nIf one person loves you, then it's me. \nIf no one loves you, then I am dead'"

def praise():
	return(f"{omg} from a function!")
    
c = praise()

import random
numbers = random.randrange(1,1000000)
users = random.randrange(1,20)



print(f"My name is {name} and I am {age} years old. I started learning coding 2 days ago. \nI haven't played any games in a while since learning. Coding is all I want to do. {games} It's also free. \n{free}")

if a > b:
	txt = message
else:
	txt = free
    
print(f"{txt}")

#Simulated monitoring tool

print("---- SERVER REPORT ----")

print(f"Server: {server}")

if numbers > 10000:
    server_status = x
else:
    server_status = y

print(f"Status: {server_status}")

if users > 1:
    print(f"Users: {users} active")
else:
    print("Users: Idle")

print(f"Connections: {numbers}")

print(f"CPU Load: {numbers % 100}%")  # fake but more realistic idea

print("-----------------------")

if "Online" in server_status:
	congrat = d
else:
	congrat = e
    
print(f"{congrat}")

accounts = ["Admin", "Guest", "Root"]

for account in accounts:
	print(account)
