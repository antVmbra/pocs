# POC of Packer + Docker + Keycloak + Spring Boot + GraphQL Server

Sample project to learn the basics of using these technologies together.

In order to use this POC you will need these software's installed:
- Packer: http://packer.io
- Docker: http://docker.com
- Maven: https://maven.apache.org

Here's an overview of how the technologies work together and the build/start order:
- Packer will build the Docker image of the application
- Docker stores the image of the application
- Docker-compose defines the services and their infrastructure and launches the services
- Keycloak service is started on port 8080 and configured with the admin user and passowrd set to: admin/password
- Keycloak config is set-up for the application
- MongoDB is started on port 27017
- Application is started with Spring Boot and GraphQL Server on port 8180
- the /graphql endpoint is configured to be secured and the endpoint /graphiql is not secured