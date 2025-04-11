# nginxxdocker
Reverse Proxy for Microservices Using Docker and Nginx

Full Article:
https://murphyelo.com/posts/notes/nginx-server/

## Description:
This project demonstrates the implementation of using Docker containers and Nginx as a reverse proxy for a task management application with two microservices:

1. **User Service:** Handles user authentication and login.
2. **Task Service:** Manages task creation, modification, and retrieval.

## Project Structure:
- **user_service:** Contains the source code and Dockerfile for the User Service.
- **task_service:** Contains the source code and Dockerfile for the Task Service.
- **nginx:** Contains the custom nginx.conf file for Nginx reverse proxy configuration.

## Prerequisites:
- Docker: Install Docker Desktop from [Docker's official website](https://www.docker.com/).
- Docker Compose: Install Docker Compose following the instructions on [Docker's documentation](https://docs.docker.com/compose/install/).

## Instructions:
1. **Building Microservices:**
   - Develop the User Service and Task Service using Flask.
   - Test the services using Postman.

2. **Dockerizing Services:**
   - Create Dockerfiles in the respective service directories to build Docker images.
   - Use the Docker build command (`docker build -t <image-name> .`) to build images for each service.

3. **Setting Up Nginx Reverse Proxy:**
   - Create a custom nginx.conf file in the nginx directory to define reverse proxy configurations.
   - Configure Nginx to forward requests to the appropriate backend service based on URL paths.

4. **Running with Docker Compose:**
   - Pull the official Nginx Docker image: `docker pull nginx`.
   - Use Docker Compose to run the Nginx reverse proxy and microservices in isolated containers:
     ```
     docker-compose up -d
     ```
   
5. **Testing:**
   - Access the services using the URLs provided by Nginx (e.g., `localhost/login`).
   - Ensure that requests are routed correctly to the respective backend services.

## Conclusion:
By following this project, you have successfully used Docker containers and Nginx as a reverse proxy for a task management application with two microservices. The microservices are isolated, allowing for easy deployment and scaling, while Nginx efficiently manages incoming requests and routes them to the appropriate backend services.
