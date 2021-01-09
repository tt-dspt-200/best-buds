from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app import model

description = """
This application is to help people who can legally use cannabis to find strains to meet their needs.
Users can input information about ailments they hope to address and the effects they would like to achieve
The result will be a list of the top five recommended strains of cannabis, with descriptions of each.
"""

app = FastAPI(
    title='Best Buds API',
    description=description,
    docs_url='/',
)

app.include_router(model.router, tags=['Medical Needs Search'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)

# app.include_router(db.router, tags=['Database'])
# app.include_router(viz.router, tags=['Visualization'])