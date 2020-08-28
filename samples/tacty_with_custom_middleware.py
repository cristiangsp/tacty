from typing import Callable

from tacty.command_bus import CommandBus
from tacty.handler import Handler
from tacty.middleware import Middleware, CommandHandlerMiddleware
from tacty.resolver import InMemoryResolver


class PrintNumberCommand:
    def __init__(self, number):
        self.number = number


class PrintNumberHandler(Handler):
    def handle(self, command: PrintNumberCommand):
        print(command.number)


class PrintLoggerMiddleware(Middleware):
    def execute(self, command: object, next: Callable) -> any:
        print("Executing " + command.__class__.__name__)
        result = next(command)
        print(command.__class__.__name__ + " executed")
        return result


if __name__ == "__main__":
    resolver = InMemoryResolver()
    resolver.add_handler(PrintNumberCommand, PrintNumberHandler())

    command_bus = CommandBus(
        [PrintLoggerMiddleware(), CommandHandlerMiddleware(resolver)]
    )
    command_bus.handle(PrintNumberCommand(300))
