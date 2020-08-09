from tacty.command_bus import CommandBus
from tacty.resolver import InMemoryResolver


class PrintNumberCommand:
    def __init__(self, number):
        self.number = number


class PrintNumberHandler():
    def handle(self, command: PrintNumberCommand):
        print(command.number)


if __name__ == "__main__":

    resolver = InMemoryResolver()
    resolver.add_handler(PrintNumberCommand, PrintNumberHandler())

    command_bus = CommandBus(resolver)
    command_bus.handle(PrintNumberCommand(300))
