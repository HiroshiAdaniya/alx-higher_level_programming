# 0x02-python-import_modules

### Modules

Modules are file that are very similar to header files in C programming. They allow the user to access and use, predefined functions within their script or within pythons interpreter. This allows ease of access so that longer programs can be shortened, prevents the repetition of redefining functions and use functions outside of their scope.

In order to use a module the user would need to use the keyword "import" in their script or inside the python interpreter. It's important to note that within the python interpreter, the user can only import each module once per session, if you make any changes to the module you have to restart the interpreter to revert it back to its default version.

Here is an example of a module with defined functions:

	module name: names.py	<------ a file within a directory

	contents of names.py:

	# prints the names in lis
	
	def display():
	    lis = ["Sakura", "Natsuki", "Toshiko"]
	    for i in range(len(lis)):
	        print("{} ".format(lis[i]), end='')
	    print("\n")

	# returns a + b

	def add(a, b):
	    return a + b
	
	# End of module

This is how to import a module in a script and in the python interpreter (>>>)

	script:

	#!/usr/bin/python3
	import names


	interpreter:
	>>> import names

There are variants of the import statement that allows different interactions with modules. For example, you can import a select number of functions from a module. This means that the module itself will not be defined within the scope of the script and any other function will not be accessible. Using the keyword "from" will allow the user to extract the functions they need.

	interpreter:

	>>> from names import display
	...
	>>> display()
	
	script:
	
	#!/usr/bin/python3
	from names import display
	display()

	# This is print the names in the list "lis"

There is an option to typedef a modules name to which ever name you'd like using the keyword "as" while importing.

	>>>import names as l
	>>>l.display()

	# This will have the same result as the previous example and print the list in names

This doesnt only apply to the module, but to the functions within the module as well.

	>>> from names import add as addition
	>>> print("{}".format(addition(1,2))
	>>> 3	<------ output

There is also an option to import all the function from a module by using the character "\*". This means that the module itself will not be defined but all the functions that it contained can be accessed in the scope of the script or interpreter it was called in.

	>>> from names import *
	>>> display()

### dir()

dir() is a built in function that lists all the function names within a module and displays them in a sorted list. However this function does not find a list of builtin functions like; "open", "ord", "str", etc. but rather you'll need to use dir() and the argument "builtins" to list all of these functions.

Using the example above "names.py", if a user were to run python and import "names", then use "dir(names)", it will list the essential functions and the ones the user has defined.

	>>> dir(names)
	>>> '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'display', 'add'

as you can see, the last two names are of those that were personally defined, the others are all essential functions.
