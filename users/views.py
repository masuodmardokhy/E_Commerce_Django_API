from rest_framework.response import Response
from rest_framework import status                      # for show messages
from rest_framework import viewsets , permissions      # viewsets for class base view
from .serializers import *



# WE USE VIEWSETS AND AT THE END OF THESE CODES  , WE CREATED THIS CLASS USING APIVIEW AND COMMENTED IT.
class UserViewSet(viewsets.ViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    def list(self,request):
        user = Users.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):  # for find recorde
        try:
            user = Users.objects.get(id=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response("user not found", status=status.HTTP_404_NOT_FOUND)


    def update(self, request, pk=None):
        try:
            user = Users.objects.get(id=pk)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Users.DoesNotExist:
            return Response("user not found", status=status.HTTP_404_NOT_FOUND)


    def destroy(self, request, pk=None):    # for delete recorde
        try:
            user = Users.objects.get(id=pk)
            user.delete()
            return Response("user deleted", status=status.HTTP_204_NO_CONTENT)
        except Users.DoesNotExist:
            return Response("user not found", status=status.HTTP_404_NOT_FOUND)








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
