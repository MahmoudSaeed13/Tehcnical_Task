# Technical Task

This is the code solutoin for the technical task for backend mentorship program 2022 intake.

## Description:

This repo contains of two python files [absolute-difference.py](https://github.com/MahmoudSaeed13/Tehcnical_Task/blob/main/absolute-difference.py) and [sub_string.py](https://github.com/MahmoudSaeed13/Tehcnical_Task/blob/main/sub_string.py) for the technical problems and a Django project for creating a public API allowing users to do normal CRUD operations tasks and change state based on API action with respect to task state machine as mentioned.

### Part 1 : Technical Problems:
In this part there is the solution for the two techncial problems **absolute difference** and **common substring**.

#### Absolute difference:
The file [absolute_difference.py](https://github.com/MahmoudSaeed13/Tehcnical_Task/blob/main/absolute-difference.py) is python code for solving the problem fo finding the minimum absolute difference for an array of integers, the program takes the **2** user inputs one is the legnth of the array and the other is a string of **space-separated** array of integers, Then converts the array and converts in to a list of integers and make sure its legnth is exactly as the user enterd. Then the program performs some calculations on the array to etermine the minimum absolute difference and prints it to the user.
##### How to run the program:
When navigate in the dir that contains the file absolute_difference.py and run in the cammand promt *python absolute_difference.py* you will be prompted to enter the legnth of the array and **space-separated** array of integers the program will return to you an integer of the minimum absoulte difference 

#### Common Substring:
The file [sub_string.py](https://github.com/MahmoudSaeed13/Tehcnical_Task/blob/main/sub_string.py) is a python code that prompts the user to enter 2 strings and then a function that takes both strings as arguments and loops over both of them to determine if they have at least one similar charachter **case insensitively** as *H == h*, the function returns 'YES' if any smilarities found and 'NO' if there is no similar letters.

##### How to run the program:
When navigate in the dir that contains the file and run the command *python sub_string.py* you will be prompted to enter two different strings the the program will responde with 'YES' or 'NO' weather it found common sub strings or not.

### Part 2 : Technical Project:

This part is a django project that makes a public API to allow user to make CRUD operations in a task and cange it's state based on a predefined state machine that this task
must respect, and it performs some test cases on the API to asserts that everything is working as needed.
**The project is built using django rest framework and needs to install the library *djangorestframework***
models.py, tests.py, urls.py, views.py
when navigate inside the dir Technical_Project and then inside api you now can see the files where all the code is written
- [models.py](https://github.com/MahmoudSaeed13/Tehcnical_Task/blob/main/Technical_Project/api/models.py):    
in this file the model Task is defined which has an id, title and state.
- [urls.py](https://github.com/MahmoudSaeed13/Tehcnical_Task/blob/main/Technical_Project/api/urls.py):  
in this file all the paths in our project is defined.
- [views.py](https://github.com/MahmoudSaeed13/Tehcnical_Task/blob/main/Technical_Project/api/views.py):  
in the views.py file implemented all the views , they are function based views. 
- [test.py](https://github.com/MahmoudSaeed13/Tehcnical_Task/blob/main/Technical_Project/api/tests.py):  
in tests.py built some test cases for our project to ensure and assert that it's working as needed.
#### List of project urls:
- **"/"** this url runs a ***GET*** request to show all the tasks in the database - returns an HTTP status 200 when runs without any problems and status 204 if there are no taks in the database
- **"/<int:id>"** this url takes a integer id and it runs ***GET*** request to show a specific task by its id and it returns status code of 200 when OK and 404 NOT found when the task does not exist in the database
- **"/create"** this url runs a ***POST*** request to add task to the database it retuens status code of 201 when CREATED and 406 when the content you provided is NOT ACCEPTABLE
- **"/update/<int:id>"** this url runs a ***PUT*** request to update a specific task by id it return status code of 200 when updated and 405 when the METHOD NOT ALLOWED
- **"/delete/<int:id>"** this url runs a ***DELETE*** request to delete a specific task by id and it returns status code of 200 when deleted.
#### How to run the program:
**YOU CAN USE THE BROWSER TO RUN THE PROJECT OR YOU CAN USE POSTMAN DESKTOP**.  
When you navgate in the dir Technical_Project and run the command line *python manage.py runserver* it will run the project and provieds you a link to visit *http://127.0.0.1:8000/* when you visit the link you will be shown all the tasks in the database and providing one of the urls shown above you shall be able to GET a specific task, POST *create* a new task, PUT *update* a specific task by id or DELETE a specific task by id. 

