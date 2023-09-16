from flask import Flask, render_template, request, redirect, url_for
import csv
from datetime import datetime

app = Flask(__name__)

# Function to calculate the number of years a mobile has been used
def calculate_years_used(purchase_year):
    current_year = datetime.now().year
    return current_year - int(purchase_year)

# Route for the homepage
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        purchase_year = request.form['purchase_year']
        future_model = request.form['future_model']

        # Calculate years used
        years_used = calculate_years_used(purchase_year)

        # Save data to CSV
        with open('data.csv', 'a', newline='') as csvfile:
            fieldnames = ['Brand', 'Model', 'Purchase Year', 'Years Used', 'Future Model']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Check if the CSV file is empty, if so, write the header
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'Brand': brand, 'Model': model, 'Purchase Year': purchase_year, 'Years Used': years_used, 'Future Model': future_model})

        return redirect(url_for('index'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
