# **Holberton** AirBnB clone - Console
![Lines text](https://pbs.twimg.com/media/El6vk5xW0AUJNY4?format=png&name=4096x4096)
## Description:
The goal of this project is to deploy on your server a simple copy of the AirBnB website.
The complete web application will be composed by:
- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
- A website (the front-end) that shows the final product to everybody: static and dynamic.
- A database or files that store data (data = objects).
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them).
This project will be built in several steps therefore in this step we will focus on build a command interpreter to manipulate data without a visual interface, like in a Shell.
## Classes:
---
| # | Implemented classes |
| ------ | ------ |
| 1 | ```BaseModel``` class for instantation of AirBnB clone objects |
| 2 | ```User ```,```State```, ```City```, ```Place```, ```Amenity```, Review subclasses that inherit from ```BaseModel``` |
| 3 | A storage engine for the project (Save objects): ```FileStorage``` |
| 4 | A ```HBNBCommand``` interpreter where we can instantiate, store, destroy, and update attributes of objects, as well as print out the string representation of those objects |
## Storage:
All the instances of the previously classes are stored in a JSON file called ```file.json```. 
## The Console:
The console is command line that permites interact with the objects.
* create your data model.
* manage (create, update, destroy, etc) objects via a console / command interprete.
* store and persist objects to a file (JSON file).

![Lines text](https://pbs.twimg.com/media/El6v2qRXgAEykYU?format=jpg&name=large)
---
## Using the console:
---
One way of using this program is to clone the repository.
In your terminal type:
```
$ git clone git@github.com:aarizat/AirBnB_clone.git
```
Then
```
$ cd AirBnB_clone
```
Once here in this folder you can run the console like this:
```
$ ./console.py
(hbnb) 
```

The console can be used in interactively and non-interactively:
#### interactive mode:
```sh
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb) 
(hbnb) 
(hbnb) quit
$
```
#### non-interactive mode: 
---
```sh
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
$
```
In order to quit the console, write ```quit``` or ```ctrl + D```.
```
$ ./console.py
(hbnb) quit
$
```
## Available commands:
---
This console supports the following commands:
* `create`
    * Usage: ```create <ClassName>```
Creates a new instance of `ClassName`, saves it (to the JSON file) and prints the `id`.
```
$ ./console.py
(hbnb) create User
a2c9e550-55b5-4243-99b0-658f95af1505
(hbnb) quit
$ cat file.json; echo ""
{"User.a2c9e550-55b5-4243-99b0-658f95af1505": {"created_at": "2020-11-04T19:34:10.606297",
"updated_at": "2020-11-04T19:34:10.606484",
"__class__": "User", "id": "a2c9e550-55b5-4243-99b0-658f95af1505"}}
$
```
* `show`
    * usage: `show <ClassName> <id>` or `<ClassName>.show(<id>)`
Prints the string representation of an instance based on the class name and `id`.
```
$ ./console.py
(hbnb) create BaseModel
040f8e2f-5f20-40f7-be53-787ab8a7894b
(hbnb) show BaseModel 040f8e2f-5f20-40f7-be53-787ab8a7894b
[BaseModel] (040f8e2f-5f20-40f7-be53-787ab8a7894b) {'created_at': datetime.datetime(2020,
11, 4, 19, 42, 53, 976735), 'updated_at': datetime.datetime(2020, 11, 4, 19, 42, 53, 977026),
'id': '040f8e2f-5f20-40f7-be53-787ab8a7894b'}
(hbnb)
```
* `destroy`
    * Usage: `destroy <ClassName> <id>` or `<ClassName>.destroy(<id>)`.
Deletes an instance based on the class name and id (save the change into the JSON file).
```
$ cat file.json; echo ""
{"BaseModel.040f8e2f-5f20-40f7-be53-787ab8a7894b": {"__class__": "BaseModel",
"created_at": "2020-11-04T19:42:53.976735", "id": "040f8e2f-5f20-40f7-be53-787ab8a7894b",
"updated_at": "2020-11-04T19:42:53.977026"},
"User.a2c9e550-55b5-4243-99b0-658f95af1505": {"__class__": "User",
"created_at": "2020-11-04T19:34:10.606297", "id": "a2c9e550-55b5-4243-99b0-658f95af1505",
"updated_at": "2020-11-04T19:34:10.606484"}}
$ ./console.py
(hbnb) User.destroy("a2c9e550-55b5-4243-99b0-658f95af1505")
(hbnb) quit
$ cat file.json ; echo ""
{"BaseModel.040f8e2f-5f20-40f7-be53-787ab8a7894b": {"__class__": "BaseModel",
"id": "040f8e2f-5f20-40f7-be53-787ab8a7894b", "created_at": "2020-11-04T19:42:53.976735",
"updated_at": "2020-11-04T19:42:53.977026"}}
$
```
* `all`
    * Usage: `all` or `all ClassName` or `ClassName.all()`.
Prints all string representation of all instances based or not on the class name.
```
$ ./console.py
(hbnb) create City
464d93dd-8254-465d-b2eb-69b90caf6c6f
(hbnb) all
["[City] (464d93dd-8254-465d-b2eb-69b90caf6c6f) {'id': '464d93dd-8254-465d-b2eb-69b90caf6c6f',
'created_at': datetime.datetime(2020, 11, 4, 19, 56, 51, 680573),
'updated_at': datetime.datetime(2020,11, 4, 19, 56, 51, 680865)}",
"[BaseModel] (040f8e2f-5f20-40f7-be53-787ab8a7894b) {'id': '040f8e2f-5f20-40f7-be53-787ab8a7894b',
'created_at': datetime.datetime(2020, 11, 4, 19, 42, 53, 976735),
'updated_at': datetime.datetime(2020, 11, 4, 19, 42, 53, 977026)}"]
(hbnb) 
```
* `count`
    * USage: `count ClassName` or `ClassName.count()`.
Retrieve the number of instances of a class.
```
$ ./console.py
(hbnb) all
["[City] (464d93dd-8254-465d-b2eb-69b90caf6c6f) {'id': '464d93dd-8254-465d-b2eb-69b90caf6c6f',
'created_at': datetime.datetime(2020, 11, 4, 19, 56, 51, 680573),
'updated_at': datetime.datetime(2020, 11, 4, 19, 56, 51, 680865)}",
"[City] (7e9c93b3-5377-4dea-850e-058a0b46785d) {'id': '7e9c93b3-5377-4dea-850e-058a0b46785d',
'created_at': datetime.datetime(2020, 11, 4, 20, 4, 27, 610554),
'updated_at': datetime.datetime(2020, 11, 4, 20, 4, 27, 611156)}",
"[BaseModel] (040f8e2f-5f20-40f7-be53-787ab8a7894b) {'id': '040f8e2f-5f20-40f7-be53-787ab8a7894b',
'created_at': datetime.datetime(2020, 11, 4, 19, 42, 53, 976735),
'updated_at': datetime.datetime(2020, 11, 4, 19, 42, 53, 977026)}"]
(hbnb) count City
2
(hbnb) BaseModel.count()
1
(hbnb) 
```
* `update`
    * Usage: `update <class name> <id> <attribute name> "<attribute value>"` or `<ClassName>.update(<id>, <attribute name>, <attribute value>)`.
Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).
```
$ ./console.py
(hbnb) all
["[City] (464d93dd-8254-465d-b2eb-69b90caf6c6f) {'id': '464d93dd-8254-465d-b2eb-69b90caf6c6f',
'created_at': datetime.datetime(2020, 11, 4, 19, 56, 51, 680573),
'updated_at': datetime.datetime(2020, 11, 4, 19, 56, 51, 680865)}",
"[City] (7e9c93b3-5377-4dea-850e-058a0b46785d) {'id': '7e9c93b3-5377-4dea-850e-058a0b46785d',
'created_at': datetime.datetime(2020, 11, 4, 20, 4, 27, 610554),
'updated_at': datetime.datetime(2020, 11, 4, 20, 4, 27, 611156)}",
"[BaseModel] (040f8e2f-5f20-40f7-be53-787ab8a7894b) {'id': '040f8e2f-5f20-40f7-be53-787ab8a7894b',
'created_at': datetime.datetime(2020, 11, 4, 19, 42, 53, 976735),
'updated_at': datetime.datetime(2020, 11, 4, 19, 42, 53, 977026)}"]
(hbnb) update City 464d93dd-8254-465d-b2eb-69b90caf6c6f state "California"
(hbnb) City.show("464d93dd-8254-465d-b2eb-69b90caf6c6f")
[City] (464d93dd-8254-465d-b2eb-69b90caf6c6f) {'id': '464d93dd-8254-465d-b2eb-69b90caf6c6f',
'updated_at': datetime.datetime(2020, 11, 4, 20, 14, 58, 220520),
'created_at': datetime.datetime(2020, 11, 4, 19, 56, 51, 680573), 'state': 'California'}
(hbnb) 
```
## Requirements
* All the files were compiled/interpreted on Ubuntu 14.04 LTS using ```Python3``` (3.4.3)
## Authors
---
- **GitHub:** [@aarizat](https://github.com/aarizat)
- **Twitter:** [@aarizatr](https://twitter.com/aarizatr)
- **GitHub**[@ronald0204](https://github.com/ronald0204)
- **Twiitter:** [@ronald45251997](https://twitter.com/ronald45251997)