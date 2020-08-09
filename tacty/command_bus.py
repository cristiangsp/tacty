from typing import Callable, List

from tacty.middleware import Middleware, CommandHandlerMiddleware
from tacty.resolver import Resolver


class CommandBus:
    def __init__(
        self,
        resolver: Resolver,
        middlewares: List[Middleware] = []
    ) -> None:
        middlewares.append(CommandHandlerMiddleware(resolver))
        self.middleware_chain = self.__create_execution_chain(middlewares)

    def __create_execution_chain(
        self,
        middlewares: List[Middleware]
    ) -> Callable:
        last_callable = lambda *args: None

        for middleware in middlewares:
            last_callable = lambda command, middleware=middleware, last_callable=last_callable: middleware.execute(command, last_callable)

        return last_callable

    def handle(self, command) -> None:
        self.middleware_chain(command)
