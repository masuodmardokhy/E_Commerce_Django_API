from rest_framework import viewsets, status
from rest_framework.response import Response
from core.serializers.users import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from django.contrib.auth.hashers import make_password
from django.http import QueryDict
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from core.serializers.token import *
from django.contrib.auth.models import User




class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


    @action(detail=False, methods=['post'])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user = Users.objects.get(email=email)
            if check_password(password, user.password):
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("Invalid email or password", status=status.HTTP_401_UNAUTHORIZED)
        except Users.DoesNotExist:
            return Response("Invalid email or password", status=status.HTTP_401_UNAUTHORIZED)




    # def create(self, request, *args, **kwargs):
    #     data = request.data.copy()
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    #


    # def create(self, request, *args, **kwargs):
    #     data = request.data.copy()
    #     password = data.get('password')
    #     hashed_password = make_password(password)
    #     data['password'] = hashed_password
    #
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #
    #     # Create a token for the user
    #     user = serializer.instance
    #     token = Token.objects.create(user=user)
    #
    #     # Serialize the token
    #     token_serializer = TokenSerializer(token)
    #     response_data = serializer.data
    #     response_data['token'] = token_serializer.data
    #
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
    #


    # @action(detail=False, methods=['post'])
    # def login(self, request):
    #     email = request.data.get('email')
    #     password = request.data.get('password')
    #
    #     user = authenticate(request, email=email, password=password)
    #     if user is not None:
    #         login(request, user)
    #         serializer = UserSerializer(user)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response("Invalid email or password", status=status.HTTP_401_UNAUTHORIZED)
    #




    #
    # @action(detail=True, methods=['get'])
    # def filter_user_by_name(self, request, name=None):
    #     try:
    #         users = Users.objects.filter(first_name=name)
    #         serializer = UserSerializer(users, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except Users.DoesNotExist:
    #         return Response("User not found", status=status.HTTP_404_NOT_FOUND)
    #
    #
    # @action(detail=True, methods=['get'])
    # def filter_user_by_id(self, request, pk=None):
    #     try:
    #         user = Users.objects.get(id=pk)
    #         serializer = UserSerializer(user)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except Users.DoesNotExist:
    #         return Response("User not found", status=status.HTTP_404_NOT_FOUND)
    #
    #
    #
    # @action(detail=False, methods=['post'])
    # def user_sign_in(self, request):
    #     email = request.data.get('email')
    #     password = request.data.get('password')
    #
    #     user = authenticate(request, email=email, password=password)
    #     if user is not None:
    #         login(request, user)
    #         serializer = UserSerializer(user)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response("Invalid email or password", status=status.HTTP_401_UNAUTHORIZED)
    #
    #
    # @action(detail=False, methods=['post'])
    # def user_sign_out(self, request):
    #     logout(request)
    #     return Response("User signed out", status=status.HTTP_200_OK)





    #
    # @action(detail=False, methods=['get'])
    # def list_user(self,request):
    #     user1 = Users.objects.all()
    #     serializer = UserSerializer(user1,many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    #
    # @action(detail=False, methods=['post'])
    # def create_user(self,request):
    #         serializer = UserSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data , status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    #
    # @action(detail=True, methods=['put'])
    # def update_user(self, request, pk=None):
    #     try:
    #         user = Users.objects.get(id=pk)
    #         serializer = UserSerializer(user, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     except Users.DoesNotExist:
    #         return Response("user not found", status=status.HTTP_404_NOT_FOUND)
    #
    #
    # @action(detail=True, methods=['delete'])
    # def destroy_user(self, request, pk=None):    # for delete recorde
    #     try:
    #         user = Users.objects.get(id=pk)
    #         user.delete()
    #         return Response("user deleted", status=status.HTTP_204_NO_CONTENT)
    #     except Users.DoesNotExist:
    #         return Response("user not found", status=status.HTTP_404_NOT_FOUND)






    # @action(detail=False, methods=['post'])
    # def user_sign_in(self, request):
    #     email = request.data.get('email')
    #     password = request.data.get('password')
    #
    #     try:
    #         user = Users.objects.get(email=email, password=password)
    #         serializer = UserSerializer(user)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     except Users.DoesNotExist:
    #         return Response("Invalid email or password", status=status.HTTP_401_UNAUTHORIZED)
    #
    #
    #
    # @action(detail=False, methods=['post'])
    # def user_sign_out(self, request):
    #     auth_token = request.META.get('HTTP_AUTHORIZATION')   # get token in header
    #     if auth_token:
    #         Token.objects.filter(key=auth_token).delete()    # clear token as system
    #         return Response("User signed out", status=status.HTTP_200_OK)
    #     else:
    #         return Response("Authentication token not provided", status=status.HTTP_400_BAD_REQUEST)








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
