import requests
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from client.models import Course
from client.serializers import CourseSerializer
from client.services import teachbase_service
from teachbase.settings import TEACHBASE_HOST


class CoursesListApiView(APIView):
    """Получение списка курсов из сервиса Teachbase
    """

    def get(self, request: Request) -> Response:
        url: str = f'{TEACHBASE_HOST}/courses'
        headers: dict = teachbase_service.teachbase_auth()
        res: requests.Response = requests.get(url, headers=headers, params=request.query_params)
        return Response(res.json(), status=res.status_code)


class CourseApiView(APIView):
    """Получение детального представления о курсе из сервиса Teachbase
    """

    def get(self, request: Request, course_id: int) -> Response:
        url: str = f'{TEACHBASE_HOST}/courses/{course_id}'
        headers: dict = teachbase_service.teachbase_auth()
        res: requests.Response = requests.get(url, headers=headers)
        return Response(res.json(), status=res.status_code)


class UserApiView(APIView):
    """Создание пользователя в сервисе Teachbase
    """

    def post(self, request: Request) -> Response:
        url: str = f'{TEACHBASE_HOST}/users/create'
        headers: dict = teachbase_service.teachbase_auth()
        res: requests.Response = requests.post(url, json=request.data, headers=headers)
        return Response(res.json(), status=res.status_code)


class CourseSessionApiView(APIView):
    """Запись пользователя на сессию в сервисе Teachbase
    """

    def post(self, request: Request, session_id: int) -> Response:
        url: str = f'{TEACHBASE_HOST}/course_sessions/{session_id}/register'
        headers: dict = teachbase_service.teachbase_auth()
        res: requests.Response = requests.post(url, json=request.data, headers=headers)
        return Response(res.json(), status=res.status_code)


class CourseSessionsListApiView(APIView):
    """Получение списка сессий определенного курса в сервисе Teachbase
    """

    def get(self, request: Request, course_id: int) -> Response:
        url: str = f'{TEACHBASE_HOST}/courses/{course_id}/course_sessions'
        headers: dict = teachbase_service.teachbase_auth()
        res: requests.Response = requests.get(url, headers=headers, params=request.query_params)
        return Response(res.json(), status=res.status_code)


class CourseView(ReadOnlyModelViewSet):
    """Получение списка курсов или детального представления одного курса
    """

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
