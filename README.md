# **Holberton** AirBnB clone - Console
![Lines text](https://pbs.twimg.com/media/El6vk5xW0AUJNY4?format=png&name=4096x4096)

## The following was implemented in the project:

---
| # | Implemented classes |
| ------ | ------ |
| 1 | ```BaseModel``` class for instantation of AirBnB clone objects |
| 2 | ```User ```,```State```, ```City```, ```Place```, ```Amenity```, Review subclasses that inherit from BaseModel |
| 3 | A storage engine for the project: ```FileStorage``` |
| 4 | A ```HBNBCommand``` interpreter where we can instantiate, store, destroy, and update attributes of objects, as well as print out the string representation of those objects |

# The Console
![Lines text](https://pbs.twimg.com/media/El6v2qRXgAEykYU?format=jpg&name=large)
---
## Requirements
* All the files were compiled/interpreted on Ubuntu 14.04 LTS using ```Python3``` (3.4.3)
## How to use
---
#### This shell works like this in interactive mode:
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

#### But also in non-interactive mode: 
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
## Now let's create objects from this console.
---
```$
$ ./console.py
(hbnb) create BaseModel
5f670f8f-aa6e-4d40-9566-45e4f86accdc
(hbnb) create User
f4466fae-4f04-494f-8047-c93610368b15
(hbnb) create City
d95bf479-db20-417e-a680-553b8f333a4b
(hbnb) create Place
fe4349b1-554e-471d-8f44-52ffe14263e0
(hbnb) create Amenity
35137dea-d871-4495-9c4b-fd2a41dc0b35
(hbnb) all
["[User] (f4466fae-4f04-494f-8047-c93610368b15) {'created_at': datetime.datetime(2020, 11, 3, 19, 50, 18, 936827), 'updated_at': datetime.datetime(2020, 11, 3, 19, 50, 18, 936893), 'id': 'f4466fae-4f04-494f-8047-c93610368b15'}", "[Amenity] (35137dea-d871-4495-9c4b-fd2a41dc0b35) {'created_at': datetime.datetime(2020, 11, 3, 19, 52, 10, 16294), 'updated_at': datetime.datetime(2020, 11, 3, 19, 52, 10, 16329), 'id': '35137dea-d871-4495-9c4b-fd2a41dc0b35'}", "[Place] (fe4349b1-554e-471d-8f44-52ffe14263e0) {'created_at': datetime.datetime(2020, 11, 3, 19, 52, 1, 409258), 'updated_at': datetime.datetime(2020, 11, 3, 19, 52, 1, 409295), 'id': 'fe4349b1-554e-471d-8f44-52ffe14263e0'}", "[BaseModel] (5bb5bd16-c047-472a-9ce1-e91899e5c2c5) {'created_at': datetime.datetime(2020, 11, 3, 19, 46, 53, 688424), 'updated_at': datetime.datetime(2020, 11, 3, 19, 46, 53, 688460), 'id': '5bb5bd16-c047-472a-9ce1-e91899e5c2c5'}", "[City] (d95bf479-db20-417e-a680-553b8f333a4b) {'created_at': datetime.datetime(2020, 11, 3, 19, 50, 28, 743684), 'updated_at': datetime.datetime(2020, 11, 3, 19, 50, 28, 743720), 'id': 'd95bf479-db20-417e-a680-553b8f333a4b'}"]

(hbnb) destroy City d95bf479-db20-417e-a680-553b8f333a4b
(hbnb) all
["[User] (f4466fae-4f04-494f-8047-c93610368b15) {'created_at': datetime.datetime(2020, 11, 3, 19, 50, 18, 936827), 'updated_at': datetime.datetime(2020, 11, 3, 19, 50, 18, 936893), 'id': 'f4466fae-4f04-494f-8047-c93610368b15'}", "[Amenity] (35137dea-d871-4495-9c4b-fd2a41dc0b35) {'created_at': datetime.datetime(2020, 11, 3, 19, 52, 10, 16294), 'updated_at': datetime.datetime(2020, 11, 3, 19, 52, 10, 16329), 'id': '35137dea-d871-4495-9c4b-fd2a41dc0b35'}", "[Place] (fe4349b1-554e-471d-8f44-52ffe14263e0) {'created_at': datetime.datetime(2020, 11, 3, 19, 52, 1, 409258), 'updated_at': datetime.datetime(2020, 11, 3, 19, 52, 1, 409295), 'id': 'fe4349b1-554e-471d-8f44-52ffe14263e0'}", "[BaseModel] (5bb5bd16-c047-472a-9ce1-e91899e5c2c5) {'created_at': datetime.datetime(2020, 11, 3, 19, 46, 53, 688424), 'updated_at': datetime.datetime(2020, 11, 3, 19, 46, 53, 688460), 'id': '5bb5bd16-c047-472a-9ce1-e91899e5c2c5'}"]

```



## Available commands:
---
| command. | Explanation. |
| ------ | ------ |
| all | Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel |
| create |Creates a new instance of CLASS_NAME, saves it (to the JSON file) and print the id |
| show | Prints the string representation of an instance based on the CLASS_NAME and ID |
| destroy | Deletes an instance based on the CLASS_NAME and ID (save the change into the JSON file) |
| update | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). |

## Authors
---
- **GitHub:** [Andres-Ariza](https://github.com/aarizat)
- **Twitter:** [@aarizatr](https://twitter.com/aarizatr)
- **GitHub**[@ronald0204](https://github.com/ronald0204)
- **Twiitter:** [@ronald45251997](https://twitter.com/ronald45251997)