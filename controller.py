class GameController:
    def __init__(self, game, players):
        self.game = game
        self.players = players
    
    def play(self):
        print('=== Início do jogo ===\n')

        while not self.game.is_game_over():
            state = self.game.get_state()
            current_player_id = state["current_player"]
            player = self.players[current_player_id]

            while True:
                move = player.choose_move(state)
                pile_index = move['pile_index']
                amount = move['amount']

                try:
                    self.game.apply_move(current_player_id, pile_index, amount)
                    break

                except Exception as e:
                    print(f"Erro: {e}. Tente novamente.\n")
        
        self.print_winner()
    
    def print_winner(self):
        winner_id = self.game.get_winner()
        print('=== Fim de jogo ===')
        print(f'Vencedor: Jogador {self.players[winner_id].get_name()}!\n')
