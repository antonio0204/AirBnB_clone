# **Holberton** AirBnB clone - Console
![Lines text](https://pbs.twimg.com/media/El6vk5xW0AUJNY4?format=png&name=4096x4096)

## The following was implemented in the project:

---
| Code | File |
| ------ | ------ |
| 1 | BaseModel class for instantation of AirBnB clone objects |
| 2 | User, State, City, Place, Amenity, Review subclasses that inherit from BaseModel |
| 3 | Serialization/deserialization of instances |
| 4 | A storage engine for the project: FileStorage |
| 5 | A console/command interpreter where we can instantiate, store, destroy, and update attributes of objects, as well as print out the string representation of those objects |

# The Console
![Lines text](https://pbs.twimg.com/media/El6v2qRXgAEykYU?format=jpg&name=large)
---
## Environment
### - Ubuntu 14.04 LTS via Vagrant in VirtualBox and Interpret Python3
#### Your shell should work like this in interactive mode:
```sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

#### But also in non-interactive mode: (like the Shell project in C)
---
```sh
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
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