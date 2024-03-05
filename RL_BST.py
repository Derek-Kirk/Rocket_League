class BST:
    def __init__(self):
        import RL_Node
        import pandas as pd

        self.data = pd.read_csv("joined_data.csv")
        self.root = None
        self.player = input('What player PRO RL would you like to grab data for?')
        

    def __str__(self):
        return f"This is the root {str(self.root)}"


    def add_node(self, node, next_node=None):
        if self.root is None:
            self.root = node
            return f"New root: {str(node)}"

        if next_node is None:
            next_node = self.root

        elif node.rating > next_node.rating:
            if next_node.right_child is None:
                next_node.right_child = node

            return self.add_node(node, next_node.right_child)

        elif node.rating < next_node.rating:
            if next_node.left_child is None:
                next_node.node.left_child = node

            return self.add_node(node, next_node.left_child)

        return "node has been added"

    # Adds a single player games to BST
    def player_fill(self):
        import RL_Node
        player = self.player

        
        if player not in list(self.data.player_tag):
            print("Try a pro player that does exist")
            return False

        player_df = self.data[self.data.player_tag == player]
        for i in range(len(player_df)):
            obj = RL_Node.Node(player_df.iloc[i])
            self.add_node(obj)
        print(f"all of {player}'s have been added from the 2022-2023 season ")
        return True

    # Using game score to search for specific games
    def search(self, node=None):
        upper_limit = self.data.advanced_rating.max()
        lower_limit = self.data.advanced_rating.min()

        print(f'The range for game scores is {lower_limit} - {upper_limit}.
               PLEASE select a value within the upper and lower when prompted.')
        
        upper = int(input("Provide an upper limit. "))
        lower = int(input('Provide a lower limit. '))

        if upper > upper_limit or lower < lower_limit

        matches = []

        print("This range is inclusive")

        if self.root is None:
            return "There's no root"

        if node is None:
            node = self.root

        if node.rating >= lower and node.rating <= upper:
            matches.append(node)

        elif node.left_child == None and node.right_child == None:
            return

        elif node.left_child is not None and node.left_child >= lower:
            return self.search(lower, upper, node.left_child)

        elif node.right_child is not None and node.right_child <= upper:
            return self.search(lower, upper, node.right_child)
