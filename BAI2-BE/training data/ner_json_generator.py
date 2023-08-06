import json

# Open the text files containing the questions

file_path_city = "datasets/parameters NER/city.txt"
file_path_countries = "datasets/parameters NER/country.txt"
file_path_customerName = "datasets/parameters NER/customerName.txt"
file_path_firstName = "datasets/parameters NER/firstName.txt"
file_path_lastName = "datasets/parameters NER/lastName.txt"
file_path_productLine = "datasets/parameters NER/productLine.txt"
file_path_status = "datasets/parameters NER/status.txt"
file_path_productName = "datasets/parameters NER/productName.txt"


# Save each parameter in its own list

with open("datasets/questions_ncl.txt", "r") as file:
    questions_raw = file.read().splitlines()
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

questions = []

for question in questions_raw:
    questions.append(question.split('%')[0])


# Create dictionaries to store the json data

data_train = []
data_val = []


# Substitute the parameters in the questions

for question in questions:

    for city in cities:

        if city in question:

            startIndex = question.find(city)
            endIndex = startIndex + len(city) - 1

            data_train.append({
                "text": question,
                "entities": [{
                    "startIndex": startIndex,
                    "endIndex": endIndex,
                    "tag": 'city'
                    }]
                })

for question in questions:

    for country in countries:

        if country in question:

            startIndex = question.find(country)
            endIndex = startIndex + len(country) - 1

            data_train.append({
                "text": question,
                "entities": [{
                    "startIndex": startIndex,
                    "endIndex": endIndex,
                    "tag": 'country'
                    }]
                })

for question in questions:

    for customerName in customerNames:

        if customerName in question:

            startIndex = question.find(customerName)
            endIndex = startIndex + len(customerName) - 1

            data_train.append({
                "text": question,
                "entities": [{
                    "startIndex": startIndex,
                    "endIndex": endIndex,
                    "tag": 'customerName'
                    }]
                })

for question in questions:

    for firstName in firstNames:

        if firstName in question:

            startIndex = question.find(firstName)
            endIndex = startIndex + len(firstName) - 1

            data_train.append({
                "text": question,
                "entities": [{
                    "startIndex": startIndex,
                    "endIndex": endIndex,
                    "tag": 'firstName'
                    }]
                })

for question in questions:

    for lastName in lastNames:

        if lastName in question:

            startIndex = question.find(lastName)
            endIndex = startIndex + len(lastName) - 1

            data_train.append({
                "text": question,
                "entities": [{
                    "startIndex": startIndex,
                    "endIndex": endIndex,
                    "tag": 'lastName'
                    }]
                })

for question in questions:

    for productLine in productLines:

        if productLine in question:

            startIndex = question.find(productLine)
            endIndex = startIndex + len(productLine) - 1

            data_train.append({
                "text": question,
                "entities": [{
                    "startIndex": startIndex,
                    "endIndex": endIndex,
                    "tag": 'productLine'
                    }]
                })

for question in questions:

    for status in statuses:

        if status in question:

            startIndex = question.find(status)
            endIndex = startIndex + len(status) - 1

            data_train.append({
                "text": question,
                "entities": [{
                    "startIndex": startIndex,
                    "endIndex": endIndex,
                    "tag": 'status'
                    }]
                })

for question in questions:

    for productName in productNames:

        if productName in question:

            startIndex = question.find(productName)
            endIndex = startIndex + len(productName) - 1

            data_train.append({
                "text": question,
                "entities": [{
                    "startIndex": startIndex,
                    "endIndex": endIndex,
                    "tag": 'productName'
                    }]
                })
            

# Save the json files

file_path = "ner spacy data/training_data_NER.json"
with open(file_path, "w") as json_train:
    json.dump(data_train, json_train, indent=2)

print("NER training file saved successfully.")