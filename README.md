# Tacty

An extensible command bus for Python 3 inspired by the [Tactician](https://tactician.thephpleague.com/) Project.

## Introduction

A *command bus* is a software component that performs operations in which the data and the execution steps are decoupled. The data for the operation is contained in a *Command* object and the execution steps are contained in a *Handler*. The responsibility of the command bus is matching a Command with its Handler and execute it.

**Tacty** is a library that provides a command bus implementation that is extensbile and easy to use.

## Basic Usage

``` python
# A Command class containing the required data for the operation is defined. 
class PrintNumberCommand:
    def __init__(self, number):
        self.number = number


# A Handler class that receives an instance of the command and contains the execution steps is defined.
class PrintNumberHandler(Handler):
    def handle(self, command: PrintNumberCommand):
        print(command.number)


# An instance of the Command is passed to the command bus for its execution.
command = PrintNumberCommand(300)
command_bus.handle(command)
```

## Initialization

``` python
# A Resolver is a class that given a Command returns its Handler. The InMemoryResolver receives pairs of Command and Handlers keeping them connected in memory.
resolver = InMemoryResolver()
resolver.add_handler(PrintNumberCommand, PrintNumberHandler())

# The CommandHandlerMiddleware uses a resolver to match a Command with its Handler and executes it.
command_handler_middleware = CommandHandlerMiddleware(resolver)

# The CommandBus receives a list of middlewares that are executed when processing a Command. In order to fulfill its minimum functionality (executing a Handler given a Command) an instance of the CommandHandlerMiddleware must be passed as the last element.
command_bus = CommandBus([command_handler_middleware])
```

## Examples

Find next some examples using Tacty:

- [Using Tacty with the in memory resolver](https://github.com/cristiangsp/tacty/blob/master/samples/tacty_with_in_memory_resolver_usage.py)
- [Using Tacty with a custom middleware](https://github.com/cristiangsp/tacty/blob/master/samples/tacty_with_custom_middleware.py)
- [Using Tacty with a Handler that retuns a value](https://github.com/cristiangsp/tacty/blob/master/samples/tacty_with_handler_that_returns_a_value.py)
