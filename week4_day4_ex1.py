# I don't want to copy the code example from class exactly
# But I do like a lot of the class and function names...

# I wanted to go back through each of Brian's steps and kind of write them in
# my own way to better understand this Data Structure

# the class Node is used to initiate the root node, value, and next_node that will
# be used through the entire Linked List
class Node:

    def __init__(self, node_value):

        # the first time the class Node is called it sets the incoming node_value
        # as the root node
        # every time it's called after it sets the node_value as the previous node_value
        self.node_value = node_value

        # this is the next node 
        self.next_node = None

    def __str__(self):
        # this allows me to print the value of a node when called to print
        return self.node_value

    def __repr__(self):
        # this returns a programmer friendly representation of the called node
        return f"<Node>|{self.node_value}"


# the class Linked_list is used to return the value of node or None.
# insert a new node to the front of the Linked_List
# add a new node to the end of the Linked_list
# add a new node in the Linked_list after a certain node's position
# traverse (iterate) through the Linked_list and print each node 
class Linked_list:

    def __init__(self):
        # the head attribute always points to the FIRST NODE(root_node) in the Linked_list
        self.head = None


    # this method is used to search for a specific node value in the Linked_list
    def _get_node_search(self, node_search_value):

        # start search with the first node in Linked_list
        check = self.head

        # while check(self.head) is True (a node)
        while check is not None:

            # if the check(self.head) value is equal to the node_search_value
            if check.node_value == node_search_value:

                # then you found the node searching for, return that node
                return check

            # if the check(self.head) value is not equal to node_search_value
            # move on to the next_node
            check = check.next_node

        # when check is None (meaning the Linked_list has been searched and found
        # no result of node_search_value)
        return None


    # this method is used to add a new node value to the FRONT of the Linked_list
    def node_to_front(self, new_node_value):

        # first create a new node with the value passed into the method by calling
        # the Node class to create a new instance of a node
        new_node = Node(new_node_value)

        # now set the new_node's next_node attribute to be the current head
        # the current head hands the driver's wheel over to the new_node
        new_node.next_node = self.head

        # now set the new node to the front of the list (self.head)
        self.head = new_node


    # this method is used to add a new node to the END of the Linked_list
    def node_to_end(self, new_node_value):

        # create a new node with the new_node_value passed in
        new_node = Node(new_node_value)

        # check if the Linked_list is empty first
        if self.head is None:
            
            # if the Linked_list is empty then set the head to the new node
            self.head = new_node

        # if the Linked_list is not empty
        else:
            # traverse to the end of the list by check if every node has a next_value
            # once there is no next value you are at the end
            
            node = self.head

            # while the node we are looking at has a next attribute
            while node.next_node is not None:

                # move on the the next node
                node = node.next_node
            
            # once the current node has no next attribute set that node's next
            # attribute to the new node
            node.next_node = new_node


    # this method is used to add a new node to the Linked_list after a certain
    # specified node
    def add_node_after(self, old_node_value, new_node_value):

        # set a node variable to call the _get_node_search method to find the
        # old_node_value in the Linked_list
        old_node = self._get_node_search(old_node_value)

        # check if the old_node_value exists in the Linked_list
        if old_node is None:
            
            # and if the old_node does not exist print "not in list"
            print(f"{old_node_value} is not in the Linked_list.")
            return # end the search

        # if the old_node_value does exist in the Linked_list
        # create a new node with the new_node_value passed into it
        new_node = Node(new_node_value)

        # point the new node's next attribute to the old_node's next attribute
        new_node.next_node = old_node.next_node

        # point the old_node's next to the new node
        old_node.next_node = new_node

    
    # this method is used to traverse through the Linked_list to print each
    # node in order
    def traverse_list(self):
        
        # point to the beginning node in the list
        node = self.head

        # while there is a node (not None)
        while node is not None:
            print(node) # printing (node) calls the __str__ method

            # go to the next node in the Linked_list
            node = node.next_node
# THE END

seasons = Linked_list() # initiated the Linked_list class

seasons.node_to_front('Spring')
seasons.node_to_front('Winter')

seasons.node_to_end('Summer')
seasons.node_to_end('Fall')

seasons.add_node_after('Summer', 'Second Summer')

seasons.traverse_list()