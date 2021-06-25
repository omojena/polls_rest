from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models.user import User
from api.serializers.user_serializer import UserSerializer
from api import utils


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, utils.CanChangeUser,)


class ChangeIsActive(APIView):

    def post(self, request, *args, **kwargs):
        try:
            if request.user.userType == utils.SUPER_ADMIN:
                data = request.data
                user_id = data.get('id')
                user = User.objects.get(id=user_id)
                value = not user.is_active
                user.is_active = value
                user.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'User updated successfully',
                    'data': []
                }
                return Response(response)
            else:
                return Response({"message": "User does not have permissions to perform this operation"},
                                status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ChangeUserType(APIView):

    def post(self, request, *args, **kwargs):
        try:
            if request.user.userType == utils.SUPER_ADMIN:
                data = request.data
                user_type = data.get('user_type')
                user_id = data.get('id')
                user = User.objects.get(id=user_id)
                user.userType = user_type
                user.save()
                response = {
                    'status': 'success',
                    'code': status.HTTP_200_OK,
                    'message': 'User type updated successfully',
                    'data': []
                }
                return Response(response)
            else:
                return Response({"message": "User does not have permissions to perform this operation"},
                                status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
