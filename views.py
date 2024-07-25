from flask import Flask, render_template, request, redirect, url_for, send_file, abort, flash
from .services import GenAI
from google.cloud import firestore
import json
from .model import *
import pandas as pd
import os


app = Flask(__name__)
app.secret_key = 'this_is_my_secret_id'


"""
@app.route('/')
def home():
    return render_template('index.html')

# Ensure this route is named 'process_url' and accepts POST requests
@app.route('/process_url', methods=['POST'])
def process_url():
    # Get the URL from the form
    product_url = request.form['productUrl']
    # Process the URL or perform some action
    # For demonstration, just redirect to home
    product_json_data, product_gen_desc = GenAI.result_desc(product_url)
    print(product_json_data)
    
    return render_template('validatedata.html', json_data=product_json_data, generated_descriptions=product_gen_desc )


@app.route('/submit_description', methods=['POST'])
def submit_description():
    
    product_json_data_str = request.form.get('json_data')
    print(product_json_data_str)
    product_gen_desc = request.form.get('generated_descriptions')
    

    print("Calling extract function--------------------------------->")
    #product_json_data = GenAI.extract_json(product_json_data_str)
    product_json_data = GenAI.extract_json(str(product_json_data_str))
    print(product_json_data)

    insert_data(product_json_data, product_gen_desc)
    
    # Process the selected description
    # Redirect or return another template
    return redirect(url_for('home'))


@app.route('/display', methods=['GET'])
def display():
    products = get_data()  # Get the latest 10 products
    return render_template('display.html', products=products)



@app.route('/download_excel')
def download_excel():
    try:
        products = get_data()  # Fetch the products
        if not products:
            return "No data available to download.", 404

        # Identify all unique keys
        all_keys = set(key for product in products for key in product.keys())

        # Normalize the JSON objects to have the same keys in the same order
        normalized_products = []
        for product in products:
            normalized_product = {key: product.get(key, None) for key in all_keys}
            normalized_products.append(normalized_product)

        # Convert the normalized products to a DataFrame
        df = pd.DataFrame(normalized_products)

        # Directly determine the Downloads folder path
        home = os.path.expanduser("~")
        downloads_path = os.path.join(home, 'Downloads')
        filename = "products.xlsx"
        filepath = os.path.join(downloads_path, filename)  # Full path to save the file

        # Save the DataFrame to an Excel file in the Downloads folder
        df.to_excel(filepath, index=False)

        # Send the file to the user
        return send_file(filepath, as_attachment=True, download_name=filename)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return abort(500, description="Error generating Excel file.")

"""


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_url', methods=['POST'])
def process_url():
    try:
        product_url = request.form['productUrl']
        product_json_data, product_gen_desc = GenAI.result_desc(product_url)
        print(product_json_data)
        return render_template('validatedata.html', json_data=product_json_data, generated_descriptions=product_gen_desc)
    except Exception as e:
        print(f"Error processing URL: {e}")
        return abort(500, description="Error processing the URL.")

@app.route('/submit_description', methods=['POST'])
def submit_description():
    try:
        product_json_data_str = request.form.get('json_data')
        product_gen_desc = request.form.get('generated_descriptions')
        print("Calling extract function--------------------------------->")
        product_json_data = GenAI.extract_json(product_json_data_str)
        print(product_json_data)
        insert_data(product_json_data, product_gen_desc)
        flash('Data insertion was successful!', 'success')
        return redirect(url_for('home'))
    except Exception as e:
        print(f"Error submitting description: {e}")
        flash(f'Error submitting the product description: {e}', 'error')
        return abort(500, description="Error submitting the product description.")

@app.route('/display', methods=['GET'])
def display():
    try:
        products = get_data()  # Get the latest 10 products
        if not products:
            return "No products available.", 404
        return render_template('display.html', products=products)
    except Exception as e:
        print(f"Error displaying products: {e}")
        return abort(500, description="Error displaying products.")

@app.route('/download_excel')
def download_excel():
    try:
        products = get_data()  # Fetch the products
        if not products:
            return "No data available to download.", 404

        all_keys = set(key for product in products for key in product.keys())
        normalized_products = [{key: product.get(key, None) for key in all_keys} for product in products]
        df = pd.DataFrame(normalized_products)

        home = os.path.expanduser("~")
        downloads_path = os.path.join(home, 'Downloads')
        filename = "products.xlsx"
        filepath = os.path.join(downloads_path, filename)

        df.to_excel(filepath, index=False)
        return send_file(filepath, as_attachment=True, download_name=filename)
    except Exception as e:
        print(f"An error occurred while generating Excel: {e}")
        return abort(500, description="Error generating Excel file.")