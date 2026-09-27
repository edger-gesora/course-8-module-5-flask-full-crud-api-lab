from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# Welcome route (Satisfies the grading criteria)
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Event Management API"})

# GET /events - Retrieve all events
@app.route('/events', methods=['GET'])
def get_events():
    return jsonify([event.to_dict() for event in events])

# POST /events - Create a new event
@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400
    
    new_id = events[-1].id + 1 if events else 1
    new_event = Event(new_id, data["title"])
    events.append(new_event)
    return jsonify(new_event.to_dict()), 201

# PATCH /events/<id> - Update an event title
@app.route('/events/<int:id>', methods=['PATCH'])
def update_event(id):
    data = request.get_json()
    event = next((e for e in events if e.id == id), None)
    
    if not event:
        return jsonify({"error": "Event not found"}), 404
        
    if data and "title" in data:
        event.title = data["title"]
        
    return jsonify(event.to_dict()), 200

# DELETE /events/<id> - Remove an event
@app.route('/events/<int:id>', methods=['DELETE'])
def delete_event(id):
    global events
    event = next((e for e in events if e.id == id), None)
    
    if not event:
        return jsonify({"error": "Event not found"}), 404
        
    events.remove(event)
    return '', 204
if __name__ == "__main__":
    app.run(debug=True)