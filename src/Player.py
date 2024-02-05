class Player:

    def __init__(self, symbol, color):
        """_summary_

        Args:
            symbol (String): "X" or "O"
            color : player color
        """
        self.symbol = symbol
        self.color = color

    def get_couleur(self):
        """_summary_
        Returns:
            return the player color
        """
        return self.color

    def set_couleur(self, col):
        """_summary_
        Args:
            col(int) : the horizontal vertical
        """
        self.color = col

    def get_symbol(self):
        """_summary_
        Returns:
            return the player symbol
        """
        return self.symbol

    def set_symbol(self, sym):
        """_summary_
        Args:
            sym(String) : the player symbol
        """
        self.symbol = sym
