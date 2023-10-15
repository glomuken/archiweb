# Import necessary librariesfrom flask import Flask, request, jsonify,render_template

app = Flask(__name__)

# Define a dictionary of predefined responses (you can replace this with a more extensive knowledge base)
responses = {
    "hello": "Hello! How can I assist you today?",
    "crop_info": "Sure! Which crop are you interested in?",
    "pest_control": "To control pests, it's important to use proper pesticides and maintain good crop hygiene.",
    "weather_forecast": "You can check the weather forecast for your area on weather websites or apps.",
    "default": "I'm sorry, I don't understand. Please ask another question."
}

# Define a function to process user queries and return responses
def process_query(user_query):
    user_query = user_query.lower()
    if user_query in responses:
        return responses[user_query]
    else:
        return responses["default"]

# Define a route for receiving and responding to user queries
@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_message = request.json["message"]
    response = process_query(user_message)
    render_template("./chatai.html")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
    


