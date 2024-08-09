
from dataclasses import dataclass
import uuid

@dataclass
class PostAnimalRequest:
    animal_display_name: str
    animal_key: str = uuid.uuid4()
    animal_age: int = None
    animal_is_friendly: bool = False