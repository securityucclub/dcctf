from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Usuarios
from .queries import make_query

class MakeQuery(APIView):
    def post(self, request):
        user = request.data["user"]
        color = make_query(user)

        if len(color) != 0:
            return Response(color)
        else:
            return Response("El usuario no existe!", status=400)
