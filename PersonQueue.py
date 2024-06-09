# Define a class for a Person with attributes first_name, last_name, and age
class Person:
    # Initialize a Person object with the provided first name, last name, and age
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

# Define a class for a Queue
class Queue:

    # Initialize an empty list to hold Person objects 
    def __init__(self):
        self.people = []

    # Add a Person object to the Queue
    def enqueue(self, person):
        self.people.append(person)

    # Print each Person's details within the Queue
    def print_queue(self):
        for person in self.people: print(f"{person.first} {person.last}, Age: {person.age}")

# Function to partition the list of people for quicksort
def partition(people, low, high, compare):
    # Select the pivot element from the sublist
    pivot = people[high]  

    i = low - 1  # Initialize the index of the smaller element

    for j in range(low, high):  # Iterate through the sublist
        if compare(people[j], pivot) >= 0:  # Compare elements to the pivot
            i += 1  # Move the index of smaller element
            # Swap elements 
            people[i], people[j] = people[j], people[i]  

    people[i + 1], people[high] = people[high], people[i + 1]  # Move pivot

    return i + 1  # Return the index of pivot


# Custom quicksort function for sorting people based on a given comparison function
def custom_quick_sort(people, low, high, compare):

    # Check if the current sublist to be sorted has more than one element
    if low < high:
    
        # Partition the sublist using the partition function to determine the pivot position
        pivot = partition(people, low, high, compare)

        # Recursively sort the elements before the pivot (left sublist)
        custom_quick_sort(people, low, pivot - 1, compare)

        # Recursively sort the elements after the pivot (right sublist)
        custom_quick_sort(people, pivot + 1, high, compare)

def compare_by_last_name_desc(a, b):
    # Comparison function to sort people by last name in descending order
    return 1 if b.last > a.last else -1 if b.last < a.last else 0

# Comparison function to sort people by age in descending order
def compare_by_age_desc(a, b):
    return b.age - a.age

# Main function to execute the program
def main():
    
    queue = Queue() # Create empty queue

    # Prompt user to add people to the queue
    print("Enter the name (first & last) of 5 people:")
    for i in range(5):
        first = input("First: ")
        last = input("Last: ")
        age = int(input("Age: "))
        person = Person(first, last, age)
        queue.enqueue(person)

    # Display contents of the queue
    print("\nPerson Queue contents:")
    queue.print_queue()

    # Sort queue by last name in descending order
    custom_quick_sort(queue.people, 0, len(queue.people) - 1, compare_by_last_name_desc)
    print("\nPerson Queue sorted by last name:")
    queue.print_queue()

    # Sort queue by age in descending order
    custom_quick_sort(queue.people, 0, len(queue.people) - 1, compare_by_age_desc)
    print("\nPerson Queue sorted by age:")
    queue.print_queue()

if __name__ == "__main__":
    main()
