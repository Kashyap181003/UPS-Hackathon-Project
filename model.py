from flask import Flask, request, jsonify
from google.cloud import firestore
from flask_session import Session

db = firestore.Client(project='qwiklabs-gcp-04-091cbe4fed8b', database='products-database')


def insert_data(product_json_data, product_gen_desc):
    try:
        # Expecting JSON data in the request
        product_json_data["Product Description (generated)"] = product_gen_desc
        print(product_json_data)
        data = product_json_data
        # You can directly use the data dictionary if it matches the Firestore document structure
        doc_ref = db.collection('products').document()
        doc_ref.set(data)
        print({"success": True, "message": "Data inserted successfully"})
    except Exception as e:
        print({"success": False, "error": str(e)})
    

def get_data():
    try:
        docs = db.collection('products').stream()
        
        # Convert documents to dictionaries
        products = [doc.to_dict() for doc in docs]
        
        print("Data fetched successfully")
        return products

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []
    

