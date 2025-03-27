from typing import Callable, Dict


MessageStrategy = Callable[[str, str], Dict[str, str]]

def message_sender(strategy: MessageStrategy, to: str, message_body: str) -> Dict[str, str]:
    return strategy(to, message_body)