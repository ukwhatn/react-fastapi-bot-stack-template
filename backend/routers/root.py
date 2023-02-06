import logging

from fastapi import APIRouter

# jinja2 template
# from fastapi.templating import Jinja2Templates

# for db import
# import sys
# sys.path.append("/user_modules")

# logger
logger = logging.getLogger(__name__)

# router
router = APIRouter(
    tags=["root"]
)


# jinja2 template
# templates = Jinja2Templates(directory="templates")


@router.get("/")
def root():
    return "Hello World!"
