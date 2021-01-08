"""Machine learning functions"""

import logging
import joblib
import json
# import random
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
    ### Request Body

    - `user_input:`: string

    ### Response
    - `strain_name`: string
    - `description`: string
    - `strain_effects`: string
    - `strain_ailments`: string
    x4
    """
    
    vectorizer = joblib.load('app/jl_tfidf.joblib')
    nn = joblib.load('app/jl_knn.joblib')

    MJ = pd.read_csv('https://raw.githubusercontent.com/tt-dspt-200/best-buds/main/data/MJ.csv')

    model_food = vectorizer.transform([user.user_input])

    # ### Old and functional?
    # strain_name_v=(MJ.loc[nn.kneighbors(model_food.todense())[1][0][0]]['Strain']),
    # description_v=(MJ.loc[nn.kneighbors(model_food.todense())[1][0][0]]['Description']),
    # strain_effects_v=(MJ.loc[nn.kneighbors(model_food.todense())[1][0][0]]['Effects_y']),
    # strain_ailments_v=(MJ.loc[nn.kneighbors(model_food.todense())[1][0][0]]['Ailment'])

    # return {

    #     'strain_name': strain_name_v,
    #     'description': description_v,
    #     'strain_effects': strain_effects_v,
    #     'strain_ailments': strain_ailments_v
    #     }

    strains = []
    for i in range(4):
        strain_name = (MJ.loc[nn.kneighbors(model_food.todense())[1][0][i]]['Strain']),
        description = (MJ.loc[nn.kneighbors(model_food.todense())[1][0][i]]['Description']),
        strain_effects = (MJ.loc[nn.kneighbors(model_food.todense())[1][0][i]]['Effects_y']),
        strain_ailments = (MJ.loc[nn.kneighbors(model_food.todense())[1][0][i]]['Ailment'])
        strains.append([strain_name, description, strain_effects, strain_ailments])

    strain_df = pd.DataFrame(strains, columns = ['name', 'description', 'effects', 'ailments'])
    strain_json = strain_df.to_json(orient="records")
    parsed = json.loads(strain_json)
    result = json.dumps(parsed)

    return {
        result
    }
