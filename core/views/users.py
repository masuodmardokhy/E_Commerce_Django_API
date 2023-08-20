from tokenize import TokenError
from django.db.models import Q
from django.contrib.auth import authenticate
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from core.models.users import *
from core.serializers.users import *


# class UserRegistrationView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)  # Replace YourUserSerializer with your actual serializer
#         if serializer.is_valid():
#             user = serializer.save(password=make_password(serializer.validated_data['password']))
#             refresh = RefreshToken.for_user(user)
#             access_token = refresh.access_token
#             return Response({'access_token': str(access_token), 'refresh_token': str(refresh), 'user': serializer.data},
#                             status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            return Response({'access_token': str(access_token), 'refresh_token': str(refresh), 'user': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListView(APIView):
    permission_classes = [IsAdminUser]  # Require admin permission for access

    def get(self, request):
        queryset = Users.objects.all()

        # Filtering based on query parameters
        is_admin = request.query_params.get('is_admin')
        first_name = request.query_params.get('first_name')
        user_name = request.query_params.get('user_name')

        if is_admin is not None:
            queryset = queryset.filter(is_admin=is_admin)

        if first_name:
            queryset = queryset.filter(first_name__icontains=first_name)

        if user_name:
            queryset = queryset.filter(user_name__icontains=user_name)

        # Sorting based on query parameters
        order_by = request.query_params.get('order_by')
        if order_by == 'create':
            queryset = queryset.order_by('-create')
        elif order_by == 'first_name':
            queryset = queryset.order_by('first_name')
        elif order_by == 'is_admin':
            queryset = queryset.order_by('-is_admin')

        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

class UserProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        serializer = UserProfileUpdateSerializer(user, data=request.data, partial=True)  # Use partial=True for partial updates
        if serializer.is_valid():
            if 'password' in serializer.validated_data:
                password = serializer.validated_data.pop('password')
                user.set_password(password)  # pass change to hash
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            return Response({'access_token': str(access_token), 'user': UserSerializer(user).data})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)



class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, user_id):
        try:
            user = Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response(serializer.data)



class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.set_exp(-1)  # Set expiration time to a negative value
                return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
            except TokenError:
                return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)


class PromoteToAdminView(APIView):
    permission_classes = [IsAdminUser]  # Only admins can promote users to admin

    def put(self, request, user_id):
        try:
            user = Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user.is_admin = True
        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
