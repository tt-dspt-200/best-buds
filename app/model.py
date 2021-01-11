"""Machine learning functions"""

import logging
import joblib
import json
import pandas as pd

from fastapi import APIRouter
from nltk.stem.snowball import SnowballStemmer
from pydantic import BaseModel, Field
from sklearn.neighbors import NearestNeighbors


log = logging.getLogger(__name__) 
router = APIRouter()





class User(BaseModel):
    """
    The User class contains the input string with a user's ailments, effects, and
    other information used to search for cannabis strains to meet the user's needs.

    The User class can be expanded for use with an application database.
    """
    user_input: str=Field(..., example=
        """
        I am having trouble sleeping, I'm stressed and I don't want to eat.
        I would like to have an appetite, sleep well, and be able to relax.
        I prefer sweet, citrus flavors.
        """)

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])


@router.post('/predict')
async def predict(user: User):
    """
    ### Request Body

    - `user_input:`: string

    ### Response
    JSON format of:
    - `name`: string,`description`: string, `effects`: string, `ailments`: string x 5

    """
    sb = SnowballStemmer("english")
   

    vectorizer = joblib.load('app/jl_tfidf.joblib')
    nn = joblib.load('app/jl_knn.joblib')

    MJ = pd.read_csv('https://raw.githubusercontent.com/tt-dspt-200/best-buds/main/data/MJ.csv')


    model_food = vectorizer.transform([sb.stem(user.user_input)])
    output = []
    for word in user.user_input.split(): 
        output.append(" ".join([sb.stem(word)]))
    stemmed = ""
    for item in output:
        stemmed += item + " "
    model_food = vectorizer.transform({stemmed})


    ### Access strain information and create JSON object

    strain_name_list = []
    description_list = []
    strain_effects_list = []
    strain_ailments_list = []

    for i in range(5):
        strain_name = (MJ.loc[nn.kneighbors(model_food.todense())[1][0][i]]['Strain']),
        description = (MJ.loc[nn.kneighbors(model_food.todense())[1][0][i]]['Description']),
        strain_effects = (MJ.loc[nn.kneighbors(model_food.todense())[1][0][i]]['Effects_y']),
        strain_ailments = (MJ.loc[nn.kneighbors(model_food.todense())[1][0][i]]['Ailment'])
        strain_name_list.append(str(strain_name).strip("(").strip(")")),
        description_list.append(str(description).strip("(").strip(")")),
        strain_effects_list.append(str(strain_effects).strip("(").strip(")")),
        strain_ailments_list.append(strain_ailments)

    strain_df = pd.DataFrame(
        [strain_name_list, description_list, strain_effects_list, strain_ailments_list],
        index=['name', 'description', 'effects', 'ailments']
        ).T
  
    strain_json = strain_df.to_json(orient="records")
    parsed = json.loads(strain_json)
    result = json.dumps(parsed)

    return {
            result
    }
