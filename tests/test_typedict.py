import openai
import instructor
from typing_extensions import TypedDict
from pydantic import BaseModel, TypeAdapter, create_model

class User_typedict(TypedDict):
    name: str
    age: int
    
class User_pydantic(BaseModel):
    name: str
    age: int

def test_client_pydantic():
    client = instructor.from_openai(openai.OpenAI(), model="gpt-3.5-turbo")

    user = client.create(
        response_model=User_pydantic,
        messages=[{"role": "user", "content": "Jason is 10"}],
        temperature=0,
    )
    assert user.name == "Jason"
    assert user.age == 10

def test_client_typedict():
    client = instructor.from_openai(openai.OpenAI(), model="gpt-3.5-turbo")
    user = client.create(
        response_model=TypeAdapter(User_typedict).json_schema(),
        messages=[{"role": "user", "content": "Jason is 10"}],
        temperature=0,
    )
    # assert user.name == "Jason"
    # assert user.age == 10