class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

        self.score_strings = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1
    
    def _get_even_score(self, score):
        pregame_score_limit = 2
        if 0 <= score <= pregame_score_limit:
            return self.score_strings[score] + "-All"
        else:
            return "Deuce"
    
    def _get_endgame_score(self, string):
        if self.player1_score > self.player2_score:
            return string + self.player1_name
        else:
            return string + self.player2_name

    def get_score(self):
        endgame_score = 4

        if self.player1_score == self.player2_score:
            return self._get_even_score(self.player1_score)
        elif self.player1_score >= endgame_score or self.player2_score >= endgame_score:
            difference = abs(self.player1_score - self.player2_score)
            advantage_difference = 1

            if difference == advantage_difference:
                return self._get_endgame_score("Advantage ")
            else:
                return self._get_endgame_score("Win for ")
        else:
            return \
                self.score_strings[self.player1_score] \
                + "-" \
                + self.score_strings[self.player2_score]
