from tacty.command_bus import CommandBus
from tacty.handler import Handler
from tacty.middleware import CommandHandlerMiddleware
from tacty.resolver import InMemoryResolver


class PrintNumberCommand:
    def __init__(self, number):
        self.number = number


class PrintNumberHandler(Handler):
    def handle(self, command: PrintNumberCommand):
        print(command.number)


if __name__ == "__main__":
    resolver = InMemoryResolver()
    resolver.add_handler(PrintNumberCommand, PrintNumberHandler())

    command_bus = CommandBus([CommandHandlerMiddleware(resolver)])
    command_bus.handle(PrintNumberCommand(300))
