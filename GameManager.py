class GameManager:
    # This class keeps track of the score
    # The score starts at -1 because the first food that will spawn will increment it to 0 which will be the start score
    def __init__(self):
        self.score = -1