
# """Machine learning functions"""

# import logging
# import joblib
# import random
# import pandas as pd

# from fastapi import APIRouter
# import pandas as pd
# from pydantic import BaseModel, Field, validator
# from sklearn.neighbors import NearestNeighbors



# log = logging.getLogger(__name__)
# router = APIRouter()

# class User(BaseModel):
#     """Use this data model to parse the request body JSON."""
#     user_input: str = Field(..., example=
#         """I am having trouble sleeping, I'm stressed and I don't want to eat. I would like to have an appetite, sleep well, and be able to relax.""")


#     def to_df(self):
#         """Convert pydantic object to pandas dataframe with 1 row."""
#         return pd.DataFrame([dict(self)])


# @router.post('/predict')
# async def predict(user: User):
#     """
#     Make random baseline predictions for classification problem 🔮

#     ### Request Body

#     - `user_input:`: string

#     ### Response
#     - `strain_name`: list
#     - `description`: string
#     - `strain_effects`: string
#     - `strain_ailments`: string
#     """
    
#     vectorizer = joblib.load('app/jl_tfidf.joblib')
#     nn = joblib.load('app/jl_knn.joblib')

#     MJ = pd.read_csv('data\MJ.csv')

#     model_food = vectorizer.transform([user.user_input])

#     strains = []
#     strain_0 = []
#     strain_1 = []
#     strain_2 = []
#     strain_3 = []
#     strain_4 = []
#     for i in range(4):
#         strain_name_[i] = (MJ.loc[nn.kneighbors(model_food.todense())[1][0][i]]['Strain']),
#         description_[i] = (MJ.loc[nn.kneighbors(model_food.todense())[1][0][i]]['Description']),
#         strain_effects_[i] = (MJ.loc[nn.kneighbors(model_food.todense())[1][0][i]]['Effects_y']),
#         strain_ailments_[i] = (MJ.loc[nn.kneighbors(model_food.todense())[1][0][i]]['Ailment'])
#         strains.append(strain_name[i])
#         strain_[i].append(description_[i], strain_effects_[i], strain_ailments_[i])
#         return strains, strain_0, strain_1, strain_2, strain_3, strain_4 
        
#     return {

#         'Top 5 stains': str(strains),
#     #     'First': strain_0,
#     #     'Second': strain_1,
#     #     'Third': strain_2,
#     #     'Fourth': strain_3,
#     #     'Fifth': strain_4
#         }

    # return {
    #     'strain_name': 'nice pot',
    #     'description': 'lots of cool info about nice pot',
    #     'strain_ailments': 'insomnia, anxiety',
    #     'strain_effects': 'peace, chillness'
    #     }

    # - `stain_name`: string
    # - `description`: string
    # - `strain_ailment`: string
    # - `strain_effect`: string

    # strain_name: str = Field(..., example='nice pot')
    # description: str = Field(..., example='lots of cool info about nice pot')
    # strain_ailments: str = Field(..., example='insomnia, anxiety')
    # strain_effects: str = Field(..., example='peace, chillness')
# import os
# from dotenv import load_dotenv
# from fastapi import APIRouter, Depends
# import sqlalchemy

# # load_dotenv()
# # DB_NAME = os.getenv('DB_NAME', default='OOPS')
# # DB_USER = os.getenv('DB_USER', default='OOPS')
# # DB_PASS = os.getenv('DB_PASS', default='OOPS')
# # DB_HOST = os.getenv('DB_HOST', default='OOPS')

# load_dotenv()
# database_url = os.getenv('DB_URL', default='OOPS')
# engine = sqlalchemy.create_engine(database_url)
# connection = engine.connect()
# try:
#     yield connection
# finally:
#     connection.close()
# print(database_url)
# print(DATABASE_URL)