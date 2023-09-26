from sqlmodel import Field, UniqueConstraint

from app.db.base_model import BaseDBModel
from app.util import BaseEnum


class PromptTypes(str, BaseEnum):
    lesson = "lesson"
    concepts = "concept"
    outline = "outline"
    topic = "topic"
    title = "title"


class Prompt(BaseDBModel, table=True):
    __table_args__ = (UniqueConstraint("hash", "model", name="unique_hash_model"),)
    hash: str = Field(index=True)
    prompt: str
    response: str
    type: PromptTypes
    model: str
