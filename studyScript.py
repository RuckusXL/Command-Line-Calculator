#This script is meant for trying out new functions as I learn them

#my_list = [1, 2, 3, 4, 5]
#print(len(my_list))
#my_list.append(6)
#print(my_list)


def check_password(password):
    if len(password) < 8:
        return "Too short"

    for char in password:
        if char.isdigit():
            return "Password is strong"

    return "Password must include a number"


def count_vowels(word):
    count = 0

    for char in word:
        if char.lower() in "aeiou":
            count += 1
    return count
        
def longest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

print(check_password("pasjdfhi22esd"))
#print(count_vowels("hello world"))
#print(longest_word("The quick brown fox jumps over the lazy dog"))