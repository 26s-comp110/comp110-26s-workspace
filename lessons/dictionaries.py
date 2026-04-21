"""Dictionaries"""

# Construct an empty dict

temps: dict[str, float] = dict()  # returns the literal
# or
temps: dict[str, float] = {}  # u dictsses curly brackets
# lists and sets use []


# Create a dictionary called ice_cream(Initialist a populated dictionary)


ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 5,
}  # only putting "" around keys bc they are strings


# Adding elements to dictionaries
# We do not use append to add to dictionaries
# We use subscription notation
# <dict name>[<key>]=<value>
ice_cream["mint"] = 3


# Removing elements
# <dict name>.pop(<key>)
ice_cream.pop("mint")

# To access a value, use subscription notation:
# <dict name>[<key>]
ice_cream["chocolate"]

# To modify also use subcribtion notation
ice_cream["vanilla"] = 10
# or
ice_cream["vanilla"] += 2

# len of dictioary
len(ice_cream)  # Telling you the amount of keys value pairs in the dict or len of dict

# check if key in dictionary
# <key> in <dict name>
print("choclate" in ice_cream)  # evaluate to booleans
print("mint" in ice_cream)
# If "mint" in ice_cream, print num orders

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint")
# print the dictionary
print(ice_cream)

# Important Note: Can't have multiple of the same key!


def grade_bump(gradebook: dict[str, str], student: str) -> None:
    # Find the student in the gradebook
    letter_grade: str = gradebook[student]  # Get student's letter grade
    if letter_grade == "A":
        gradebook[student] = "A+"  # Update grade
    else:
        gradebook[student] = "A"  # Update grade


grades: dict[str, str] = {"alyssa": "A", "luke": "B"}
grade_bump(grades, "luke")
print(grades)
grade_bump(grades, "luke")
print(grades)
print(ice_cream["pecan"])
