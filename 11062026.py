# 1. Create a tuple containing the names of 5 different cities
cities = ("Tokyo", "Paris", "New York", "Sydney", "Berlin")
print("Cities tuple:", cities)

# 2. Function that returns the first and last elements of a tuple
def first_and_last(city_tuple):
    return (city_tuple[0], city_tuple[-1])

print("First and last city:", first_and_last(cities))

# 3. Create a tuple of tuples with student names and grades
students = (("John", 85), ("Alice", 92), ("Bob", 78), ("Diana", 88))
print("Students tuple:", students)

# 4. Function that returns a new tuple with students' names sorted alphabetically
def sorted_student_names(student_tuple):
    names = [name for name, grade in student_tuple]
    return tuple(sorted(names))

print("Sorted student names:", sorted_student_names(students))

# 5. Function to practice tuple unpacking
def unpack_tuple(my_tuple):
    a, b, c = my_tuple
    print("First element:", a)
    print("Second element:", b)
    print("Third element:", c)

# Example usage of unpacking function
sample_tuple = ("Python", "AI", "java")
unpack_tuple(sample_tuple)
