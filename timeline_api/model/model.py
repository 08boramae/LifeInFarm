from pydantic import BaseModel

class PutTimeline(BaseModel):
    title: str
    thumbnail: str
    contents: str
    farm: str