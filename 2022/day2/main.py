# For example, suppose you were given the following strategy guide:
#
# A Y
# B X
# C Z
# This strategy guide predicts and recommends the following:
#
# In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

class Rock:
    score = 1
    player_key = "X"
    opponent_key = "A"
    opponent_winning_key = "B"


class Paper:
    score = 2
    player_key = "Y"
    opponent_key = "B"
    opponent_winning_key = "C"


class Scissor:
    score = 3
    player_key = "Z"
    opponent_key = "C"
    opponent_winning_key = "A"


class RockPaperScizzor:
    win = 6
    draw = 3

    def runGame(self, opponent, player):
        player_dict = {"Z": Scissor, "Y": Paper, "X": Rock}
        move = player_dict[player]
        if move.opponent_key == opponent:
            return self.draw + move.score
        if move.opponent_winning_key == opponent:
            return move.score
        return move.score + self.win

    def runGameTwo(self, opponent, what_needs_to_happen):
        play_dict = {"C": Scissor, "B": Paper, "A": Rock}
        win_dict = {Scissor: Rock, Paper: Scissor, Rock: Paper}
        lose_dict = {Scissor: Paper, Paper: Rock, Rock: Scissor}
        what_needs_to_happen_dict = {"Z": "Win", "Y": "Draw", "X": "Lost"}
        opponent_move = play_dict[opponent]
        player_move = what_needs_to_happen_dict[what_needs_to_happen]

        if player_move == "Win":
            return win_dict[opponent_move].score + self.win
        if player_move == "Lost":
            return lose_dict[opponent_move].score
        return opponent_move.score + self.draw


with open('./input.txt') as f:
    matchSheet = f.readlines()
    matchRounds = [x.replace('\n', '').split(" ") for x in matchSheet]
    totalScore = 0
    totalScoreRoundTwo = 0
    for round in matchRounds:
        totalScore += RockPaperScizzor().runGame(round[0], round[1])
        totalScoreRoundTwo += RockPaperScizzor().runGameTwo(round[0], round[1])

    print(f"Totalscore: {totalScore} (Part 1)")
    print(f"Totalscore: {totalScoreRoundTwo} (Part 2)")
