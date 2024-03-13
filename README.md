# Worksheet - Classes

The exercises on this labsheet will help you to evidence:
- Develop programs that create simple classes and instantiate objects of those classes.
- Develop programs using functions with parameter passing.

# Task 1 - class Student - BRONZE

1) Open `student.py` and describe what you think the program will do when run. Add comments to the code to explain this.
2) Run `student.py` - compare the result with what you predicted.
3) Modify the code in `student.py`:
	- to comment out the code that prints the `name` of student_1 and the `email` of student_2
	- to call the method `print_details()` to print the details of each student.

# Task 2 - class UniModule - SILVER

You are given a template file `unimodule.py` by your industrial attachment supervisor to complete the definition of `UniModule` class that is to be used to store the details of a module taken by a student with the following specification:

 - instance attributes:
    + `code` - the code of the module, eg COMP1012
    + `name` - the name of the module, eg Introduction to Programming
    + `year` - at which year/level the module is offered either integer 1, 2, 3 or 4
    + `credit` - the credit for the module, eg 10
    + `grade` - the grade obtained for the module, eg 80. The grade should be between integer 0 and 100. The default grade is 0.
    + `PFP` - whether the module is pass for progression module, either boolean `True` or `False`. The default value for PFP is `False`.
 - instance methods:
    + `__init__()` - to initialise all instance attributes
    + `print_details()` - prints the detials of the module taken in the format `code:name:Yyear:creditCR:gradeGRD:[N]PFP`. If `PFP` is False, it will print `NPFP`.
			
The following code snippet is an example to create an instance of the class `UniModule` and call the method `print_details()`.
```
COMP1011 = UniModule("COMP1011", "Intro to Programming", 1, 10)
COMP1011.print_details()
```
The code will produce the following output.
```
COMP1011:Intro to Prog.:Y1:10CR:0GRD:NPFP
```

Based on the specifications, list and explain which of the instance attributes require input validation and how would you validate the input? Please explain if an input validation fails, should the program terminate?

```
# answer here



```

As you might have realised, the specification does not consider the scenario when a student fails a module and have to resit. Please recommend any improvements to UniModule to indicate whether the grade is of first attempt or resit. 
```
# answer here



```

# Task 3 - class Transcript - GOLD
Upon completion of `UniModule` class, you are assigned to complete the definition of a class called `Transcript` in a given template file `transcript.py` that utilises the `UniModule` class. The specification of the `Transcript` class is as follows:

- instance attributes
	
	+ `modules` - a list for all the modules taken by a student. A module is an instance of the UniModule class. When an instance of Transcript is created, this attribute is set to an empty list.
- instance methods
	+ `__init__()` - initialse the instance attribute called modules
	+ `add_module(self, item)` - add an instance of `UniModul` (item) to the modules. If a module has already been added, raise a `ValueError("module already exists!")`. If item is not an instance of `UniModule`, raise a `ValueError("expected item be an instance of UniModule.")`
	+ `print_transcript(self)` - print details of all modules with the `print_details()` method
  + `print_formatted_transcript(self)` - print the details of all modules formatted by year, current year and cummulative credit hours as shown below:

 ```
Year 1
|   Module |     Title           | Grade| Credit Hours | PFP |
| COMP1011 | Intro to Programming|  75  |     10       |  Y  |

                    Attempt Hours | Passed Hours |Earned Hours|
Current year            100      |      100      |    100    |
Cumulative              100      |      100      |    100    |

Year 2
|   Module |     Title           | Grade| Credit Hours | PFP |
| COMPxxxx | xxxxxxxx            |  75  |     10       |  Y  |

                    Attempt Hours | Passed Hours |Earned Hours|
Current year            100      |      100      |    100    |
Cumulative              200      |      200      |    200    |

 ```

The following code snippets creates 3 instances of `UniModule` and add these modules to the instance of `Transcript` and call the `print_transcript()` to print the details of all added modules.
```
COMP1012 = UniModule("COMP1011", "Intro to Programming", 1, 10, grade=75)
COMP1121 = UniModule("COMP1121", "Databases", 1, 10, PFP=True)
COMP1211 = UniModule("COMP1211", "Computer Architecture", 1, 10, grade=80, PFP=True)
t_student1 = Transcript()
t_student1.add_module(COMP1012)
t_student1.add_module(COMP1121)
t_student1.add_module(COMP1211)
t_student1.print_transcript()
t_student1.print_formatted_transcript()
```

The code produces the followings:
```
COMP1011:Intro to Programming:Y1:10CR:75:NPFP
COMP1121:Databases:Y1:10CR:0:PFP
COMP1211:Computer Architecture:Y1:10CR:80:PFP
Year 1
|  Module  |           Title           |Grade|Credit Hours|PFP|
| COMP1011 |Intro to Programming       | 75  |     10     | N |
| COMP1121 |Databases                  |  0  |     10     | Y |
| COMP1211 |Computer Architecture      | 80  |     10     | Y |

                       Attempt Hours|Passed Hours|Earned Hours|
Current year                30      |     20     |     20     |
Cummulative                 30      |     20     |     20     |

```

# Worksheet - Structure Query Language

The exercises on this labsheet will help you to evidence:
- To write SQL queries to create and delete database objects
- To write SQL queries to insert, update, and delete data from database
- To write SQL queries to retrieve data from database.

# Task 1 - database with 1 table - BRONZE

1) Open the file `sql_task1.sql`, describe what you think will happen when the sql queries are executed? Add comments to the code to explain this. Single line comments in sql start with -- as shown in `sql_task1.sql`.
2) Open database and run the sql queries by:
	- Launch sqlite3 in terminal/cmd by typing `sqlite3 task1.db`.
	- On the sqlite terminal prompt, type `.read sql_task1.sql`.
3) Write a INSERT query to add your details to the Student table.
```
# answer here



```
4) Write a SELECT query to retrieve the details of all students called 'John Smith' from the Student table.
```
# answer here



```

# Task 2 - database with 1 table - BRONZE

1) Open the file `sql_task2.sql`, describe what you think will happen when the sql queries are executed? Add comments to the code to explain this. Single line comments in sql start with -- as shown in `sql_task2.sql`.
2) Open database and run the sql queries by:
	- (a) Launch sqlite3 in terminal/cmd by typing `sqlite3 task2.db`.
	- (b) On the sqlite terminal prompt, type `.read sql_task2.sql`.
3) Write a UPDATE query to set the value for the column PFP to 'N' for the module with code COMP1012.
```
# answer here



```
4) Write a SELECT query to retrieve the code for all modules with grade greater and equals to 40.
```
# answer here



```
5) Write a SELECT query to retrieve the code and grade for all PFP modules (ie modules with PFP = 'Y').
```
# answer here



```

# Task 3 - students and grades database - SILVER

## Task 3.1

During your summer internship, your are given a task by your supervisor to write and to update the queries in a given sql file `create_load_data.sql`. To get started, the following instructions were given.

1) Launch sqlite and create a database called `task3.db`
2) Run the sql file `create_load_data.sql` to create the tables and import data to respective tables. You should open `create_load_data.sql` and related files to have a look.
3) Make sure data in student.txt, module.txt, taken.txt are properly imported into respective tables. Please explain how do you plan to validate this?
```
# answer here



```
## Task 3.2

Upon successful creation of the database and imported all data into the respective database tables, you are asked to write a few queries to do the followings in a sql file called `query.sql`.
1) Write a SELECT query to retrieve the student id, name, and grade for all students that failed the module COMP1421.
2) Write a query to create a view called vCOMP1121 for the module leader to view all students in that module (COMP1121) with their student id, name, grade, and remark.

## Task 3.3

Your supervisor is impressed with your progress and would like you to suggest updates to queries in `create_load_data.sql` to:
1) make sure that a module cannot be deleted if it is linked to other tables? It would be fantastic if you could update the queries in `create_load_data.sql` to do so.
2) to ensure that updates to the module code is reflected in other tables. It would be very helpful if you could update the queries in `create_load_data.sql` to do so.


# Task 4 - musicstore database - GOLD
