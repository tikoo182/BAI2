from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
from fuzzywuzzy import fuzz
from decimal import Decimal
import mysql.connector
import numpy as np
import torch
import spacy

def query_bai2(question):
    

    # Load the model and tokenizer

    new_model = AutoModelForSequenceClassification.from_pretrained("./bert")
    new_tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

    # BERT model predictor function
    
    def bert_classifier(text):

        encoding = new_tokenizer(text, return_tensors="pt", padding="max_length", truncation=True, max_length=128) 

        outputs = new_model(**encoding)

        logits = outputs.logits

        sigmoid = torch.nn.Sigmoid()

        probs = sigmoid(logits.squeeze().cpu())
        probs = probs.detach().numpy()
        label = np.argmax(probs, axis=-1)
            
        if label == 0:
            return {
                'label_text': "cl1",
                'probability': probs[0]
            }
        elif label == 1:
            return {
                'label_text': "cl2",
                'probability': probs[1]
            }
        elif label == 2:
            return {
                'label_text': "cl3",
                'probability': probs[2]
            }
        elif label == 3:
            return {
                'label_text': "ncl1",
                'probability': probs[3]
            }
        elif label == 4:
            return {
                'label_text': "ncl2",
                'probability': probs[4]
            }
        elif label == 5:
            return {
                'label_text': "ncl3",
                'probability': probs[5]
            }
        elif label == 6:
            return {
                'label_text': "ncl4",
                'probability': probs[6]
            }
        elif label == 7:
            return {
                'label_text': "ncl5",
                'probability': probs[7]
            }
        elif label == 8:
            return {
                'label_text': "ncl6",
                'probability': probs[8]
            }
        elif label == 9:
            return {
                'label_text': "ncl7",
                'probability': probs[9]
            }
        elif label == 10:
            return {
                'label_text': "ncl8",
                'probability': probs[10]
            }
        elif label == 11:
            return {
                'label_text': "ncl9",
                'probability': probs[11]
            }
        elif label == 12:
            return {
                'label_text': "ncl10",
                'probability': probs[12]
            }
        elif label == 13:
            return {
                'label_text': "ncl11",
                'probability': probs[13]
            }
        elif label == 14:
            return {
                'label_text': "ncl12",
                'probability': probs[14]
            }
        
        else:
            return None    

    # Spacy NER function

    def spacy_ner(question):

        nlp_ner = spacy.load("./spacy/model-best/")

        doc = nlp_ner(question)

        entity_dict = {}
        
        for ent in doc.ents:
            if ent.label_ in entity_dict:
                entity_dict[ent.label_].append(ent.text)
            else:
                entity_dict[ent.label_] = [ent.text]

        return entity_dict
    
    
    # Stores the results of the BERT model and Spacy NER in dictionaries

    bert_dict = bert_classifier(question)
    spacy_dict = spacy_ner(question)

    
    # Stores the results of the BERT model and Spacy NER in variables

    class_label = bert_dict['label_text']
    probability = bert_dict['probability']

    parameter = ""
    value = ""

    for k, v in spacy_dict.items():
        parameter = k.lower()
        value = v[0].lower()


    # Opens the parameter txt files in order to compare the values

    file_path_city = "training data/datasets/parameters NER/city.txt"
    file_path_countries = "training data/datasets/parameters NER/country.txt"
    file_path_customerName = "training data/datasets/parameters NER/customerName.txt"
    file_path_firstName = "training data/datasets/parameters NER/firstName.txt"
    file_path_lastName = "training data/datasets/parameters NER/lastName.txt"
    file_path_productLine = "training data/datasets/parameters NER/productLine.txt"
    file_path_status = "training data/datasets/parameters NER/status.txt"
    file_path_productName = "training data/datasets/parameters NER/productName.txt"


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


    # Bad Spelling Correction Function

    def fuzzy_match(original_strings, user_input):

        best_match = None
        best_ratio = 0
        threshold = 50

        for original_string in original_strings:
            ratio = fuzz.ratio(original_string.lower(), user_input.lower())
            if ratio >= threshold and ratio > best_ratio:
                best_match = original_string
                best_ratio = ratio
        
        return best_match
    
    
    # Query construction function

    query = ""

    def query_select(label):

        match label:
            case "ncl1":
                if parameter == "country":
                    param_corrected_value = fuzzy_match(countries, value)
                    if "each" in param_corrected_value:
                        query = "SELECT country, SUM(amount) AS totalPayments FROM payments INNER JOIN customers ON payments.customerNumber = customers.customerNumber GROUP BY country ORDER BY country;"
                    else:
                        query = "SELECT country, SUM(amount) AS totalPayments FROM payments INNER JOIN customers ON payments.customerNumber = customers.customerNumber WHERE country = '" + param_corrected_value + "';"

                elif parameter == "productline":
                    param_corrected_value = fuzzy_match(productLines, value)
                    if "each" in param_corrected_value:
                        query = "SELECT productLine, SUM(amount) AS totalPayments FROM payments INNER JOIN customers ON payments.customerNumber = customers.customerNumber INNER JOIN orders ON customers.customerNumber = orders.customerNumber INNER JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber INNER JOIN products ON orderdetails.productCode = products.productCode GROUP BY productLine ORDER BY productLine;"
                    else:
                        query = "SELECT productLine, SUM(amount) AS totalPayments FROM payments INNER JOIN customers ON payments.customerNumber = customers.customerNumber INNER JOIN orders ON customers.customerNumber = orders.customerNumber INNER JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber INNER JOIN products ON orderdetails.productCode = products.productCode WHERE productLine = '" + param_corrected_value + "';"
                else:
                    query = ""

            case "ncl2":
                if parameter == "city":
                    param_corrected_value = fuzzy_match(cities, value)
                    if "each" in param_corrected_value:
                        query = "SELECT city, COUNT(*) AS numOrders FROM orders INNER JOIN customers ON orders.customerNumber = customers.customerNumber GROUP BY city ORDER BY city;"
                    else:
                        query = "SELECT city, COUNT(*) AS numOrders FROM orders INNER JOIN customers ON orders.customerNumber = customers.customerNumber WHERE city = '" + param_corrected_value + "';"
                elif parameter == "customername":
                    param_corrected_value = fuzzy_match(customerNames, value)
                    if "each" in param_corrected_value:
                        query = "SELECT customerName, COUNT(*) AS numOrders FROM orders JOIN customers ON orders.customerNumber = customers.customerNumber GROUP BY customerName ORDER BY customerName;"
                    else:
                        query = "SELECT customerName, COUNT(*) AS numOrders FROM orders JOIN customers ON orders.customerNumber = customers.customerNumber WHERE customerName = '" + param_corrected_value + "';"
                else:
                    query = ""

            case "ncl3":
                if parameter == "productname":
                    param_corrected_value = fuzzy_match(productNames, value)
                    if "each" in param_corrected_value:
                        query = "SELECT productName, SUM(quantityOrdered) AS totalQuantityOrdered FROM orderdetails JOIN products on orderdetails.productCode = products.productCode GROUP BY productName ORDER BY productName;"
                    else:
                        query = "SELECT productName, SUM(quantityOrdered) AS totalQuantityOrdered FROM orderdetails JOIN products on orderdetails.productCode = products.productCode WHERE productName = '" + param_corrected_value + "';"
                elif parameter == "customername":
                    param_corrected_value = fuzzy_match(customerNames, value)
                    if "each" in param_corrected_value:
                        query = "SELECT customerName, SUM(quantityOrdered) AS totalQuantityOrdered FROM orderdetails INNER JOIN orders ON orderdetails.orderNumber = orders.orderNumber join customers on orders.customerNumber = customers.customerNumber GROUP BY customerName ORDER BY customerName;"
                    else:
                        query = "SELECT customerName, SUM(quantityOrdered) AS totalQuantityOrdered FROM orderdetails INNER JOIN orders ON orderdetails.orderNumber = orders.orderNumber join customers on orders.customerNumber = customers.customerNumber WHERE customerName = '" + param_corrected_value + "';"
                else:
                    query = ""

            case "ncl4":
                if parameter == "customername":
                    param_corrected_value = fuzzy_match(customerNames, value)
                    if "each" in param_corrected_value:
                        uery = "SELECT customerName, AVG(amount) AS avgPaymentAmount FROM payments join customers on payments.customerNumber = customers.customerNumber GROUP BY customerName ORDER BY customerName;"
                    else:
                        query = "SELECT customerName, AVG(amount) AS avgPaymentAmount FROM payments join customers on payments.customerNumber = customers.customerNumber WHERE customerName = '" + param_corrected_value + "';"
                else:
                    query = ""
            
            case "ncl5":
                if parameter == "productline":
                    param_corrected_value = fuzzy_match(productLines, value)
                    if "each" in param_corrected_value:
                        query = "SELECT productLine, COUNT(*) AS numProducts FROM products GROUP BY productLine ORDER BY productLine;"
                    else:
                        query = "SELECT productLine, COUNT(*) AS numProducts FROM products WHERE productLine = '" + param_corrected_value + "';"
                else:
                    query = ""
            
            case "ncl6":
                if parameter == "customername":
                    param_corrected_value = fuzzy_match(customerNames, value)
                    if "each" in param_corrected_value:
                        query = "SELECT customerName, SUM(quantityOrdered * priceEach) AS totalSalesRevenue FROM orderdetails INNER JOIN orders ON orderdetails.orderNumber = orders.orderNumber inner join customers on orders.customerNumber = customers.customerNumber GROUP BY customerName ORDER BY customerName;"
                    else:
                        query = "SELECT customerName, SUM(quantityOrdered * priceEach) AS totalSalesRevenue FROM orderdetails INNER JOIN orders ON orderdetails.orderNumber = orders.orderNumber inner join customers on orders.customerNumber = customers.customerNumber WHERE customerName = '" + param_corrected_value + "';"
                elif parameter == "city":
                    param_corrected_value = fuzzy_match(cities, value)
                    if "each" in param_corrected_value:
                        query = "SELECT city, SUM(quantityOrdered * priceEach) AS totalSalesRevenue FROM orderdetails INNER JOIN orders ON orderdetails.orderNumber = orders.orderNumber inner join customers on orders.customerNumber = customers.customerNumber GROUP BY city ORDER BY city;"
                    else:
                        query = "SELECT city, SUM(quantityOrdered * priceEach) AS totalSalesRevenue FROM orderdetails INNER JOIN orders ON orderdetails.orderNumber = orders.orderNumber inner join customers on orders.customerNumber = customers.customerNumber WHERE city = '" + param_corrected_value + "';"
                else:
                    query = ""

            case "ncl7":
                if parameter == "country":
                    param_corrected_value = fuzzy_match(countries, value)
                    if "each" in param_corrected_value:
                        query = "SELECT country, AVG(creditLimit) AS avgCreditLimit FROM customers GROUP BY country ORDER BY country;"
                    else:
                        query = "SELECT country, AVG(creditLimit) AS avgCreditLimit FROM customers WHERE country = '" + param_corrected_value + "';"
                else:
                    query = ""

            case "ncl8":
                if parameter == "status":
                    param_corrected_value = fuzzy_match(statuses, value)
                    if "each" in param_corrected_value:
                        query = "SELECT status, COUNT(*) AS numOrders FROM orders GROUP BY status ORDER BY status;"
                    else:
                        query = "SELECT status, COUNT(*) AS numOrders FROM orders WHERE status = '" + param_corrected_value + "';"
                else:
                    query = ""

            case "ncl9":
                if parameter == "productline":
                    param_corrected_value = fuzzy_match(productLines, value)
                    if "each" in param_corrected_value:
                        query = "SELECT productLine, SUM(quantityOrdered) AS totalQuantitySold FROM orderdetails INNER JOIN products ON orderdetails.productCode = products.productCode GROUP BY productLine ORDER BY productLine;"
                    else:
                        query = "SELECT productLine, SUM(quantityOrdered) AS totalQuantitySold FROM orderdetails INNER JOIN products ON orderdetails.productCode = products.productCode WHERE producLine = '" + param_corrected_value + "';"
                else:
                    query = ""

            case "ncl10":
                if parameter == "customername":
                    param_corrected_value = fuzzy_match(customerNames, value)
                    if "each" in param_corrected_value:
                        query = "SELECT customerName, COUNT(*) AS numPayments FROM payments inner join customers on payments.customerNumber = customers.customerNumber GROUP BY customerName ORDER BY customerName;"
                    else:
                        query = "SELECT customerName, COUNT(*) AS numPayments FROM payments inner join customers on payments.customerNumber = customers.customerNumber WHERE producLine = '" + param_corrected_value + "';"
                elif parameter == "firstname":
                    param_corrected_value = fuzzy_match(firstNames, value)
                    if "each" in param_corrected_value:
                        query = "SELECT firstName, COUNT(*) AS numPayments FROM payments inner join customers on payments.customerNumber = customers.customerNumber inner join employees on customers.salesRepEmployeeNumber = employees.employeeNumber GROUP BY firstName ORDER BY firstName;"
                    else:
                        query = "SELECT firstName, COUNT(*) AS numPayments FROM payments inner join customers on payments.customerNumber = customers.customerNumber inner join employees on customers.salesRepEmployeeNumber = employees.employeeNumber WHERE firstName = '" + param_corrected_value + "';"
                elif parameter == "lastname":
                    param_corrected_value = fuzzy_match(lastNames, value)
                    if "each" in param_corrected_value:
                        query = "SELECT lastName, COUNT(*) AS numPayments FROM payments inner join customers on payments.customerNumber = customers.customerNumber inner join employees on customers.salesRepEmployeeNumber = employees.employeeNumber GROUP BY lastName ORDER BY lastName;"
                    else:
                        query = "SELECT lastName, COUNT(*) AS numPayments FROM payments inner join customers on payments.customerNumber = customers.customerNumber inner join employees on customers.salesRepEmployeeNumber = employees.employeeNumber WHERE lastName = '" + param_corrected_value + "';"
                else:
                    query = ""
            
            case "ncl11":
                if parameter == "productline":
                    param_corrected_value = fuzzy_match(productLines, value)
                    if "each" in param_corrected_value:
                        query = "SELECT productLine, AVG(buyPrice) AS avgBuyPrice FROM products GROUP BY productLine ORDER BY productLine;"
                    else:
                        query = "SELECT productLine, AVG(buyPrice) AS avgBuyPrice FROM products WHERE productLine = '" + param_corrected_value + "';"
                else:
                    query = ""
            
            case "ncl12":
                if parameter == "productname":
                    param_corrected_value = fuzzy_match(productNames, value)
                    if "each" in param_corrected_value:
                        query = "SELECT productName, AVG(priceEach) AS avgPricePerUnit FROM orderdetails join products on orderdetails.productCode = products.productCode GROUP BY productName ORDER BY productName;"
                    else:
                        query = "SELECT productName, AVG(priceEach) AS avgPricePerUnit FROM orderdetails join products on orderdetails.productCode = products.productCode WHERE productName = '" + param_corrected_value + "';"
                else:
                    query = ""
            
            case "cl1":
                query = "SELECT customerName, creditLimit FROM customers ORDER BY creditLimit DESC LIMIT 10;"
            
            case "cl2":
                query = "SELECT productLine, MAX(quantityInStock) AS highestQuantityInStock FROM products GROUP BY productLine ORDER BY productLine;"
            
            case "cl3":
                query = "SELECT productLine, productName, MSRP FROM products WHERE (productLine, MSRP) IN (SELECT productLine, MAX(MSRP) FROM products GROUP BY productLine) ORDER BY productLine;"
    
        return query
    

    # Returns query

    query = query_select(class_label)


    # Verify if query is empty

    if len(query) == 0:
        result_list = [{'whooooops!': "Question Not Supported Yet!"}]

    else:

        # Connection parameters to MySQL

        conn = mysql.connector.connect(
            host='localhost',
            user='gabriel_sql',
            password='mynewpassword',
            database='classicmodels'
        )

        # Execute the query

        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()


        # Get column names

        column_names = [column[0] for column in cursor.description]

        result_list = []
        for row in results:
            result_dict = dict(zip(column_names, row))
            for k, v in result_dict.items():
                if isinstance(v, Decimal):
                    result_dict[k] = float(v)
                else:
                    result_dict[k] = v

            result_list.append(result_dict)
            

        # Close the cursor and connection
        
        cursor.close()
        conn.close()

    return result_list