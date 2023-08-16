from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from core.models.users import *
from core.serializers.users import *

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save(password=make_password(serializer.validated_data['password']))
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            return Response({'access_token': str(access_token), 'user': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['post'])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = Users.objects.get(email=email)
            if check_password(password, user.password):
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token
                serializer = UserSerializer(user)
                return Response({'access_token': str(access_token), 'user': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response("Invalid email or password", status=status.HTTP_401_UNAUTHORIZED)
        except Users.DoesNotExist:
            return Response("Invalid email or password", status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        refresh_token = request.data.get('refresh_token')

        if refresh_token:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail': 'Logged out successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)









#  //// USE API VIEW ////
#  //// we can use API view for make user  and  we useing  def ( get ,post, put, delete ) for function////

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import UserSerializer
#
# class UserView(APIView):
#     def get(self, request, user_id):
#         try:
#             user = Users.objects.get(id=user_id)
#             serializer = UserSerializer(user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except Users.DoesNotExist:
#             return Response("User not found", status=status.HTTP_404_NOT_FOUND)
#
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, user_id):
#         try:
#             user = Users.objects.get(id=user_id)
#             serializer = UserSerializer(user, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Users.DoesNotExist:
#             return Response("User not found", status=status.HTTP_404_NOT_FOUND)
#
#     def delete(self, request, user_id):
#         try:
#             user = Users.objects.get(id=user_id)
#             user.delete()
#             return Response("User deleted", status=status.HTTP_204_NO_CONTENT)
#         except Users.DoesNotExist:
#             return Response("User not found", status=status.HTTP_404_NOT_FOUND)
