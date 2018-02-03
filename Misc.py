class Employee: #some bad idea
    """ an example of a class without any methods of variables,
    yet it can be filled later like a structure.
    I think a better idea is using a dictionary"""
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

print john.name