

# КЛИЕНТСКАЯ ЧАСТЬ

from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


task_temp_url = APIRouter(tags=["task"]) # чтобы красиво отображались в категории в доксе вместо default сверзу
template = Jinja2Templates(directory='templates')


@task_temp_url.get(path='/')
def index(request: Request):
    return template.TemplateResponse(
        request=request,
        name='homepage.html',
    )

@task_temp_url.get(path='/register')
def register(request: Request):
    return template.TemplateResponse(
        request=request,
        name='registration_page.html',
    )

