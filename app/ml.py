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
    # password must be hidden, how to code this?
    user_name: str = Field(..., example='PotShot')
    password: str = Field(..., example='bang')
    user_ailment: str = Field(..., example='tired, stressed')
    user_effect: str = Field(..., example='awake, relaxed')


    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    # @validator('x1')
    # def x1_must_be_positive(cls, value):
    #     assert value > 0, f'x1 == {value}, must be > 0'
    #     return value

    #     """Validate that the username is a string and is unique
    #     I do not yet know how to do this!"""

    @validator('user_name')
    def user_name_string(cls, value):
        """Validate that the username is a string and is unique
        I do not yet know how to do this!"""

        assert type(value) is StringType, "name is not a string: %r" % name
        return value


@router.post('/predict')
async def predict(item: User):
    """
    Make random baseline predictions for classification problem 🔮

    ### Request Body
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
