FROM openjdk:8

MAINTAINER  Mario Valentim <mario.valentim@shinesolutions.com>

COPY ./target/keycloak-poc-1.0-SNAPSHOT.jar /home/keycloak-poc-1.0-SNAPSHOT.jar

ENTRYPOINT ["java","-Dspring.data.mongodb.uri=mongodb://keycloakpoc_mongo/links","-jar","/home/keycloak-poc-1.0-SNAPSHOT.jar"]
