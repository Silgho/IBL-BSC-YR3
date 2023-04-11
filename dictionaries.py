#student = ["Kelvin", "Sheldon", "Brian", "John","Joy"]
#estates = ["Kasarani", "Exit 9" , "Syokimau", "Kayole", "Ngara"]

students = {
    "Kelvin": "Kasarani",
    "Sheldon": "Exit 9",
    "Brain": "Syokimau",
    "John": "Kayole",
    "Joy": "Ngara"
}

print(students["Kelvin"])
print(students)

for student in students:
    print(student, students[student])