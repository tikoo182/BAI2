import json
import random
import re


# Open the text files containing the questions

with open("datasets/questions_cl.txt", "r") as file:
    questions_cl = file.read().splitlines()
file.close()

with open("datasets/questions_ncl.txt", "r") as file:
    questions_ncl = file.read().splitlines()
file.close()

questions = questions_cl + questions_ncl


# Create the json files

data_train = []
data_val = []

for question in questions:
    values = question.split("%")
    cl = values[1]

    match = re.search(r'\d+', cl)
    extracted_integer = int(match.group())

    if 'n' in values[1]:
        label = extracted_integer + 2
    else:
        label = extracted_integer -1
    
    rand = random.randint(1, 100)
    
    if rand < 80:
        data_train.append({
            "text": values[0],
            "label": label,
            "label_text": values[1]
        })
    
    else:
        data_val.append({
            "text": values[0],
            "label": label,
            "label_text": values[1]
        })

# Save the json files

train_file_path = "bert data/training_data_BERT_Classifier.json"
with open(train_file_path, "w") as json_train:
    json.dump(data_train, json_train, indent=2)

val_file_path = "bert data/validation_data_BERT_Classifier.json"
with open(val_file_path, "w") as json_val:
    json.dump(data_val, json_val, indent=2)

print("files saved successfully.")
