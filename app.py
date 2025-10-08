from modelos.restaurantes import Restaurante

restaurante_praca = Restaurante('preça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Any', 2)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()