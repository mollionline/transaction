from fastapi import APIRouter
from app.endpoinds import endpoinds

routes = APIRouter()

routes.include_router(endpoinds.router, prefix='/api/v1')