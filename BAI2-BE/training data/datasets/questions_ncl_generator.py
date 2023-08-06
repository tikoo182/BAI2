
# Parameter txt files

file_path_city = "parameters NER/city.txt"
file_path_countries = "parameters NER/country.txt"
file_path_customerName = "parameters NER/customerName.txt"
file_path_firstName = "parameters NER/firstName.txt"
file_path_lastName = "parameters NER/lastName.txt"
file_path_productLine = "parameters NER/productLine.txt"
file_path_status = "parameters NER/status.txt"
file_path_productName = "parameters NER/productName.txt"


# Questions txt file

file_path_questions_NER = "parameters NER/questions_NER.txt"


# Read the txt files

with open(file_path_questions_NER, "r") as file:
    questions = file.read().splitlines()
file.close()

with open(file_path_city, "r") as file:
    cities = file.read().splitlines()
file.close()

with open(file_path_countries, "r") as file:
    countries = file.read().splitlines()
file.close()

with open(file_path_customerName, "r") as file:
    customerNames = file.read().splitlines()
file.close()

with open(file_path_firstName, "r") as file:
    firstNames = file.read().splitlines()
file.close()

with open(file_path_lastName, "r") as file:
    lastNames = file.read().splitlines()
file.close()

with open(file_path_productLine, "r") as file:
    productLines = file.read().splitlines()
file.close()

with open(file_path_status, "r") as file:
    statuses = file.read().splitlines()
file.close()

with open(file_path_productName, "r") as file:
    productNames = file.read().splitlines()
file.close()


# Replace the parameters in the questions

questions2 = []
for question in questions:
    if "{city}" in question:
        for city in cities:
            new = question.replace("{city}", city)
            questions2.append(new)
    else:
        questions2.append(question)

questions3 = []
for question in questions2:
    if "{country}" in question:
        for country in countries:
            new = question.replace("{country}", country)
            questions3.append(new)
    else:
        questions3.append(question)

questions4 = []
for question in questions3:
    if "{customerName}" in question:
        for customerName in customerNames:
            new = question.replace("{customerName}", customerName)
            questions4.append(new)
    else:
        questions4.append(question)

questions5 = []
for question in questions4:
    if "{firstName}" in question:
        for firstName in firstNames:
            new = question.replace("{firstName}", firstName)
            questions5.append(new)
    else:
        questions5.append(question)

questions6 = []
for question in questions5:
    if "{lastName}" in question:
        for lastName in lastNames:
            new = question.replace("{lastName}", lastName)
            questions6.append(new)
    else:
        questions6.append(question)

questions7 = []
for question in questions6:
    if "{productLine}" in question:
        for productLine in productLines:
            new = question.replace("{productLine}", productLine)
            questions7.append(new)
    else:
        questions7.append(question)

questions8 = []
for question in questions7:
    if "{status}" in question:
        for status in statuses:
            new = question.replace("{status}", status)
            questions8.append(new)
    else:
        questions8.append(question)

questions9 = []
for question in questions8:
    if "{productName}" in question:
        for productName in productNames:
            new = question.replace("{productName}", productName)
            questions9.append(new)
    else:
        questions9.append(question)


# Write the questions to a txt file

with open("questions_ncl.txt", "w") as file:
    for item in questions9:
        file.write(item + "\n")