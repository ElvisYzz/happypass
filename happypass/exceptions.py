"""Exceptions used throughout program"""


class BadCommand(Exception):
    """Raised when virtualenv or a command is not found"""


class CommandError(Exception):
    """Raised when there is an error in command-line arguments"""


class CreditAddError(Exception):
    """Raised when there is a error in the adding operation"""


class CreditUpdateError(Exception):
    """Raised when there is a error in the updating operation"""


class CreditFindError(Exception):
    """Raised when there is a error in the finding operation"""


class CreditDeleteError(Exception):
    """Raised when there is a error in the deleting operation"""
