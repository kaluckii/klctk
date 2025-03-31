from typing import Any, Callable, List, Union


class Filter:
    @classmethod
    def magic(cls, magic: Callable[..., Any]):
        return lambda message: magic(message)

    @classmethod
    def hastext(cls):
        return lambda message: bool(message.text) or bool(message.caption)

    @classmethod
    def command(cls, command: str):
        if not command:
            return lambda _: False

        return lambda message: message.text and \
                               message.text.startswith("/") and \
                               command in message.text

    @classmethod
    def callback(cls, data: Union[str, List[str]], startswith: bool = False):
        if isinstance(data, list):
            return lambda callback_query: callback_query.data in data

        if startswith:
            return lambda callback_query: callback_query.data.startswith(data)

        return lambda callback_query: callback_query.data == data
