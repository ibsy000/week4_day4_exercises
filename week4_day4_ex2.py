# I don't want to copy the code example from class exactly
# But I do like a lot of the class and function names...

# I wanted to go back through each of Brian's steps and kind of write them in
# my own way to better understand this Data Structure

class Binary_search_tree:

    # this method initiates the first instance of a node
    def __init__(self, node_value):

        self.node_value = node_value
        self.left_node = None       # left_node will always be the smallest number
        self.right_node = None      # right_node will always be the highest number



    # add a new node to the binary search tree
    def add_node(self, new_node_value):

        # if the new node's value is less than the current node's value
        if new_node_value < self.node_value:

            # if the current node has no left subtree 
            if self.left_node is None:

                # set a new instance of the new value as the left subtree
                self.left_node = Binary_search_tree(new_node_value)
            
            # if the node already has a left subtree
            else:
                # call the add_node method again until there is no left_node
                self.left_node.add_node(new_node_value) 
        
        # if the new node's value is greater than the current node's value
        else:
            # if the current node has no right subtree
            if self.right_node is None:

                # set a new instance of the new value as the right subtree
                self.right_node = Binary_search_tree(new_node_value)

            # if the node already has a right subtree
            else:
                # call the add_node method again until there is no right_node
                self.right_node.add_node(new_node_value)



    # check if certain value is in the Binary_search_tree return False if value
    # is not there, return True if value is there
    def node_search(self, target_node):

        # if target_node is less than current node value
        if target_node < self.node_value:

            # if current node's left value is empty
            if self.left_node is None:

                # this means the target node is not in the Binary_search_tree
                return False

            else:
                # calls node_search method to check the next node
                return self.left_node.node_search(target_node)
        
        # if target_node is greater than current node value
        elif target_node > self.node_value:

            # if current node's right value is empty
            if self.right_node is None:

                # this means the target_node is not in the Binary_search_tree
                return False
            
            else:
                # calls node_search method to check the next node
                return self.right_node.node_search(target_node)

        # if the target_node value is equal to the current node's value
        else:
            return True



    # this method is used the get the max value of the Binary_search_tree
    def max_node(self):

        # if the current node has no right value, we know it's the highest
        if self.right_node is None:

            # return the value of the current node for it is the highest
            return self.node_value

        # if the current node has a right value, call the max_node method again
        else:
            return self.right_node.max_node()



     # this method is used the get the min value of the Binary_search_tree
    def min_node(self):

        # if the current node has no left value, we know it's the smallest
        if self.left_node is None:

            # return the value of the current node for it is the smallest
            return self.node_value

        # if the current node has a left value, call the max_node method again
        else:
            return self.left_node.max_node()



    # this method is used to remove a specified node value from the Binary_search_tree
    def remove_node(self, remove_node_value, parent = None):

        # must move left or right until we find the node to remove
        # if the remove_node_value is less than the current node value
        if remove_node_value < self.node_value:

            # remove_node_value is less than current node value, move left
            # if the subtree has a left_node value
            if self.left_node is not None:

                # call the remove_node method with the left_node as self and the
                # current node as the parent
                self.left_node.remove_node(remove_node_value, self)


        # if the remove_node_value is greater than the current node value
        elif remove_node_value > self.node_value:

            # remove_node_value is greater than current node value, move right
            # if the subtree has a right_node value
            if self.right_node is not None:

                # call the remove_node method with the right_node as self and the
                # current node as the parent
                self.right_node.remove_node(remove_node_value, self)


        # when we find the remove_node_value in the Binary_search_tree
        else:
            # if the remove_node_value has a left_node AND right_node subtree
            if self.left_node is not None and self.right_node is not None:

                # find the highest value in the left_node subtree and copy that
                # value to the current node
                self.node_value = self.left_node.max_node()

                # don't forget to remove the max-lowest node we copied in the
                # previous step
                self.left_node.remove_node(self.node_value, self)


            # if the left_node or right_node is not none but the remove_node has
            # no parent
            elif parent is None:

                # if the left_node is not none then that means the right_node is empty
                if self.left_node is not None:

                    # set the root node to current node's left_node
                    self.node_value = self.left_node.node_value
                    self.right_node = self.left_node.right_node
                    self.left_node = self.left_node.left_node

                # if the right_node is not none then that means the left_node is empty
                elif self.right_node is not None:

                    # set the root node to current node's right_node
                    self.node_value = self.right_node.node_value
                    self.right_node = self.right_node.right_node
                    self.left_node = self.right_node.left_node

                # if both left_node and right_node are None
                else:
                    self.node_value = None


            # if the node to remove is to the left of the parent
            elif parent.left_node == self:

                #if node to remove has subtree
                if self.left_node is not None:

                    # the parent is now the current left_node_value
                    parent.left_node = self.left_node

                # if node to remove has no left subtree
                else:
                    parent.left_node = self.right_node

            # if the node to remove is to the right of the parent
            elif parent.right_node == self:
                
                # if the node to remove has subtree
                if self.left_node is not None:
                    
                    # the parent is not the current right_node_value
                    parent.right_node = self.left_node

                # if node to remove has no right subtree
                else:
                    parent.right_node = self.right_node


tree = Binary_search_tree(75)

tree.add_node(60)
tree.add_node(90)
tree.add_node(45)
tree.add_node(65)
tree.add_node(80)
tree.add_node(105)
tree.add_node(50)
tree.add_node(85)
tree.add_node(110)

tree.remove_node(60)
tree.remove_node(5)


