# ETL and REST API Project

## Overview
This project demonstrates a simple yet powerful ETL (Extract, Transform, Load) pipeline for ingesting CSV files into a postgres database. Additionally, a REST API is exposed to retrieve the recently ingested data.
Also, one or more files can be uploaded via another REST api and all the files are saved in azure blob storage.


<div align="center">
  <img src="files/images/system_diagram.png" alt="System Diagram">
</div>

### Features
- **ETL Pipeline:**
  - Ingests one or multiple CSV files into a flexible database
  - Applies basic transformations to load the data into the sql database.
  - Ensures reliable loading of data into the database:
  
![database](https://github.com/karimbenjrad/Task---Data-Engineer---1/assets/57772372/11931a97-5f69-44c9-bcd1-9e9c17245702)
  - Store the ingested files in azure blobstorage:
   
![blob_storage](https://github.com/karimbenjrad/Task---Data-Engineer---1/assets/57772372/e7d4deb6-a945-433d-9904-e75987b3f089)


- **REST API:**
  - Provides a clean API for easy integration with other services.
  - Endpoint `/ingest/` sends one or more CSV files to the microservice:
  
![ingest_endpoint](https://github.com/karimbenjrad/Task---Data-Engineer---1/assets/57772372/e72bde65-e59a-417d-97d5-d05db7fb1b24)
  - Endpoint `/read/first-chunk` retrieves the first 10 lines from the database:
    
![read_endpoint](https://github.com/karimbenjrad/Task---Data-Engineer---1/assets/57772372/90dbd850-9734-4aea-a3fc-6a7a02acf578)
  - Delivers responses in JSON format for easy consumption:
    
![read_response](https://github.com/karimbenjrad/Task---Data-Engineer---1/assets/57772372/7c3692e5-c4aa-4b9e-83e0-e733dbe6f394)


- **Logging and Tracing:**
  - Robust logging throughout the ETL process and API requests using the loguru library.
  - Traceability to troubleshoot issues and monitor performance.

## Good Practices

### Exception Handling
- **Try-Except Blocks:**
  - Utilized throughout the code to handle exceptions gracefully.
  - Ensures the application doesn't crash and provides meaningful error messages.

### Design Patterns
- **Dependency Injector:**
  - Utilized [Dependency Injector](https://github.com/ets-labs/python-dependency-injector) to manage dependencies in a clean and modular way.
  - Enhances testability and maintainability by decoupling components.
  - Promotes a structured approach to dependency management, making the codebase more organized and readable.

- **Singleton Pattern:**
  - Implemented the singleton pattern in postgreSQL session instantiation.
  - Ensures only one instance of the class exists, promoting efficient resource utilization.

- **Factory Pattern:**
  - Applied the factory pattern in the service layer.
  - Encapsulates object creation, providing a clean interface and improving code maintainability.

### Type Hinting
- **Type Annotations:**
  - Used type hints across functions and methods.
  - Enhances code readability and provides better IDE support for developers.

### Docstring
- **Documentation Strings:**
  - Employed docstrings consistently in modules, classes, and functions.
  - Describes the purpose, parameters, and return values for better code understanding.

## Running the code 

    docker-compose up

## Technologies Used
- **Python 3:** Leveraging the power and simplicity of Python.
- **Database:** PostgreSQL - Utilizing PostgreSQL for efficient data storage.
- **ETL Library:** Pandas - Efficient data manipulation and transformation.
- **Database ORM:** SQLAlchemy - Object-Relational Mapping for Python and relational databases.
- **Web Framework:** FastAPI - Building a modern, fast (high-performance), web framework for building APIs.
- **Dependency Injection:** Dependency Injector - Implementing dependency injection for modular and testable code.
- **Docker:** Optional containerization for simplified deployment.
- **Azure Services:** 
  - Azure Identity - Authentication and authorization for Azure services.
  - Azure Storage Blob - Storing and retrieving data in Azure Blob Storage.


## Things to work on
- **tests:** add unit and integtaion tests
- **deployment:** deploy the application using kubernetes or azure
- **CRUDE:** add more endpoints to handle the data and avoid the duplication of the id
- **more exception handling:** handle the exceptions more and take into consideration all the corner cases
