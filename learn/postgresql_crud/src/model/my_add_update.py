from entity.response import PostAnimalsResponse, ResponseSummary
from entity.request import PostAnimalRequest
from entity.response import PostAnimalsResponse

class MyAddUpdate:
    def __init__(self, cursor) -> None:
        self.__cursor = cursor
        
    def post_animals(self, animals: list[PostAnimalRequest]) -> PostAnimalsResponse:
        # TODO
        return PostAnimalsResponse(
            summary=ResponseSummary(
                status_code=200, 
                status_label="OK", 
                message=""
            )
        )