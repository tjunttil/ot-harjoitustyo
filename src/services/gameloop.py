from services.loop import Loop
class GameLoop(Loop):
    def __init__(self, renderer, space, event_handler, clock):
        super().__init__(renderer, event_handler, clock)
        self.__difficulty = 3
        self.__space = space
        self.__points = 0

    def _get_rendering_params(self):
        return (self.__points, self.__space)

    def _logic_call(self):
        return self.__update_space()

    def _handle_commands(self, commands):
        movement = commands["move"]
        if movement:
            self.__space.change_ship_velocity(movement[0], movement[1])
        if commands["fire"]:
            self.__space.fire_ship_cannon()
        return super()._handle_commands(commands)

    def __update_space(self):
        self.__space.create_asteroid(self.__difficulty)
        self.__space.move_objects()
        plasma_hits, ship_destruction = self.__space.check_collisions()
        if ship_destruction:
            return "game over"
        self.__points += plasma_hits
        return True
