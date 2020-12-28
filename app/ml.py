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
    # user name must be unique, how to code this?
    # password musth be hidden, how to code this?
    x1: float = Field(..., example=3.14)
    user_name: str = Field(..., example='potshot')
    password: str = Field(..., example='bang')
    user_ailment: str = Field(..., example='tired, stressed')
    user_effect: str = Field(..., example='awake, relaxed')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    @validator('x1')
    def x1_must_be_positive(cls, value):
        """Validate that the username is a string and is unique
        I do not yet know how to do this!"""

        assert value > 0, f'x1 == {value}, must be > 0'
        return 'this is not functional'

    # @validator('user_name')
    # def user_name_unique(cls, value):
    #     """Validate that the username is a string and is unique
    #     I do not yet know how to do this!"""

    #     # assert value > 0, f'x1 == {value}, must be > 0'
    #     return 'this is not functional'


@router.post('/predict')
async def predict(item: Item):
    """
    Make random baseline predictions for classification problem 🔮

    ### Request Body
    - `x1`: positive float
    - `user_name`: string
    - `password`: string
    - `user_ailment`: string
    - `user_effect`: string

    ### Response
    - `prediction`: boolean, at random
    - `predict_proba`: float between 0.5 and 1.0, 
    representing the predicted class's probability

    Replace the placeholder docstring and fake predictions with your own model.
    This will become a strain suggestion or list of strain suggestions.
    """
    X_new = item.to_df()
    log.info(X_new)
    y_pred = random.choice([True, False])
    y_pred_proba = random.random() / 2 + 0.5
    return {
        'prediction': y_pred,
        'probability': y_pred_proba
    }
