class UIService:
    def __init__(self):
        self.__menu_view = True
        self.__game_view = False
        self.__game_over_view = False
        self.__score_list_view = False
        self.__operations = [self._menu_operation, self._game_operation,
        self._game_over_operation, self._scorelist_operation]
        self.__views = []
        self.__view_operations = []
        self.__update_views()

    def __update_views(self):
        self.__views = [self.__menu_view, self.__game_view,
        self.game_over_view, self.__score_list_view]
        self.__view_operations = list(zip(self.__views, self.__operations))

    def _menu_operation(self):
        pass

    def _game_operation(self, *args):
        pass

    def _game_over_operation(self, *args):
        pass

    def _scorelist_operation(self, *args):
        pass

    def _basic_operations(self):
        return []

    def _final_operations(self, data, *args):
        pass

    def _combine(self, data1, data2):
        return data1 + data2

    def service_operation(self, *args):
        data_struct = self._basic_operations()
        for view, operation in self.__view_operations:
            if view:
                add_data = operation(*args)
                data_struct = self._combine(data_struct, add_data)
        return self._final_operations(data_struct, *args)

    @property
    def game_view(self):
        return self.__game_view

    @property
    def menu_view(self):
        return self.__menu_view

    @property
    def game_over_view(self):
        return self.__game_over_view

    @property
    def score_list_view(self):
        return self.__score_list_view

    @game_view.setter
    def game_view(self, value):
        if isinstance(value, bool) and value:
            self.__game_view = value
            self.__menu_view = not value
            self.__update_views()

    @menu_view.setter
    def menu_view(self, value):
        if isinstance(value, bool) and value:
            self.__menu_view = value
            self.__game_view = not value
            self.__game_over_view = not value
            self.__score_list_view = not value
            self.__update_views()

    @game_over_view.setter
    def game_over_view(self, value):
        if isinstance(value, bool) and value:
            self.__game_over_view = value
            self.__game_view = not value
            self.__update_views()

    @score_list_view.setter
    def score_list_view(self, value):
        if isinstance(value, bool) and value:
            self.__score_list_view = value
            self.__menu_view = not value
            self.__update_views()

    @property
    def views(self):
        return self.__views
