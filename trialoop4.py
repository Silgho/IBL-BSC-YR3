class person:
    number_of_people = 0
    
    def __init__(self, name):
        self.name = name
        person.number_of_people += 1

p1 = person("Tim")
print(person.number_of_people)
p2 = person("Jill")
print(person.number_of_people)
p3 = person("Joy")
print(person.number_of_people)

