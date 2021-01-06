"""Machine learning functions"""

import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()

class User(BaseModel):
    """Use this data model to parse the request body JSON."""
    User_Input: str = Field(..., example=
        """I am having trouble sleeping, I'm stressed and I don't want to eat.
        I would like to have an appetite, sleep well, and be able to relax.""")


    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])
\

@router.post('/predict')
async def predict(user: User):
    """
    Make random baseline predictions for classification problem 🔮

    ### Request Body

    - `User_Input:`: string

    ### Response
    - `stain_name`: string
    - `description`: string
    - `strain_ailment`: string
    - `strain_effect`: string
    """
    return {
        'strain_name': 'nice pot',
        'description': 'lots of cool info about nice pot',
        'strain_ailments': 'insomnia, anxiety',
        'strain_effects': 'peace, chillness'
        }

