# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data # Store the data for the node
        self.next = None # Initialize the next pointer to None (no next node yet)
# Create individual nodes with data values
node1 = Node(10) # First node with data 10
node2 = Node(20) # Second node with data 20
node3 = Node(30) # Third node with data 30
# Link the nodes together to form a chain (a simple linked list)
node1.next = node2
node2.next = node3
# Function to traverse the list and print each node's data
def print_linked_list(head):
# Start with the head node
    current = head
# Continue until reach the end of the list (None)
    while current != None:
        # Print the data and follow with "->"
        print(current.data, end=" -> ")
        # Move to the next node in the list
        current = current.next
    # Indicate the end of the lis
    print("None")

# Test the print function by printing the linked list from node1
print_linked_list(node1)

# Exercise 1: Update node2's data and print the list again
# Change data in the second node
node2.data = 45
print_linked_list(node1)

# Exercise 2: Add a new node (node4) with a new value and link it to the list
# Create a new fourth node with data 75
node4 = Node(75)
node3.next = node4
print_linked_list(node1)

# Exercise 3: Modify the print function to count nodes and print the count
def print_linked_list_with_count(head):
    # Start with the head node
    current = head
    # Initialize a counter for the nodes
    counter = 0
    # Traverse until the end of the list
    while current != None:
        # Print the data for each node
        print(current.data, end=" -> ")
        # Move to the next node
        current = current.next
        # Increment the count for each node visited
        counter += 1
    # Indicate the end of the list
    print("None")
    # Print the total node count
    print(f"Total Node Count: {counter}")
    
# Test the new function to print the list and count nodes
print_linked_list_with_count(node1)