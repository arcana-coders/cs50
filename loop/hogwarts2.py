students = [
    {"name": "Hermione", "house": "Gryffindor", "patrouns": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patrouns": "Stag"},     
    {"name": "Ron", "house": "Gryffindor", "patrouns": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patrouns": None}
]

for student in students:
    print(student["name"], student["house"], student["patrouns"], sep=", ")