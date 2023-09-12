# Description
A simple REST API capable of CRUD operations on a Person resource

## Technologies Used
* [Django]: A python web framework
* [DjangoRestFramework(DRF)]: A powerful and flexible toolkit for building APIs

## Installation
* to run this project locally, ensure you have python installed globally
* install virtualenv, to do this run the below code in your terminal
    ```pip install virtualenv```
* Then, clone this repo to your PC
    ```git clone https://github.com/ademola-b/hng-task2.git```
* ### Dependencies
    1. In your terminal, CD into the cloned the repo
    2. Create and activate a virtual environment
        ```
            py -m venv env-name
            env-name\scripts\activate
        ```
    3. Install the dependencies needed to run the app:
        ```pip install -r requirements.txt```
    4. To bring up the database
        ```
            py manage.py makemigrations
            py manage.py migrate
        ```
* #### Run It
    to run the server
    ```py manage.py runserver```
    You can now access the API service on your browser with the below endpoint
        ```http://localhost:8000/api/```

* ## Using the api
    with the API, you can perform the following operations
    1. Add a person
    2. View a person's details by providing the person's id
    3. Edit a person's details by providing the person's id
    4. Delete a person's details by providing the person's id

    ## Endpoints
    ### Add new user
        ```/api/ [POST]```
        using this endpoint, the body look thus:
        ```{
            "name": "",
            "age": null,
            "address": ""
            }
        ```

    ### Modify Person
        ```/api/person-id [GET, PUT, DELETE]```
        with this endpoint, you can either get the person's details, edit or delete a person
        ```{
            "id": person-id
            "name": "person-name",
            "age": person-age,
            "address": "person-address"
            }
        ```
        