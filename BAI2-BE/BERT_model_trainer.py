from transformers import AutoModelForSequenceClassification
from transformers import TrainingArguments, Trainer
from transformers import AutoTokenizer
import pandas as pd
import json
import pyarrow as pa
from datasets import Dataset


# Open the json files containing the data 

file_path = "training data/bert data/training_data_BERT_Classifier.json"
with open(file_path, 'r', encoding='utf-8') as file:
    train = json.load(file)

file_path = "training data/bert data/validation_data_BERT_Classifier.json"
with open(file_path, 'r', encoding='utf-8') as file:
    val = json.load(file)


# Convert the json files to pandas dataframes

train_pdf = pd.DataFrame(train)
val_pdf = pd.DataFrame(val)


# Creates a tokenizer for the BERT model

tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')


# Function to add the label to the data and tokenize the text

def process_data(row):

    text = str(row['text'])
    text = ' '.join(text.split())

    # Use max_length 512 for better presicion
    encodings = tokenizer(text, padding="max_length", truncation=True, max_length=128)


    label = row['label']

    encodings['label'] = label
    encodings['text'] = text

    return encodings


# Process the data

processed_data_train = []

for i in range(len(train_pdf)):
    processed_data_train.append(process_data(train_pdf.iloc[i]))

processed_data_val = []

for i in range(len(val_pdf)):
    processed_data_val.append(process_data(val_pdf.iloc[i]))


# Transform the list of dictionaries to a pandas dataframe

train_df = pd.DataFrame(processed_data_train)
valid_df = pd.DataFrame(processed_data_val)

# Transform the pandas dataframe to a pyarrow table
train_hg = Dataset(pa.Table.from_pandas(train_df))
valid_hg = Dataset(pa.Table.from_pandas(valid_df))


# Creates the model and trains it

model = AutoModelForSequenceClassification.from_pretrained(
    'bert-base-uncased',
    num_labels=15
)

training_args = TrainingArguments(output_dir="./bert_result", evaluation_strategy="epoch")

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_hg,
    eval_dataset=valid_hg,
    tokenizer=tokenizer
)


trainer.train()