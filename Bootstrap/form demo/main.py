from flask import Flask, render_template, jsonify, json, request, redirect, url_for
import os

app = Flask(__name__, template_folder="templates")

# Route for the homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route for the about page
@app.route("/about/", methods=["GET"])
def about():
    return render_template("about.html")

# Route to display the form
@app.route("/form/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Redirect to submit route on form submission
        return redirect(url_for("submit"))
    return render_template("form.html")

# Route to handle form submission
@app.route("/submit/", methods=["POST"])
def submit():
    # Get user input from the form
    user_data = {
        "name": request.form.get("name"),
        "city": request.form.get("city"),
        "age": request.form.get("age")
    }

    # Save data into JSON file
    file_path = "user_data.json"
    if not os.path.exists(file_path):  # Create the file if it doesn't exist
        with open(file_path, "w") as user_file:
            json.dump([], user_file)

    # Append new data to the JSON file
    with open(file_path, "r+") as user_file:
        data = json.load(user_file)  # Load existing data as a list
        data.append(user_data)  # Append new data
        user_file.seek(0)  # Reset file pointer to the beginning
        json.dump(data, user_file, indent=4)  # Write updated data

    # Return a response to the user
    return jsonify({"message": "Data saved successfully!"})

# Route to display data
@app.route("/data/", methods=["GET"])
def data():
    # Read data from JSON file
    file_path = "user_data.json"
    if not os.path.exists(file_path):  # Handle missing file
        return jsonify({"error": "No data available!"})

    with open(file_path, "r") as user_file:
        try:
            user_data = json.load(user_file)
        except json.JSONDecodeError:
            return jsonify({"error": "Error reading data!"})

    # Return data as JSON
    return jsonify(user_data)


if __name__ == "__main__":
    app.run(debug=True)
