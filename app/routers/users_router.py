from app import api
from flask_restx import Resource
from flask import Response


user_ns = api.namespace(
    name='HealthCheck',
    description='Validar que el despliegue esta activo',
    path='/health'
)


@user_ns.route('')
class HealthCheck(Resource):
    def get(self):
        ''' Servicio para validar el despliegue '''
        return {
            "Sapo":"Sapo"
        },200