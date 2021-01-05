from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app import db, ml, viz

description = """
Users can input information about ailments they hope to address, and effects they would like to achieve.
The result with be a list of the top 5 recommended strains of marijuana, with descriptions of each.
"""

app = FastAPI(
    title='Best Buds API',
    description=description,
    docs_url='/',
)

app.include_router(db.router, tags=['Database'])
app.include_router(ml.router, tags=['Machine Learning'])
app.include_router(viz.router, tags=['Visualization'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)
