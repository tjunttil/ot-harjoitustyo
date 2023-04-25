class GameLoop:
    def __init__(self, renderer, space, event_handler, event_queue, clock):
        self.__renderer = renderer
        self.__event_handler = event_handler
        self.__event_queue = event_queue
        self.__clock = clock
        self.__space = space
        self.__points = 0
        self.__game_over = False

    def __handle_commands(self, commands):
        if commands["quit"]:
            return False
        movement = commands["move"]
        if movement:
            self.__space.change_ship_velocity(movement[0], movement[1])
        if commands["fire"]:
            self.__space.fire_ship_cannon()
        return True

    def __handle_events(self):
        events = self.__event_queue.get()
        for event in events:
            commands = self.__event_handler.handle_event(event)
            if not self.__handle_commands(commands):
                return False
        return True

    def __update_space(self):
        self.__space.create_asteroid()
        self.__space.move_objects()
        plasma_hits, ship_destruction = self.__space.handle_collisions()
        if ship_destruction:
            self.__game_over = True
        self.__points += plasma_hits

    def start(self):
        while True:
            if not self.__handle_events():
                break
            if not self.__game_over:
                self.__update_space()
            self.__renderer.draw(self.__points, self.__game_over)
            self.__clock.tick(60)
