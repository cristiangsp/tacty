from tacty.command_bus import CommandBus
from tacty.handler import Handler
from tacty.middleware import CommandHandlerMiddleware
from tacty.resolver import InMemoryResolver


class AddTwoNumbersCommand:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b


class AddTwoNumbersHandler(Handler):
    def handle(self, command: AddTwoNumbersCommand):
        return command.a + command.b


if __name__ == "__main__":
    resolver = InMemoryResolver()
    resolver.add_handler(AddTwoNumbersCommand, AddTwoNumbersHandler())

    command_bus = CommandBus([CommandHandlerMiddleware(resolver)])
    print(command_bus.handle(AddTwoNumbersCommand(2, 3)))
