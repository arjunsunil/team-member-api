# Implement Team Member Using Django Rest framework

## Introduction

The goal of the project is to implement an HTTP API to support a team-member management
application. The team member data should be persisted in a MySQL database. The application
needs to support listing team members, adding a new team member, editing a team member,
and deleting a team member.

## To run the application

git clone https://github.com/arjunsunil/team-member-api.git

git checkout develop

make sure that docker and python are installed on your system and correctly configured to run this application.

run `docker-compose up --build` to rebuild and run the application

## API List
1. create/update/delete/list interviewer or candidate `http://127.0.0.1:8000/member`



## API Documentation

### postman collection

`https://github.com/arjunsunil/team-member-api/tree/develop/team-member_postman_collection.json`

### swagger

`http://127.0.0.1:8000/swagger/`


### curl

#### Get the team members list
curl --location --request GET 'http://0.0.0.0:8000/member/'

#### Create a team member
curl --location --request POST 'http://0.0.0.0:8000/member/' \
--form 'first_name="{first_name}"' \
--form 'last_name="{last_name}"' \
--form 'email="{email}"' \
--form 'phone_number="{phone_number}"' \
--form 'role="{role}"'

#### Update a team member
curl --location --request PATCH 'http://0.0.0.0:8000/member/{member_id}/' \
--form 'first_name="{first_name}"' \
--form 'last_name="{last_name}"' \
--form 'email="{email}"' \
--form 'phone_number="{phone_number}"' \
--form 'role="{role}"'

#### Delete a team member
curl --location --request DELETE 'http://0.0.0.0:8000/member/{member_id}/'
