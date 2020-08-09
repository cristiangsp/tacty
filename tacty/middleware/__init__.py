from abc import ABC, abstractclassmethod
from typing import Callable

from tacty.resolver import Resolver


class Middleware(ABC):
    def __init__(self, resolver: Resolver) -> None:
        self.resolver: Resolver = resolver

    @abstractclassmethod
    def execute(self, command: object, next: Callable) -> any:
        pass


class CommandHandlerMiddleware(Middleware):
    def execute(self, command: object, next: Callable) -> any:
        handler = self.resolver.resolve(type(command))
        handler.handle(command)
