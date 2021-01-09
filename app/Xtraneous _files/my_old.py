"""
Machine learning functions
This format was based upon using a list of checkboxes,
which is not really what NLP is intended to do.
"""

'''

import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()

class User(BaseModel):
    """Use this data model to parse the request body JSON."""
    Type: str = Field(..., example='Type')
    Depression: str = Field(..., example='Depression')
    Inflammation: str = Field(..., example='')
    Insomnia: str = Field(..., example='Insomnia')
    Appitite:str = Field(..., example='Appitite')
    Pain:str = Field(..., example='Pain')
    Nausea:str = Field(..., example='Nausea')
    Creative: str = Field(..., example='')
    Energetic: str = Field(..., example='Energetic')
    Euphoric: str = Field(..., example='')
    Focused: str = Field(..., example='')
    Happy: str = Field(..., example='Happy')
    Hungry: str = Field(..., example='Hungry')
    Relaxed: str = Field(..., example='Relaxed')


    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    # @validator('x1')
    # def x1_must_be_positive(cls, value):
    #     assert value > 0, f'x1 == {value}, must be > 0'
    #     return value

    #     """Validate that the username is a string and is unique
    #     I do not yet know how to do this!"""

    # @validator('user_ailment')
    # def user_ailment_string(cls, value):
    #     """Validate that the username is a string and is unique
    #     I do not yet know how to do this!"""

    #     assert type(value) is StringType, "input is not a string: %r" % name
    #     return value


@router.post('/predict')
async def predict(user: User):
    """
    Make random baseline predictions for classification problem 🔮

    ### Request Body

    - `Type`: string
    - `Depression`: string
    - `Inflammation`: string
    - `Insomnia`: string
    - `Appitite`: string
    - `Pain`: string
    - `Nausea`: string
    - `Creative`: string
    - `Energetic`: string
    - `Euphoric`: string
    - `Focused`: string
    - `Happy`: string
    - `Hungry`: string
    - `Relaxed`: string

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

'''