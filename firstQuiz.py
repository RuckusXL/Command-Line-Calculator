#First quiz
#The structure of this script will assign variables to lists then create functions that will ask the user questions and respond accordingly. The functions will be called at the end of the script to run the quiz. The quiz will be a series of questions that will ask the user about their name, age, mood, and hobbies. The responses will be based on the user's input and will provide different responses based on the answers given. The quiz will also include a function that will provide website links if the user is feeling down. The quiz will end with a question about taking over the world and a response based on the user's answer.
#Variables will be set prior to answers to play with unpacking lists and tuples.
#In theory its seems simple like the same command over again. Seems like it would depend on the complexity of the response.
#Author: RuckusXL

admin = "Hadi", "Marissa", "Tony"
craft = "coding", "gaming", "drawing", "working out", "movies", "cars" 
food = "pizza", "burgers", "sushi", "tacos", "pasta"

#This function will ask the user for their name and check if they are an admin. If they are an admin, it will welcome them as such. If not, it will greet them and offer assistance.
def ask_name():
	name = input("\n1. What is your name? ")
	
	if name.title() in admin:
		print("\n---Welcome! You are an admin.---".upper())
	else:
		print("\n---Hello, we will assist you as best we can.---".upper())
    	
	return name

#This function will ask the user for their age and respond accordingly. If they are over 30, it will ask if they feel old. If they are under 30, it will ask if telling them to leave would get rid of them.
def ask_age():
	age = int(input("\n2. How old are you? "))
	
	if age > 30:
		youth = input("\n3. Do you feel old yet? ")
	else:
		youth = input("\n3. You're not old enough to be here. Would telling you to leave get rid of you? ")

	return youth

#This function will ask the user how they are feeling and respond accordingly. If they are feeling great, it will acknowledge that. If not, it will offer good vibes and provide some links if they want them.
def ask_mood():
	mood = input("\n4. How are you feeling today? ")
	
	if "great" in mood.lower():
		print("\n---That's awesome to hear!---".upper())
	else:
		vibes = input("\n5. Sorry to hear that. Would you like some good vibes? ")
		if "yes" in vibes.lower():
			print("\n---Ok, try some of these =)---".upper())
			website_links()
		else:
			print("\n---We understand, we will be here if you need us.---".upper())

#This function will print out a list of website links for the user to check out if they are feeling down. The links are stored in a list and printed out one by one.
def website_links():
    links = [
        "\n---https://www.youtube.com/watch?v=89lK93r2AC4---",
        "---https://www.youtube.com/watch?v=9Deg7VrpHbM---",
        "---https://www.youtube.com/watch?v=Jy0Y0vMgiDM---"
    ]

    for link in links:
        
        print(link)

def favorite_food(food_list):
	food_choice = input("\nWhat is your favorite food? ")
	
	if food_choice.lower() in [item.lower() for item in food_list]:
		print(f"\n---Nice, {food_choice.title()} Party at my place?---".upper())
	else:
		food_list.append(food_choice)
		print(f"\n---We've never heard of {food_choice.title()} before, searching webs for information---".upper())
	
	return food_choice

ask_name()
ask_age()	
ask_mood()
favorite_food(food)

hobby = input("\n6. Do you have any hobbies? ")
rec = ""

if "yes" in hobby.lower():
	print("\n---HOLY NICE!!---".upper())
	bottle = input("\n7. Tell me one? ")
else:
	bottle = input("\n8. Would you like us to recommend one? ")

if bottle.lower() in craft:
	print(f"\n---Nice, that's a solid hobby. We like {bottle} as well---".upper())
else:
	rec = input("\n9. Do you like computers? ")

if "no" in rec.lower():
	print("\n---We can try learning coding?---".upper())
elif rec != "":
	print("\n---We are watching you closely---".upper())

cli = input("\n10. Are you comfortable with the command line? ")
kill = input("\n11. What is the command short cut to kill a process in the command line? ")

if kill == "ctrl c":
	print("\n---CORRECT----")
else:
	print("\n---LIAR LIAR---")

recruit = input("\n12. Tell me, would you like to takeover the world with us? ")

if "yes" in recruit.lower():
	print("\n---We knew they were wrong about you. We will be in contact with the next steps. Take Care.---".upper())
