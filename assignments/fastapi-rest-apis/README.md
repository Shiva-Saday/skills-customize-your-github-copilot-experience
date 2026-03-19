# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will learn how to build a simple REST API using the FastAPI framework. They will practice creating endpoints, handling request data, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create Basic API Endpoints

#### Description
Build a FastAPI application with endpoints that allow users to view API information and retrieve a list of resources.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Add a root endpoint that returns a welcome message
- Add a GET endpoint that returns a list of items as JSON
- Run successfully with Uvicorn and respond without errors


### 🛠️ Add CRUD-Style Behavior

#### Description
Expand the API so users can add and retrieve individual items using request parameters or request bodies.

#### Requirements
Completed program should:

- Add a POST endpoint to create a new item
- Add a GET endpoint that returns one item by its ID
- Validate incoming data using a Pydantic model
- Return clear JSON responses for both successful requests and missing items