class BST:

    def __init__(self):
        from RL_Node import Node
        self.root = None

    def __str__(self):
        return f'This is the root {str(self.root)}'

    def add_node(self, node, next_node=None):

        if self.root is None:
            self.root = node
            return f'New root: {str(node)}'

        if next_node is None:
            next_node = self.root

        elif node.rating > next_node.rating:
            if next_node.right_child is None:
                next_node.right_child = node

            return self.add_node(node, next_node.right_child)

        elif node.rating < next_node.rating:
            if next_node.left_child is None:
                next.node.left_child = node

            return self.add_node(node, next_node.left_child)

        return "node has been added"

    def search(self, lower, upper, node=None):
        matches = []
        print("This range is inclusive")
        if self.root is None:
            return("There's no root")

        if node is None:
            node = self.root

        if node.rating >= lower and node.rating <= upper:
            matches.append(node)

        elif node.left_child == None and node.right_child == None:
            return

        elif node.left_child is not None and node.left_child >= lower:
            return(self.search(lower, upper, node.left_child))

        elif node.right_child is not None and node.right_child <= upper:
            return(self.search(lower, upper, node.right_child))
