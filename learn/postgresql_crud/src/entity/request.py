
from dataclasses import dataclass

@dataclass
class PostAnimalRequest:
    animal_display_name: str
    animal_key: str = None
    animal_age: int = -1
    animal_is_friendly: bool = False