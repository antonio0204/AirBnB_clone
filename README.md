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
