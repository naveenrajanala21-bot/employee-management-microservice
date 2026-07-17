# Employee Management Microservices

Production-ready microservices architecture built with Java 21, Spring Boot 3, and Spring Cloud.

## Services
- Eureka Server (Port 8761): Service Discovery
- Config Server (Port 8888): Centralized Configuration
- API Gateway (Port 8080): Spring Cloud Gateway with JWT Validation
- Employee Service: Manages Employee data
- Department Service: Manages Department data
- Leave Service: Manages Leave Applications
- Notification Service: Mock Email Notifications

## Tech Stack
- Java 21
- Spring Boot 3 & Spring Cloud
- OpenFeign
- Spring Data JPA
- PostgreSQL
- Spring Security (JWT based)
- Docker & Docker Compose
- Swagger for API Docs

## How to Run
1. Run `docker-compose up --build`
2. Access Eureka: http://localhost:8761
3. Access API Gateway: http://localhost:8080 API endpoints

Import `Postman_Collection.json` to Postman to test APIs.