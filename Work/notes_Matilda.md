Section 1
=======

Introduction
-----------
You can run python in 2 modes: interactive or run as a script. Even when running a script, you can use interactive mode via `python3 -i FILE_NAME.py`. It is good to learn python using Terminal, but when doing real projects, it's easier to use an IDE such as Jupyter notebook.

Mutability
-----------

This is one of the most important feature of a data type. If a type is immutable, each operation that attempts to modify its content would create a new instance of the original variable. You need to reassign this new instance to a new variable, or simply replace the origianl variable, in order to use it.

When chosing the right data type, mutability is an important consideration.

* Mutable data types include: List, dictionary, set
* Immutable data types include: Strings, tuple


Pass by reference / value
-----------

* Note that arguments are passed by assignment. (https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference) Beware if the argument you passed around is mutable or immutable!

String
-----------
* Byte strings
* Raw strings (don't interpret `\`)
* Formatted strings (this is useful!)

List
-----------
* Membership test
* Holds any type of data

File 
-----------
* Best practice is to close the file after opening.

Section 2
=======

Tuple
-----------
* Useful method: packing, unpacking

Dictionary
-----------
* Useful method: `.items()`
* `key` must be immutable

Set
-----------
* Contains *unique* items




















