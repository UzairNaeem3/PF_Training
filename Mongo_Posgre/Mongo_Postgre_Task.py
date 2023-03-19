import os
from zipfile import ZipFile

import pymongo
from flask import Flask, request, render_template, jsonify
import psycopg2
from embeddings import get_embeddings
from pymongo import MongoClient
import gridfs

# PostgresSQL Table creation
try:
    # Connect to the PostgresSQL database
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="0321",
        host="localhost",
        port="5432"
    )

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS postgres_db')

    # Define the SQL query to create a table
    create_table_query = '''CREATE TABLE IF NOT EXISTS postgres_db
          (ID SERIAL PRIMARY KEY     NOT NULL,
          NAME           VARCHAR(40)   NOT NULL,
          EMBEDDING      VARCHAR    NOT NULL,
          PATH           VARCHAR) '''

    # Execute the SQL query
    cursor.execute(create_table_query)

    # Commit the changes to the database
    conn.commit()

    print("Table created successfully in PostgresSQL Database!")

except Exception as error:
    print(error)

app = Flask(__name__)


@app.route('/')
def html_form():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Check if file was uploaded
        if 'file' not in request.files:
            return 'No file selected'

        file = request.files['file']
        # Check if file has a valid name and extension
        if file.filename == '':
            return 'No file selected'
        if not file.filename.endswith('.zip'):
            return 'Invalid file type'

        # Create directory to extract contents of zip file
        folder_name = 'uploads'
        os.makedirs(folder_name, exist_ok=True)
        # Extract zip file contents to directory
        with ZipFile(file, 'r') as z:
            z.extractall('uploads')

        return f'Successfully saved {file.filename} to {folder_name} directory!'


@app.route('/get_image_data', methods=['GET'])
def get_image_data():
    images_dir = 'uploads'
    image_data = []

    for subdir, dirs, files in os.walk(images_dir):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                image_path = os.path.join(subdir, file)
                image_name = os.path.splitext(file)[0]
                image_data.append({
                    'name': image_name,
                    'path': image_path
                })

    return jsonify(image_data)


@app.route('/fetch_data_and_insert', methods=['GET'])
def fetch_data_and_insert():
    folder_path = "./uploads"

    data = []
    embed = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                image_path = os.path.join(root, file)
                image_name = os.path.splitext(file)[0]
                data.append((image_name, image_path))
                embeddings = get_embeddings(image_path)
                embed.append(embeddings)

    # Insert data into database
    for i, (image_name, image_path) in enumerate(data):
        try:
            insert_script = 'INSERT INTO postgres_db (NAME, PATH, EMBEDDING) VALUES (%s, %s, %s)'
            insert_value = (image_name, image_path, str(embed[i]))
            cursor.execute(insert_script, insert_value)
            conn.commit()
        except:
            conn.rollback()
            print("Error inserting data for image:", image_name)

    # Close the database connection
    cursor.close()
    conn.close()

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["dummy"]

    # Create a new GridFS object
    fs = gridfs.GridFS(db, collection="full_images")

    # Insert metadata for each image into the "data" collection
    data_coll = db["data"]
    image_data = [
        {"filename": "arslan.jpg", "filepath": r"E:\Mongo_Posgre\uploads\test\arslan.jpg"},
        {"filename": "baboon.png", "filepath": r"E:\Mongo_Posgre\uploads\test\baboon.png"},
        {"filename": "female.jpg", "filepath": r"E:\Mongo_Posgre\uploads\test\female.jpg"},
        {"filename": "hassan.jpg", "filepath": r"E:\Mongo_Posgre\uploads\test\hassan.jpg"},
        {"filename": "male.png", "filepath": r"E:\Mongo_Posgre\uploads\test\male.png"},
        {"filename": "rebecca.jpg", "filepath": r"E:\Mongo_Posgre\uploads\test\rebecca.jpg"},
    ]

    for image in image_data:
        with open(image["filepath"], "rb") as f:
            # Upload the file to GridFS
            file_id = fs.put(f, filename=image["filename"])
            print(f"Uploaded {image['filename']} with ID {file_id}")

        metadata = {"filename": image["filename"], "file_id": file_id}
        metadata.update(image.get("metadata", {}))
        data_coll.insert_one(metadata)

    return "Data fetched and inserted into the database successfully!"


if __name__ == '__main__':
    app.run(debug=True)
