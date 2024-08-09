from dataclasses import dataclass
from entity.data_tables import Animal, AnimalSpecies, Species

@dataclass
class ResponseSummary:
    status_code: int = -1
    status_label: str = '?'
    message: str = '?'
    
@dataclass
class AnimalSummary: 
    summary: ResponseSummary = ResponseSummary()
    animal: Animal | bool = False
    
@dataclass
class PostAnimalsResponse:
    summary: ResponseSummary = ResponseSummary()
    animals: list[AnimalSummary] | bool = False
