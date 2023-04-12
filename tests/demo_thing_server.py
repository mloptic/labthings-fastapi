import logging
from typing import Optional
from labthings_fastapi.thing import Thing
from labthings_fastapi.decorators import thing_action, mark_thing_action
from labthings_fastapi.thing_server import ThingServer
from labthings_fastapi.descriptors import PropertyDescriptor

logging.basicConfig(level=logging.INFO)

class MyThing(Thing):
    @thing_action
    def anaction(self, repeats: int, title: str="Untitled", attempts: Optional[list[str]] = None) -> str:
        return "finished!!"
    
    @thing_action
    def increment_counter(self):
        self.counter += 1

    counter = PropertyDescriptor(int, 0, readonly=True)

    foo = PropertyDescriptor(str, "Example")
    
thing_server = ThingServer()
thing_server.add_thing(MyThing(), "/my_thing")

app = thing_server.app