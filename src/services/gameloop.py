from services.loop import Loop
class GameLoop(Loop):
    def __init__(self, renderer, space, event_handler, clock):
        super().__init__(renderer, event_handler, clock)
        self.__difficulty = 3
        self.__space = space
        self.__points = 0
        self.__game_over = False

    def _get_rendering_params(self):
        return (self.__points, self.__space, self.__game_over)

    def _finalisation(self):
        if not self.__game_over:
            self.__update_space()

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
            self.__game_over = True
        self.__points += plasma_hits

    # def start(self):
    #     running = True
    #     while running:
    #         for commands in self.__event_handler.handle_events():
    #             running = self.__handle_commands(commands)
    #         self.__renderer.draw(self.__points, self.__space, self.__game_over)
    #         self.__clock.tick(60)
    #     return False
