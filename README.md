# BAI2
This repository houses a natural language question-answering platform that empowers users to interact with their business data effortlessly. Powered by Spacy NER and BERT models, BAI2 offers a lightweight and accurate solution for business intelligence tasks.


# BAI2 - Business Intelligence with AI

## Table of Contents
    1. Introduction
    2. How it Works
    3. Training Data
    4. Model Training
    5. Integration
    6. Front-end
    7. Libraries Used

## Introduction

### Project Purpose
BAI2, or Business Intelligence with AI, is a project that offers a user-friendly natural language interface, empowering users to interact with complex business data effortlessly. The purpose of BAI2 is to share a simple and efficient method for achieving this objective without the need for computationally intensive ML models, making it a valuable resource for BI enthusiasts and developers seeking lightweight NLP solutions.
### Key Features
    1. Simplified NLP Interface: BAI2 employs NLP models to comprehend user questions accurately, facilitating communication with the underlying data.
    2. Simple Data Visualization: Users can easily grasp data trends and patterns with visually appealing and interactive charts, such as bar charts and pie charts.
    3. Customized Querying: BAI2 offers parameterized queries, enabling users to personalize their data requests and receive tailored responses.
### Technology Stack
    • Front-end: Angular, TS
    • Back-end: FastAPI, uvicorn, Python, SQL
    • Machine Learning Models: BERT, Spacy
### Motivation
BAI2 was born from a simple idea suggested by the head of accounting at the firm. The motivation behind the project was to create a practical and accessible solution for customers to interact with their business data naturally. With a focus on efficiency and user experience. This inspired me to start building this project to show how this idea could be placed in action without the need of llms sush as GPT-4 or LLAMA2 which are very computational expensive to run. BAI2 empowers users to make well-informed decisions, benefiting their businesses.
### Learning Objectives
Throughout the development journey, BAI2 achieved essential learning objectives, including:
    • Gaining expertise in advanced NLP techniques and applying them to business-oriented applications.
    • Mastering data preprocessing, SQL query generation, and data visualization for meaningful business analytics.
    • Developing a robust and scalable web application tailored to BI use cases.

## How it Works
The project "BAI2" (Business Intelligence with AI) is designed to understand human natural language questions typed by users on a webpage and return data in a graph format based on the retrieved information. The system works through a series of interconnected steps:
    1. Front-end: Users input their questions through the web interface.
    2. Back-end: An HTTP request is sent from the front-end to the server.
    3. NLP Processing: The back-end processes the questions using Spacy NER and BERT text classification models to comprehend the type of question being asked.
    4. SQL Query: Based on the NLP model results, a SQL query is dynamically generated and executed on a MySQL server where the relevant data is stored.
    5. Data Presentation: The query results are then sent back to the front-end, where logical decisions are made to present the information appropriately. This may involve visualizing the data as a bar chart or displaying it in a simple KPI (Key Performance Indicator) index card.
    
## Training Data
The success of the NLP models used in this project heavily relies on appropriate training data. The training data consists of two main components:
    1. Questions: Predefined sample questions that users might ask the platform.
    2. Parameters: Datapoints in the SQL database, with variant questions generated for each class.
Both questions and parameters are stored in text files in the training data directory.

## Model Training
The model training process involves the following steps:
    1. questions_ncl_generator.py: This script generates variant questions from the predefined questions and parameters, saving them in text files.
    2. bert_json_generator.py and ner_json_generator.py: These scripts convert the generated text files into JSON format, which the model trainers can read.
    3. BERT_mode_trainer.py and NER_model_trainer.py: These scripts train the BERT text classification model and the Spacy NER model, respectively. The trained models are saved in the /bert_results and /spacy directories, respectively.
    
## Integration
The trained NLP models are integrated into the bai2.py file, which serves as the backbone of the back-end. The query_bai2 function in bai2.py is called whenever the front-end sends a question. The function utilizes the models' predictions to build the SQL query and returns the data as a JSON response to the Angular front-end using FastAPI and uvicorn.

## Front-end
The Angular front-end communicates with the back-end by making a GET request to extract the relevant information. Based on the retrieved data, the front-end applies logic in the HTML to determine whether to visualize the data as a bar chart or display it in a simple KPI index card.

## Libraries Used
The project utilizes the following libraries:
    • transformers (Version: 4.29.2)
    • pandas (Version: 2.0.3)
    • pyarrow (Version: 12.0.1)
    • datasets (Version: 2.13.1)
    • fuzzywuzzy (Version: 0.18.0)
    • mysql-connector-python (Version: 8.0.33)
    • numpy (Version: 1.24.3)
    • torch (Version: 2.0.1)
    • spacy (Version: 3.5.3)

