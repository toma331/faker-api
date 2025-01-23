from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from faker import Faker
from time import time


api = FastAPI()
faker = Faker()


@api.get('/')
async def root_read(request: Request):
    return RedirectResponse(f'{request.url}docs')



@api.get('/name')
async def faker_name():
    return {'name': faker.name() , 'Time': time() }



@api.get('/email')
async def faker_email():
    return {'email': faker.email() , 'Time': time() }



@api.get('/password')
async def faker_password():
    return {'password': faker.password() , 'Time': time() }


