class BST:

    import Node

    def _init_(self, root):
        self.root = None

    def comp(self, root, node):
        if node.rating > root.rating:
            node.right_child = root
            node.left_child = root.left_child
            root.left_child = root.right_child.left_child
            self.root = node

        elif node.rating < root.rating:
            node.left_child = root.left_child.left_child
            node.right_child = root.left_child.right_child
            root.left_child = node

        else:
            if node.score > root.score:
                node.right_child = root
                node.left_child = root.left_child
                root.left_child = root.right_child.left_child
                self.root = node

            elif node.score < root.score:
                node.left_child = root.left_child.left_child
                node.right_child = root.left_child.right_child
                root.left_child = node

    def search(self, lower, upper, node=None):
        print("This range is inclusive")
        if self.root == None:
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

    def add_node(self, node):
        if self.root == None:
            self.root = node
            print(f'the root is {node}')
            return

        self.comp(node)
        return
