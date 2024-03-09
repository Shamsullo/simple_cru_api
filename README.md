# Test task: Simple CRUD API
[![codecov](https://codecov.io/gh/Shamsullo/simple_crud_api/main/graph/badge.svg)](https://codecov.io/gh/Shamsullo/simple_crud_api)

**Project Overview**

This Simple CRUD (Create, Read, Update, Delete) project is built with FastAPI, demonstrating a basic RESTful API that manages items. It uses an asynchronous approach with a PostgreSQL database backend, showcasing API creation, database integration, microservices design, and containerization by developing a small-scale RESTful API which simulates a simple document repository.

**Features**

- Create Items: Add new items with title, content, and status.
- Read Items: Fetch a list of items or a specific item by ID.
- Update Items: Modify existing items' title, content, or status.
- Delete Items: Remove items from the database.

**Technologies**

- FastAPI for the web framework
- SQLAlchemy with async support for ORM
- PostgreSQL as the database
- Pydantic for data validation
- Pytest for testing
- Docker for containerization

The documentation is structured to guide users through the installation process, understand the API endpoints.

**Installation and Running the Service**

1\. Clone the project from the GitHub repository

2\. create a .env where you need to fill environment variables. The example and the required fields are given in the .env.example

3\. run the project using docker: 

 ```bash
  docker-compose -f docker-compose.yml up --build -d
 ```

 the project will be available at http://localhost:8080

**Documentation**

More detailed API documentation can be found here, of course after starting the project: 

 - http://localhost:8080/api/docs (Swagger)

 - http://localhost:8080/api/re-docs (Redocs)


For testing purposes, I have deployed the service to the temporary server and it can be found here: http://3.77.154.109:8080/api/docs#/

**Continuous Integration (CI)**

The project includes a CI script setup to:
 - Run automated tests

 - Generate a code coverage report

 **Tests**
The API is covered with some basic test cases as an example using pytest. This command can run the test:

```bash
  docker-compose run api-service pytest -v
```

***Link to test technical requirements***
 - https://drive.google.com/file/d/1aDQbMvxXyQTZwjPte4OC70HIqi5MR-tP/view  (Backend Engineer for GetGenAI - a venture-backed startup pioneering the
automation of content review processes for highly regulated industries)
