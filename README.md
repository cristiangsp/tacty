# Tacty

An extensible command bus for Python 3 inspired by the [Tactician](https://tactician.thephpleague.com/) Project.

## Introduction

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
## In order to match Commands and Handlers, Tacty uses a Resolver class that defines the matching strategy.
resolver = InMemoryResolver()
resolver.add_handler(PrintNumberCommand, PrintNumberHandler())

## An instance of a resolver must be passes when creating the command bus.
command_bus = CommandBus(resolver)
```