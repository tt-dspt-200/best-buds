"""Machine learning functions"""

import logging
import joblib
import random
import pandas as pd

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator
from sklearn.neighbors import NearestNeighbors



log = logging.getLogger(__name__)
router = APIRouter()

class User(BaseModel):
    """Use this data model to parse the request body JSON."""
    user_input: str = Field(..., example=
        """I am having trouble sleeping, I'm stressed and I don't want to eat. I would like to have an appetite, sleep well, and be able to relax.""")


    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])


@router.post('/predict')
async def predict(user: User):
    """
    Make random baseline predictions for classification problem 🔮

    ### Request Body

    - `user_input:`: string

    ### Response
    - `strain_name`: string
    - `description`: string
    - `strain_effects`: string
    - `strain_ailments`: string
    """
    
    vectorizer = joblib.load('app/jl_tfidf.joblib')
    nn = joblib.load('app/jl_knn.joblib')

    MJ = pd.read_csv('data\MJ.csv')

    model_food = vectorizer.transform([user.user_input])
    strain_name_v=(MJ.loc[nn.kneighbors(model_food.todense())[1][0][0]]['Strain']),
    description_v=(MJ.loc[nn.kneighbors(model_food.todense())[1][0][0]]['Description']),
    strain_effects_v=(MJ.loc[nn.kneighbors(model_food.todense())[1][0][0]]['Effects_y']),
    strain_ailments_v=(MJ.loc[nn.kneighbors(model_food.todense())[1][0][0]]['Ailment'])

    return {

        'strain_name': strain_name_v,
        'description': description_v,
        'strain_effects': strain_effects_v,
        'strain_ailments': strain_ailments_v
    }
