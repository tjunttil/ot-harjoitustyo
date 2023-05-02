class UIService:
    def __init__(self):
        self.__menu_view = True
        self.__game_view = False
        self.__game_over_view = False

    def __menu_operation(self, data_struct):
        pass

    def __game_operation(self, data_struct):
        pass

    def __game_over_operation(self, data_struct):
        pass

    def __initialisation(self, data_struct):
        pass

    def __finalisation(self, data_struct):
        pass

    def operation(self, data_struct):
        self.__initialisation(data_struct)
        if self.__menu_view:
            self.__menu_operation(data_struct)
        if self.__game_view:
            self.__game_operation(data_struct)
        if self.__game_over_view:
            self.__game_over_operation(data_struct)
        self.__finalisation(data_struct)
        return data_struct

    @property
    def game_view(self):
        return self.__game_view

    @property
    def menu_view(self):
        return self.__menu_view

    @game_view.setter
    def game_view(self, value):
        if isinstance(value, bool):
            self.__game_view = value
            self.__menu_view = not value
