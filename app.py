from flask import Flask, request, jsonify
 
app = Flask(__name__)
 

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    print("Received a GET request for verification")
    verify_token = "dnfdnfj"
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if token == verify_token:
        print("Success")
        return challenge, 200
    else:
        return "Token verification failed", 403
 

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    print("Webhook POST request received", flush=True)     
    try:
        data = request.get_json() 
        if not data:
            print(f"No JSON data received, raw data: {request.data}", flush=True)  
        else:
            print(f"Received webhook event: {data}",flush=True)
        return "Event received", 200
    except Exception as e:
        print(f"Error processing webhook: {e}", flush=True)
        return "Internal server error", 500
 
@app.route('/test', methods=['GET'])
def test_route():
    print("Test route hit", flush=True)
    return "Test route working", 200
  
@app.route('/')
def home():
    return "Hello, Flask is running on Glitch!"
 
if __name__ == '__main__':
    app.run()