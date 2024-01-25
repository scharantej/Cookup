
# Import necessary modules
from flask import Flask, render_template, request, jsonify
import recipe_generator

# Create a Flask app
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    """
    Render the main page where users can input ingredients.
    """
    return render_template('index.html')

# Define the route to generate and display recipe results
@app.route('/results', methods=['POST'])
def results():
    """
    Generate a recipe using the ingredients provided by the user and display the result.
    """
    # Get the list of ingredients from the request
    ingredients = request.form.getlist('ingredient')

    # Generate a recipe using the ingredients
    recipe = recipe_generator.generate_recipe(ingredients)

    # Render the results page with the generated recipe
    return render_template('results.html', recipe=recipe)

# Define the API route to generate recipe data
@app.route('/api/v1/recipe', methods=['POST'])
def api_recipe():
    """
    Generate recipe data using the ingredients provided in JSON format.
    """
    # Get the list of ingredients from the request
    data = request.get_json()
    ingredients = data.get('ingredients')

    # Generate a recipe using the ingredients
    recipe = recipe_generator.generate_recipe(ingredients)

    # Return the recipe data in JSON format
    return jsonify(recipe)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
