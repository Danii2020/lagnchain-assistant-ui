from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser

class ImageResponse(BaseModel):
    image_description: str = Field(description="useful information of the image translated to Spanish, if the image is someying known in the popular culture tell me what it is.")

parser = JsonOutputParser(pydantic_object=ImageResponse)