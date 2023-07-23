###########################################################################
### COP 4045 - Python Programming - Dr. Oge Marques - FAU - Summer 2021 ###
###            Assignment 1: Student Introduction (in Python!)          ###
###########################################################################

name = "Carlos Sanchez"
academic_status = {"major": "Computer Science", "gpa": 3.2}
hobbies = ['Playing instruments', 'Rock climbing', 'playing soccer']

likes = "My hobbies are: \n"
for hobby in hobbies:
    likes = likes + hobby + "\n"

if academic_status['gpa'] == 4.0:
    rating = "perfect"
elif  academic_status['gpa'] >= 3.0:
    rating = "very good"
else:
    rating = "not-so-good"

print(f"My name is {name} \n")
print(f"I am majoring in {academic_status['major']} and my GPA is {academic_status['gpa']}, which is considered {rating}\n")
print(likes)
