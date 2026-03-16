class NimGame:
    def __init__(self, piles):
        self.piles = piles
        self.num_players = 2
        self.current_player = 0
        self.winner = None
    
    def is_game_over(self):
        if self.winner is not None:
            return True
        
    def is_valid_move(self, pile_index, amount):
        if pile_index < 0 or pile_index >= len(self.piles):
            return False
        
        if amount <= 0:
            return False
        
        if amount > self.piles[pile_index]:
            return False

        return True

    def apply_move(self, player_id, pile_index, amount):
        if self.is_game_over():
            raise Exception('O jogo já terminou.')

        if player_id != self.current_player:
            raise Exception('Não é a vez desse jogador.')

        if not self.is_valid_move(pile_index, amount):
            raise Exception('Jogada inválida!')
        
        self.piles[pile_index] -= amount

        if all(pile == 0 for pile in self.piles):
            self.winner = player_id
        else:
            self.current_player = (self.current_player + 1) % self.num_players