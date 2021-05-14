from typing import Optional

from pydantic import BaseModel

"""
We can use this response manager class to define response structure to our api endpoints.

"""
class SearchAnswerResponse(BaseModel):
	key1: Optional[float] = None
	key2: Optional[str] = None
	key3: Optional[int] = None