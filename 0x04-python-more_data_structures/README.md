# 0x04-python-more_data_structures

### Sets

In python, "sets" allows the user to store multiple items in one variable. This is very similar to structures in C programming, in the sense they can store different data types in one variable. However, defining and accessing these items are very different in each programming language.

"Sets" are one of four built-in data types in python that stores a collection of data, these four data types are; "sets", "list", "tuple", and "dictionary". Sets are __unordered, unchangeable, and unindexed__.

It's import to note that sets do not allow duplicate values, so make sure that when declaring them that this does not happen.

__Unordered__:

Unordered means that when defining the items in a set, they do not have to be in order and can be defined randomly. 

__unchangeable__:

Unchangeable means that once the set is created, the items within the set cannot be changed but items can be removed (using pop) and added (using update).

In c programming the user would need to define the structure with the keyword "struct", and below it, list the kind of data types that would be used, and then finally name the structure.

Example: structures

struct id{	<------ defining the structure and the name of structure
	char a;	<------ start of data types
	int num;
	double dig; <------ end of data type
} 1st;		<----- variable name

Using this in a C source code would look something like this.

#include \<stdio.h>
int main(void)
{
	st1.a = 'b';
	st1.num = 1996;
	st1.dig = 17.2;

	print("%c: %d: %.2lf\n", st1.a, st1.num, st1.dig);
}

Output:
	b: 1996: 17.20

In Python, this is way more simplified. This can be done by just declaring a variable name and then within __curly braces__, assigning each member or item with a value.

Example: Sets (interactive mode)

	>>> v = {'name': "hiroshi", 'age': 28,}
	>>> v.get('name')
	>>> 'Hiroshi'

	alternative way to access the item

	>>> v['name']
	>>> 'Hiroshi'

There is also the option to get an item that does not exist within the predefined set using the function 'get', this however will not add the item to the set.

Example: undefined item in set

	>>> l = {'name': 'hiroshi', 'age': 29}
	>>> l.get('surname', 'adaniya')
	>>> 'adaniya'
	>>> l
	>>> {'name': 'hiroshi', 'age': 29}

The set remained the same even though we accessed a set that did not exist. You'll noticed that a comma was used when using get instead of a colon. A colon would indicate a slice, and a set is a collection of items.

To add an item to the already created set, "update" can be used to append the data to the set. Remember that to define a set curly braces must be used, so when using 'update' use the curly braces inside the brackets.

Example: update

	>>> l = {'name': 'hiroshi', 'age': 29}
	>>> l.update({'sname': "adaniya"})
	>>> l
	>>> {'name': 'hiroshi', 'age': 29, 'sname': 'adaniya'}

Working with sets in a non-interactive mode.

Example: Sets (non-interactive)

	#!/usr/bin/python3
	a = {'name': 'hiroshi', 'age': 28, 'sname': 'adaniya'}
	print(a.get('name'))

Output:
	hiroshi

To print more than one item at a time:

	#!/usr/bin/python3
	a = {'name': 'hiroshi', 'age': 28, 'sname': 'adaniya'}
	print(a.get('name'), a.get('sname'))

Output:
	hiroshi adaniya

You'll notice that compare to the interactive mode in python, when the output is displayed, there are quotation marks encompassing the result while the non-interactive mode does not.

Difference:
	
	interactive:
		'hiroshi' 'adaniya'
	non-interactive:
		hiroshi adaniya
	
This is because in interactive mode print is not being used, to get the same result as the non-interactive mode, just use print to display the result

	interactive:
		print(a['name'])

		or

		print(a.get('name'))

Output:
	Hiroshi

### Lambda()

The lambda function looks very similar to the function-like macros in C programming. In Python the lambda function are simple one-line functions and do not have a def and the return is implicit,  unlike the usual function definitions in python. So the intent of a lambda function is to be short, simple, and quick to implement.

To define a function in Python you would need to use the "def" keyword and a return statement.

Example: Python Function (returns the sum of two numbers) - non-interactive

	filename: add.py

	def x(a, b):		<------ "def" keyword and the function name "x"
	    return a + b	<------ return statment

The lambda function uses the keyword "lambda" to declare the function and is followed by the argument and the expression.

Example: Lambda	- interactive

	>>> sum = lambda x, y : x + y
	>>> sum(1, 2)

This would print:
	>>> 3

Example: non-interactive

	#!/usr/bin/python3
	a = lambda x, y : x + y
	print("{}".format(a(2, 3)))

Output: 5

When assigning the return to the variable "a" it acts as the functions name and can be used to print the return value.

The lambda function can also compute an else if condition and return the value, for example to find the max int between two integers.

Example: non-interactive

	#!/usr/bin/python3
	xy = lambda x, y : x if x > y else y

Unfortunately since lambda function can only contain a single expression, using an if, elif and else function can't be used, but there is a way to work around this by nesting expression.

Example: non-interactive

	#!/usr/bin/python3
	xi = lambda x, y : x if x > y else y if y > x else x

### Map()

The map function in Python applies the same function to each element of a list. It takes two argument, a function and the sequence / list and then returns the new list to a variable or printed directly.
Example: non-interactive

	list = [1, 2, 3, 4]
	print(list(map(lambda x : x * 2, list)))

This would print:

	[2, 4, 6, 8]

OR:

	m = [2, 4, 6]
	a = list(map(lambda x : x + 2, m))
	print("{}".format(a))

Output:

	[4, 6, 8, 10]

Since the map function works with functions, a predefined function can be used as to affect a list.

Example: non-interactive

	def a(y):
	    return y * 2

	x = [2, 3, 4, 5, 6]
	b = list(map(a, x))
	print("{}".format(b))

Output:
	[4, 6, 8, 10, 12]

The map function can deal with multiple list at once. The lists that are passed can be of different lengths but the map function will only affect up until the lowest indexed list.

The map function will deal vertically with each list, this means that each 0th index of a list will be computed together, the 1st index together, and so on.

Example: non-interactive

	a = [1, 2, 3, 4, 5]
	b = [1, 2, 3]
	c = [1, 2, 3, 5, 6, 6]

	z = list(map(lambda(z, x, c : z + x + c, a, b, c)))
	print("{}".format(z))

Output:

	[3, 6, 9]

### Filter

The filter function in Python filters items from a list depending on the condition (a boolean-value / true or false) that it is given and in turn this will return a new list with the omitted values.

Example:

	l = [1, 2, 3, 4, 5]
	a = list(filter(lambda x : x < 4, l))

	print("{}".format(a))

Output:
	[1, 2, 3]

### Reduce

The reduce function in Python applies the same function to items of a list and returns a single item (not a list), and uses that value as the next parameter in the function.

You'll need to import "__functools__" to use the "reduce" function

Example: 

	from functools import reduce
	l = [1, 2, 3, 4, 5]
	a = reduce(lambda x, y : x + y, l)
	print("{}".format(a))

Output:

	15


