# **Holberton** AirBnB clone - Console
![Lines text](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201103%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201103T161508Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4337ac2103bc0fefcad123328672a225ae873c2eb0cbf3a050dd810722a4ee45)
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
![Lines text](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201103%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201103T161508Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=08a453af166b1490b025791e63ea6697b732375c047ca7487f2ba68b0725f405)
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
| command | Explanation |
| ------ | ------ |
| all | Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel |
| create |Creates a new instance of CLASS_NAME, saves it (to the JSON file) and print the id |
| show | Prints the string representation of an instance based on the CLASS_NAME and ID |
| destroy | Deletes an instance based on the CLASS_NAME and ID (save the change into the JSON file) |
| update | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). |

## Authors
---
 **GitHub:** [Andres-Ariza](https://github.com/aarizat)
 **Twitter:** [@aarizatr](https://twitter.com/aarizatr)
 **GitHub**[@ronald0204](https://github.com/ronald0204)
 **Twiitter:** [@ronald45251997](https://twitter.com/ronald45251997)