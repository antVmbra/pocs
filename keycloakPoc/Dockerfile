FROM openjdk:8

MAINTAINER  Mario Valentim <mario.valentim@shinesolutions.com>

COPY ./target/keycloak-poc-1.0-SNAPSHOT.jar /home/keycloak-poc-1.0-SNAPSHOT.jar
COPY ./realm_creation.py /home/realm_creation.py
COPY ./demo_realm.json /home/demo_realm.json
COPY ./start.sh /home/start.sh

RUN apt-get update && apt-get install -y python-pip
RUN pip install requests

ENTRYPOINT ["bin/bash","/home/start.sh"]
