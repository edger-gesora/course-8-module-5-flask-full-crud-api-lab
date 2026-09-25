# Flask Full CRUD RESTful API

A simple event management REST API built with Python and Flask.

## Endpoints

* **GET /** - Welcome message
* **GET /events** - Retrieve all events
* **POST /events** - Create a new event (expects JSON with a `title`)
* **PATCH /events/<id>** - Update an event title
* **DELETE /events/<id>** - Remove an event by ID