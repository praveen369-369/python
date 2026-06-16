# 1. Create a new list containing the names of 5 different cities
cities = ["Tokyo", "Paris", "New York", "Sydney", "Berlin"]
print( cities)

# 2. Use indexing to access and print the name of the city at the middle index
middle_index = len(cities) // 2
print("City at middle index:", cities[middle_index])

# 3. Use slicing to extract a subset of cities (first 3 cities)
subset = cities[:3]
print("First 3 cities:", subset)

# 4. Sort the list of cities in ascending order
cities.sort()
print("Sorted list:", cities)

# 5. Append a new city to the end of the list
cities.append("London")
print("After appending London:", cities)

# 6. Remove the first city from the list
cities.pop(0)
print("After removing first city:", cities)

# 7. Write a function that takes a list of cities as input and returns the length of the list
def city_count(city_list):
    return len(city_list)

# 8. Test the function with the list of cities
print("Number of cities in the list:", city_count(cities))



output:
    
    
    
['Tokyo', 'Paris', 'New York', 'Sydney', 'Berlin']
City at middle index: New York
First 3 cities: ['Tokyo', 'Paris', 'New York']
Sorted list: ['Berlin', 'New York', 'Paris', 'Sydney', 'Tokyo']
After appending London: ['Berlin', 'New York', 'Paris', 'Sydney', 'Tokyo', 'London']
After removing first city: ['New York', 'Paris', 'Sydney', 'Tokyo', 'London']
Number of cities in the list: 5
