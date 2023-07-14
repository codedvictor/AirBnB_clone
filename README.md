# AirBnB Clone

## Contents :bookmark:

   - [Intro](#Intro)
   - [Environment](#Environment)
   - [Requirements](#Requirements)
   - [Files](#Files_Structure)
   - [Installation](#Installation)
   - [Usage](#Usage)
   - [Authors](#Authors)

## Intro :page_with_curl:

This is the first step towards building our first full web application: the AirBnB clone. This first step is very important because we will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

This first step will focus on building a basic console using the Cmd Python module, to handle objects of the project with methods to create, show, update, all and destroy the classes instances.


## Environment :snake:

All files had been written/executed on Ubuntu 20.04 LTS using python3 (version 3.8.5)


## Requirements :spiral_notepad:

 - The code uses the pycodestyle (version 2.8.*)
 - All files are executable
 - All test files are python files
 - All tests can be executed by using this command: python3 -m unittest discover tests


## Files Structure :deciduous_tree:
```
AUTHORS
README.md
console.py
models
   |-- __init__.py
   |-- amenity.py
   |-- base_model.py
   |-- city.py
   |-- engine
   |   |-- __init__.py
   |   |-- file_storage.py
   |-- place.py
   |-- review.py
   |-- state.py
   |-- user.py
tests
   |-- __init__.py
   |-- test_models
   |   |-- __init__.py
   |   |-- test_amenity.py
   |   |-- test_base_model.py
   |   |-- test_city.py
   |   |-- test_engine
   |   |   |-- __init__.py
   |   |   |-- test_file_storage.py
   |   |-- test_place.py
   |   |-- test_review.py
   |   |-- test_state.py
   |   |-- test_user.py
```

## Installation


## Usage :clapper:

   | **Commands** | **Documentation** |
   | ------------ | ----------------- |
   | create | Creates instance of a class: type create <class_name> or <class_name>.create() |
   | show | Prints the string representation of an object based on class and id: type show <class_name> <obj_id> or <class_name>.show(<obj_id>) |
   | destroy | Deletes an object based on the class name and id and update the Json file: type destroy <class_name> <obj_id> pr <class_name>.destroy(<obj_id>) |
   | all | Prints all string representation of all objects based or not on lcass name: type all or all <class_name> or <class_name>.all() |
   | update | Updates an object based on the class name and id by setting object attribute and saving it in the Json file: type update <class_name> <obj_id> <attribute> <value> or <class_name>.update(<obj_id>, <attribute>, <value>) |
   | count | Counts and prints the number of instance of class: type <class_name>.count() or count <class_name> |
   | help | Lists all command and prints command documentation: type help <cmd> |
   | quit | Exit the console: type quit|
   | EOF | Exit the console: type EOF |


   #### Examples
   - No.1
   ```
   AirBnB_clone# ./console.py
   (hbnb) help
   
   Documented commands (type help <topic>):
   ========================================
   EOF  all  count  create  destroy  help  quit  show  update
   
   (hbnb) all
   []
   (hbnb) create User
   3b18ca1a-5231-4078-8895-c4016424a9cb
   (hbnb) show User 3b18ca1a-5231-4078-8895-c4016424a9cb
   [User] (3b18ca1a-5231-4078-8895-c4016424a9cb) {'id': '3b18ca1a-5231-4078-8895-c4016424a9cb', 'created_at': datetime.datetime(2023, 7, 14, 15, 47, 46, 293282), 'updated_at': datetime.datetime(2023, 7, 14, 15, 47, 46, 293322)}
   (hbnb) update User 3b18ca1a-5231-4078-8895-c4016424a9cb first_name 'Betty'
   (hbnb) show User 3b18ca1a-5231-4078-8895-c4016424a9cb
   [User] (3b18ca1a-5231-4078-8895-c4016424a9cb) {'id': '3b18ca1a-5231-4078-8895-c4016424a9cb', 'created_at': datetime.datetime(2023, 7, 14, 15, 47, 46, 293282), 'updated_at': datetime.datetime(2023, 7, 14, 15, 49, 6, 101341), 'first_name': 'Betty'}
   (hbnb) create User
   0d22daae-10b3-44ac-b879-eb036a816e46
   (hbnb) all User
   ["[User] (3b18ca1a-5231-4078-8895-c4016424a9cb) {'id': '3b18ca1a-5231-4078-8895-c4016424a9cb', 'created_at': datetime.datetime(2023, 7, 14, 15, 47, 46, 293282), 'updated_at': datetime.datetime(2023, 7, 14, 15, 49, 6, 101341), 'first_name': 'Betty'}", "[User] (0d22daae-10b3-44ac-b879-eb036a816e46) {'id': '0d22daae-10b3-44ac-b879-eb036a816e46', 'created_at': datetime.datetime(2023, 7, 14, 15, 49, 37, 865027), 'updated_at': datetime.datetime(2023, 7, 14, 15, 49, 37, 865065)}"]
   (hbnb) destroy User 0d22daae-10b3-44ac-b879-eb036a816e46
   (hbnb) show User 0d22daae-10b3-44ac-b879-eb036a816e46
   ** no instance found **
   (hbnb) all User
   ["[User] (3b18ca1a-5231-4078-8895-c4016424a9cb) {'id': '3b18ca1a-5231-4078-8895-c4016424a9cb', 'created_at': datetime.datetime(2023, 7, 14, 15, 47, 46, 293282), 'updated_at': datetime.datetime(2023, 7, 14, 15, 49, 6, 101341), 'first_name': 'Betty'}"]
   (hbnb) quit
   AirBnB_clone#
   ```

   - No.2
   ```

   ```


## Authors 📕🖋👩
