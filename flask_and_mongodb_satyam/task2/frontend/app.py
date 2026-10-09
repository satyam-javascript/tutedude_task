import os
from flask import Flask, jsonify, request, render_template # type: ignore
from flask.cli import load_dotenv
from datetime import datetime
import requests

BACKEND_URI = 'http://localhost:5000'  # Replace with your backend URI
app = Flask(__name__)




@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():

    if request.method == 'POST':
        form_data = dict(request.form)


        # Validate name
        name = form_data.get("name", "").strip()

        if not name:
            return render_template(
                'form.html',
                error="Name is required.",
                form_data=form_data
            )

        if any(char.isdigit() for char in name):
            return render_template(
                'form.html',
                error="Name cannot contain numbers.",
                form_data=form_data
            )

        response = requests.post(
            f"{BACKEND_URI}/submit",
            json=form_data
        )

        response_data = response.json()

        # Backend returned an error
        if "error" in response_data:
            return render_template(
                'submit.html',
                error=response_data["error"],
                form_data=form_data
            )

        # Backend succeeded
        return render_template(
            'success.html',
            response=response_data
        )

    return render_template('form.html',error=response_data["error"],
                    form_data=form_data)

#view all data from the collection
@app.route('/view', methods=['GET'])
def view_data():
    data = requests.get(f"{BACKEND_URI}/view")  # Exclude the '_id' field from the results
    return  render_template('view.html', data=data.json())
 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9000)