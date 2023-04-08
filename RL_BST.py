class BST:

    def _init_(self):
        from RL_Node import Node
        self.root = Node()

    def __str__(self):
        return f'This is the root {str(self.root)}'

    def add_node(self, node):
        if self.root is None:
            self.root = node
            print(f'New root: {str(node)}')
            return

        if node.rating > self.root.rating:
            node.right_child = self.root
            node.left_child = self.root.left_child
            self.root.left_child = self.root.right_child.left_child
            self.root = node

        elif node.rating < self.root.rating:
            node.left_child = self.root.left_child.left_child
            node.right_child = self.root.left_child.right_child
            self.root.left_child = node

        else:
            if node.score > self.root.score:
                node.right_child = self.root
                node.left_child = self.root.left_child
                self.root.left_child = self.root.right_child.left_child
                self.root = node

            elif node.score < self.root.score:
                node.left_child = self.root.left_child.left_child
                node.right_child = self.root.left_child.right_child
                self.root.left_child = node
        return "node has been added"

    def search(self, lower, upper, node=None):
        print("This range is inclusive")
        if self.root is None:
            print("There's no root")
            return

        if node == None:
            node = self.root

        elif node.left_child == None and node.right_child == None:
            print(node)
            return
        else:
            if node.left_child != None:
                return(self.search(lower, upper, node.left_child))

            if node.right_child != None:
                return(self.search(lower, upper, node.right_child))
