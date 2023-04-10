from rest_framework.decorators import api_view
from rest_framework.response import Response

from client.services import teachbase_service


@api_view(['GET'])
def teachbase_auth(request):
    """ Авторизация через Teachbase
    """
    token = teachbase_service.teachbase_auth()
    return Response(token)
