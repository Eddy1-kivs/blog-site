from rest_framework import serializers
from django.db import IntegrityError
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer, BlogSerializer, LoginSerializer, UserProfileSerializer, UserProfileUpdateSerializer, RelatedBlogByAuthorSerializer, RelatedBlogByCategorySerializer, CommentSerializer, CommentCreateSerializer, LikeSerializer, DislikeSerializer, CategorySerializer
from .models import CustomUser, Blog, Category, Dislike, Like, Comment, Category
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import authentication_classes, permission_classes


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 6  # Adjust the page size as needed
    page_size_query_param = 'page_size'
    max_page_size = 20


@api_view(["OPTIONS", "POST"])
@authentication_classes([])
@permission_classes([])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            # Generate a token for the user
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token), 'user_id': user.id}, status=status.HTTP_201_CREATED)

        except IntegrityError:
            return Response({'error': 'Username or email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as e:
            # Extract validation errors and return them in JSON format
            errors = dict(e.detail)
            return Response({'error': errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def login_view(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({'refresh': str(refresh), 'access': str(refresh.access_token), 'user_id': user.id, 'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    # Get the user profile for the authenticated user
    user = request.user
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user

    if request.method == 'GET':
        # Retrieve the user profile for the authenticated user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Update the user profile
        serializer = UserProfileUpdateSerializer(
            user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_blog(request):
    if request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            # Save the user along with the blog
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@authentication_classes([])  
@permission_classes([]) 
def all_blogs(request):
    """
    Retrieve all blog posts.
    """
    paginator = CustomPageNumberPagination()
    blogs = Blog.objects.all().order_by('-pub_date') 
    result_page = paginator.paginate_queryset(blogs, request)
    serializer = BlogSerializer(
        result_page, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
@authentication_classes([])  
@permission_classes([]) 
def all_categories(request):
    """
    Retrieve all categories.
    """
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_blogs(request):
    """
    Retrieve blogs posted by the authenticated user.
    """
    paginator = CustomPageNumberPagination()
    user_blogs = Blog.objects.filter(user=request.user).order_by(
        '-pub_date')  # Add ordering by created_at
    result_page = paginator.paginate_queryset(user_blogs, request)
    serializer = BlogSerializer(
        result_page, many=True, context={'request': request})
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    serializer = BlogSerializer(blog, context={'request': request})
    serialized_data = serializer.data

    # Include related blogs by author and category as before
    related_blogs_by_author = Blog.objects.filter(
        user=blog.user).exclude(id=blog_id)[:3]
    related_by_author_serializer = RelatedBlogByAuthorSerializer(
        related_blogs_by_author, many=True)
    related_blogs_by_category = Blog.objects.filter(
        category=blog.category).exclude(id=blog_id)[:3]
    related_by_category_serializer = RelatedBlogByCategorySerializer(
        related_blogs_by_category, many=True)
    serialized_data['related_by_author'] = related_by_author_serializer.data
    serialized_data['related_by_category'] = related_by_category_serializer.data

    # Include comments for the blog
    comments = Comment.objects.filter(blog=blog)
    comment_serializer = CommentSerializer(comments, many=True)
    serialized_data['comments'] = comment_serializer.data

    return Response(serialized_data)





@api_view(['GET'])
@permission_classes([AllowAny])
def blogs_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    blogs = Blog.objects.filter(category=category)
    serializer = BlogSerializer(blogs, many=True, context={'request': request})
    return Response(serializer.data)


# api/views.py


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_comment(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    user = request.user

    serializer = CommentCreateSerializer(data=request.data)
    if serializer.is_valid():
        text = serializer.validated_data['text']
        comment = Comment.objects.create(blog=blog, user=user, text=text)

        # Retrieve all comments for the blog, including the new one
        comments = Comment.objects.filter(blog=blog)
        comment_serializer = CommentSerializer(comments, many=True)

        return Response({'new_comment': CommentSerializer(comment).data, 'all_comments': comment_serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    user = request.user

    # Check if the user has already liked the blog
    existing_like = Like.objects.filter(blog=blog, user=user).first()

    if existing_like:
        # User has already liked, so unlike
        existing_like.delete()
        return Response({'message': 'Blog unliked successfully'})

    # User has not liked, so create a like
    like = Like.objects.create(blog=blog, user=user)
    serializer = LikeSerializer(like)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def dislike_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    user = request.user

    # Check if the user has already disliked the blog
    existing_dislike = Dislike.objects.filter(blog=blog, user=user).first()

    if existing_dislike:
        # User has already disliked, so undislike
        existing_dislike.delete()
        return Response({'message': 'Blog undisliked successfully'})

    # User has not disliked, so create a dislike
    dislike = Dislike.objects.create(blog=blog, user=user)
    serializer = DislikeSerializer(dislike)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_likes(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    likes = Like.objects.filter(blog=blog)
    serializer = LikeSerializer(likes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_dislikes(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    dislikes = Dislike.objects.filter(blog=blog)
    serializer = DislikeSerializer(dislikes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_comments(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = Comment.objects.filter(blog=blog)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_likes_count(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    likes_count = Like.objects.filter(blog=blog).count()
    return Response({'likes_count': likes_count})


@api_view(['GET'])
@permission_classes([AllowAny])
def get_dislikes_count(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    dislikes_count = Dislike.objects.filter(blog=blog).count()
    return Response({'dislikes_count': dislikes_count})


@api_view(['GET'])
@permission_classes([AllowAny])
def get_comments_count(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    comments_count = Comment.objects.filter(blog=blog).count()
    return Response({'comments_count': comments_count})


@api_view(['GET'])
def getData(request):
    person = {'name': 'eddy', 'age': '21'}
    return Response(person)

