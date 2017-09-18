#!/bin/sh

python /home/realm_creation.py
java -Dspring.data.mongodb.uri=mongodb://keycloakpoc_mongo/links -jar /home/keycloak-poc-1.0-SNAPSHOT.jar