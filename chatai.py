# Import necessary libraries
from flask import Flask, request, jsonify

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
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
    
<!DOCTYPE html>
<html>
<head>
    <title>Your Agricultural Website</title>
    <!-- Add your CSS styles here -->
</head>
<body>
    <h1>Welcome to Your Agricultural Website</h1>
    
    <!-- Add your website content here -->
    
    <div id="chat-container">
        <div id="chat-header">
            <h2>Chat with our Agricultural Assistant</h2>
        </div>
        <div id="chat-body">
            <div id="chat-messages"></div>
        </div>
        <div id="chat-input">
            <input type="text" id="user-input" placeholder="Type your message..." />
            <button id="send-button">Send</button>
        </div>
    </div>
    
    <!-- Add your JavaScript code here -->

</body>
</html>

<!-- Add this JavaScript code after the HTML content -->

<script>
    const chatMessages = document.getElementById("chat-messages");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");

    // Function to display a message in the chat window
    function displayMessage(text, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add(sender === "user" ? "user-message" : "bot-message");
        messageDiv.innerText = text;
        chatMessages.appendChild(messageDiv);
    }

    // Function to send user input to the chatbot server
    function sendMessage() {
        const userMessage = userInput.value;
        displayMessage(userMessage, "user");
        userInput.value = "";

        // Send a POST request to your chatbot server
        fetch("/chatbot", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: userMessage })
        })
        .then(response => response.json())
        .then(data => {
            const botResponse = data.response;
            displayMessage(botResponse, "bot");
        })
        .catch(error => {
            console.error("Error sending message:", error);
        });
    }

    // Handle button click or Enter key press to send the message
    sendButton.addEventListener("click", sendMessage);
    userInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
</script>


