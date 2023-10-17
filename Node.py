class Node:
    import pandas as pd

    def __init__(self, data):
        self.name = data["player_tag"]
        self.assist = data["core_assists"]
        self.goals = data["core_goals"]
        self.rating = data["advanced_rating"]
        self.saves = data["core_saves"]
        self.score = data["core_scores"]
        self.left_child = None
        self.right_child = None

    def __str__(self) -> str:
        print(
            f"""For this match, {self.name} had {self.goals} goal(s), {self.assist} assist(s),
              {self.saves} saves, and an advanced rating of {self.rating}! """
        )
        return
