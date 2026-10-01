from pydantic import BaseModel
from typing import List

class OptionsBase(BaseModel):
  option_text: str
  is_correct: bool = False
  class Config:
    from_attributes = False

class OptionsShow(OptionsBase):
  question_id: int  
  class Config:
    from_attributes = False


class QuestionsBase(BaseModel):
  question_text: str
  options: List[OptionsBase]
  class Config:
    from_attributes = False