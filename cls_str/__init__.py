import logging
import pathlib
import pydoc
import typing

__version__ = pathlib.Path(__file__).parent.joinpath("VERSION").read_text().strip()


logger = logging.getLogger(__name__)


def cls_to_str(cls: typing.Type) -> str:
    """
    Convert a class object to its fully qualified name (FQN) string.

    If the class is defined in the __main__ module or as a local class, a warning will be issued.
    """  # noqa: E501
    module_name = cls.__module__
    qual_name = cls.__qualname__

    # Check for __main__ trap
    if module_name == "__main__":
        logger.warning(
            f"Class '{qual_name}' is defined in the '__main__' module. "
            f"The generated path '__main__.{qual_name}' cannot be "
            "reliably imported from another independent script or process."
        )

    # Check for local class (defined inside a function)
    if "<locals>" in qual_name:
        logger.warning(
            f"Class '{qual_name}' is defined as a local class (inside a function). "
            f"The generated path '{module_name}.{qual_name}' cannot be "
            "imported because local classes are not accessible from the module level."
        )

    return f"{module_name}.{qual_name}"


def str_to_cls(path: str) -> typing.Type:
    """
    Load a class object from its FQN string using pydoc.locate.

    If the class cannot be found, an ImportError will be raised.
    """
    loaded_class = typing.cast(typing.Type, pydoc.locate(path))

    if loaded_class is None:
        # pydoc.locate returns None on failure, we convert it to a more explicit error
        raise ImportError(f"Unable to find or import class from path: {path}")

    # Check if what we found is actually a class (type)
    if not isinstance(loaded_class, typing.Type):
        logger.error(
            f"Path '{path}' does not point to a class (Type), "
            f"but to a {type(loaded_class)}"
        )

    return loaded_class
