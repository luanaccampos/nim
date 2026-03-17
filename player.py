class Player:
    def __init__(self, player_id, name):
        self.player_id = player_id
        self.name = name
    
    def get_name(self):
        return self.name
    
    def choose_move(self, game_state):
        piles = game_state['piles']

        print(f'{self.name} é a sua vez!')
        print(f'Pilhas atuais: {piles}\n')

        while True:
            try:
                pile_index = int(input("Escolha o índice da pilha: "))
                amount = int(input("Quantidade a remover: \n"))

                return {
                    'pile_index': pile_index,
                    'amount': amount
                }
            except ValueError:
                print('Entrada inválida.\n')
