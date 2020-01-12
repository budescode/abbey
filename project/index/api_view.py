from .models import Post, Comment
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from .serializers import PostSerializer, UserSerializer, LoginSerializer, CommentSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.utils.decorators import method_decorator


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = PostSerializer
    def get_queryset(self):
        print('yeahh agaun', self.request.user)
        return Post.objects.all().order_by('-id')

@method_decorator(csrf_exempt, name='dispatch')
class DetailView(generics.ListAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    lookup_field = 'pk'
    serializer_class = PostSerializer
    # 	pagination_class = PostLimitOffsetPagination
    def get_queryset(self):
	    id = self.request.GET.get('id')
	    qs = Post.objects.all()
	    if id is not None:
	        qs1 = qs.filter(id=id)
	        qs = qs1
	        return qs
	    return qs

@method_decorator(csrf_exempt, name='dispatch')
class CommentListView(generics.ListAPIView):
    permission_classes = [
        permissions.AllowAny
    ]
    lookup_field = 'pk'
    serializer_class = CommentSerializer
    # 	pagination_class = PostLimitOffsetPagination
    def get_queryset(self):
	    id = self.request.GET.get('id')
	    qs = Comment.objects.all()
	    if id is not None:
	        qs1 = qs.filter(post=id)
	        qs = qs1
	        return qs
	    return qs

@method_decorator(csrf_exempt, name='dispatch')
class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    def perform_create(self, serializer):
        id = self.request.GET.get('id')
        post = Post.objects.get(id=id)
        print(self.request.user.username, 'postedddd', id)
        serializer.save(user=self.request.user, post=post)


@method_decorator(csrf_exempt, name='dispatch')
class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = PostSerializer(queryset, many=True)
    #     return Response(serializer.data)
    def perform_create(self, serializer):
        print(self.request.user.username, 'postedddd')
        serializer.save(user=self.request.user, username=self.request.user.username)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        print(serializer.is_valid())
        print(request.data)
        if serializer.is_valid():
            print(user_form.password, 'passwordddd')
            user_form = serializer.save()
            # user_form.set_password(user_form.password)
            # user_form.save()
            print('user created')
            user = User.objects.get(pk=user_form.pk)
            user_token = Token.objects.get_or_create(user=user)
            user_token = user_token[0]
            user_token = user_token.key
            print('na the key br this '+user_token)
            return Response({'key': user_token}, status=status.HTTP_201_CREATED)
        else:
            context = {'code' : 'error', 'response' : serializer.errors}
            return JsonResponse(context)


class LoginViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LoginSerializer
    # def post(self, request, format=None):


# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data["user"]
#         django_login(request, user)
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({"token": token.key}, status=200)
