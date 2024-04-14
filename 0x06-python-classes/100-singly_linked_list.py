#!/usr/bin/python3
"This module contains linked list implimentation"


class Node:
    """A class that define the node of single linked list"""

    def __init__(self, data, next_node=None):
        """Initializes a node with the given data and next node.

        Parameters:
            data (int): The data of the node.
            next_node (node): The next node in the linked list. Default to None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the node"""

        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the node.

        Parameters:
            value (int): The data to set.

        Raises:
            TypeError: If the data is not an integer.
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node in the linked list"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the data of the node.

        Parameters:
            value (node): The next node to set.

        Raises:
            TypeError: If the next node is not a node object.
        """

        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """Class that defines a single linked list"""
    def __init__(self):
        """Initializes an empty singly linked list."""

        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list
        (increasing order).
        Parameters:
            value (int): The value to insert.
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node
        else:
            new_node.next_node = current.next_node
            current.next_node = new_node
    def __str__(self):
        """ Returns string representation of linked list

        Returns:
            str: String representation of the linked list
            """

        return_string = ''
        current = self.head
        while current:
            return_string += str(current.data) + "\n"
            current = current.next_node
        return return_string.rstrip("\n")
