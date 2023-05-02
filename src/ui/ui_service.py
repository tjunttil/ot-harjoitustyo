class UIService:
    def __init__(self):
        self.__menu_view = True
        self.__game_view = False
        self.__game_over_view = False

    def __menu_operation(self):
        pass

    def __game_operation(self):
        pass

    def __game_over_operation(self):
        pass

    def operation(self):
        if self.__menu_view:
            self.__menu_operation()
        if self.__game_view:
            self.__game_operation()
        if self.__game_over_view:
            self.__game_over_operation()
