# hng-assessment

# About The Task(Stage Two)
 - Project aims at implementing CRUD (Create, Read, Update and Delete) functionalities on a resource.

### Prerequisites

Make sure you have the following prerequisites installed on your system:

- Python: You can download and install Python from [python.org](https://www.python.org/downloads/).

### Installation

Follow these steps to set up the project:
1. Clone the repository: 
    ```
    git clone https://github.com/K-Honsu/hng-backend.git
    ```
2. Navigate to the Project Directory
    ```
    cd hng-backend/
    ```
3. Create a virtual environment (optional but recommended):
    ```
    python3 -m venv venv
    ```
4. Activate the virtual environment
    ```
    - On Windows :
    venv\Scripts\activate
    ```

    ```
    - On Mac Os/Linux :
    source venv/bin/activate
    ```
5. Install project Dependencies
    ```
    pip install -r requirements.txt
    ```
6. Inlcude secret key
    ```
        create a .env file with key SECRET_KEY and value of anything. As shown in .env.example
    ```
6. Apply migrations to set up the database:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
7. Start the development server:
    ```
    python manage.py runserver
    ```
- This will start the development server on your local machine, and you should see output similar to the following:

```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

- Open a web browser and navigate to the URL that was displayed in the output. You should see the Django project running on your local machine.

- Congratulations, you have now successfully run a Django Python backend on the local server!

## Usage 
- To register a new name/person, by sending a POST request in your api client, head over to:
```
https://hng-tasks-mbti.onrender.com/api/ : make sure to include the name field in the JSON body as shown below
```
<img src="./images/Screenshot (960).png" width="700px" height="500px" alt="register a user">

- To GET, UPDATE or DELETE the person/name that has been created in your api client, head over to:
```
https://hng-tasks-mbti.onrender.com/api/{id}/  : make sure to select the correct HTTP Method before sending the request
```
## Documentation

- To view proper documentation of API Service, kindly head over to:
```
https://hng-tasks-mbti.onrender.com/docs/swagger/
```

## UML DIAGRAM
- Find link of uml diagram attached 
```
https://drive.google.com/file/d/1909gz5_Cdmwwk4iqEMGQFu5Ow1gF8_va/view?usp=sharing
```

## Error Handling
- Errors such as field must not be blank are taken care of by Django.