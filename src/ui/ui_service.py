class UIService:
    def __init__(self):
        self.__menu_view = True
        self.__game_view = False
        self.__game_over_view = False
        self.__views = [self.__menu_view, self.__game_view,
        self.game_over_view]

    @property
    def game_view(self):
        return self.__game_view

    @property
    def menu_view(self):
        return self.__menu_view

    @property
    def game_over_view(self):
        return self.__game_over_view

    @game_view.setter
    def game_view(self, value):
        if isinstance(value, bool) and value:
            self.__game_view = value
            self.__menu_view = not value

    @menu_view.setter
    def menu_view(self, value):
        if isinstance(value, bool) and value:
            self.__menu_view = value
            self.__game_view = not value
            self.__game_over_view = not value

    @game_over_view.setter
    def game_over_view(self, value):
        if isinstance(value, bool) and value:
            self.__game_over_view = value
            self.__game_view = not value

    @property
    def views(self):
        return self.__views
