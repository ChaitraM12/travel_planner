from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/destination/<destination_id>')
def destination(destination_id):
    # Retrieve destination details from a database or external API
    # For simplicity, use static data
    destination_data = {
        'id': destination_id,
        'name': 'Example Destination',
        'description': 'A beautiful place to visit.',
        'activities': ['Sightseeing', 'Hiking', 'Shopping']
    }
    return render_template('destination.html', destination=destination_data)

@app.route('/plan', methods=['POST'])
def plan():
    # Handle form submission for travel planning
    destination_id = request.form.get('destination_id')
    # Perform additional logic (e.g., booking, scheduling) based on user input
    return redirect(url_for('destination', destination_id=destination_id))

if __name__ == '__main__':
    app.run(debuTrue)
