import unittest

from tacty.exception import (
    HandlerForCommandAlreadyExistsError,
    HandlerForCommandDoesNotExistError,
    HandlerIsNotAHandlerSubClassError,
)
from tacty.handler import Handler
from tacty.resolver import InMemoryResolver


class TestCommand:
    pass


class TestHandler(Handler):
    def handle(self, command: TestCommand) -> None:
        pass


class WrongHandler:
    pass


class TestInMemoryResolver(unittest.TestCase):
    def test_adding_a_handler(self):
        # Arrange
        test_handler = TestHandler()
        resolver = InMemoryResolver()

        # Act
        resolver.add_handler(TestCommand, test_handler)

        # Assert
        self.assertEqual(resolver.handlers[TestCommand], test_handler)

    def test_adding_a_wrong_handler_fails(self):
        # Arrange
        wrong_handler = WrongHandler
        resolver = InMemoryResolver()

        # Act & Assert
        with self.assertRaises(HandlerIsNotAHandlerSubClassError):
            resolver.add_handler(TestCommand, wrong_handler)

    def test_adding_a_handler_to_a_command_that_already_has_one_fails(self):
        # Arrange
        resolver = InMemoryResolver()

        # Act
        resolver.add_handler(TestCommand, TestHandler())

        # Assert
        with self.assertRaises(HandlerForCommandAlreadyExistsError):
            resolver.add_handler(TestCommand, TestHandler())

    def test_resolving_a_command_successfully(self):
        # Arrange
        resolver = InMemoryResolver()

        # Act
        resolver.add_handler(TestCommand, TestHandler())

        # Assert
        self.assertIsInstance(resolver.resolve(TestCommand), TestHandler)

    def test_resolving_a_command_without_assigned_handler_fails(self):
        # Arrange
        resolver = InMemoryResolver()

        # Act & Assert
        with self.assertRaises(HandlerForCommandDoesNotExistError):
            resolver.resolve(TestCommand)
