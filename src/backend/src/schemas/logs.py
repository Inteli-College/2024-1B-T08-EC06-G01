from datetime import datetime
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

class Log(BaseModel):
    id: int = Field(default=None, gt=0)
    date: Optional[datetime] = Field(default=None)
    button_pressed: bool = Field(default=False)
    used_ia: bool = Field(default=False)
    reliability: Optional[float] = Field(default=None)
    user_id: int = Field(default=None)
