
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Blog, Dislike, Like, Comment, CustomUser

User = get_user_model()


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name',
                  'email', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True},
                        'email': {'required': True}}

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match."})

        # Validate email separately
        email = data.get('email', None)
        if not email:
            raise serializers.ValidationError(
                {"email": "This field may not be blank."})

        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        return User.objects.create_user(**validated_data)


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'profile_image',
                  'about', 'bio', 'phone_number', 'email', 'date_joined']


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name',
                  'profile_image', 'about', 'bio', 'phone_number']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class BlogSerializer(serializers.ModelSerializer):
    author_username = serializers.ReadOnlyField(source='user.username')
    pub_date = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'user', 'cover_photo', 'title', 'content', 'pub_date',
                  'image_attachment', 'video_area',
                  'likes_count', 'dislikes_count', 'comments_count', 'author_username']
        read_only_fields = ['id', 'user', 'pub_date',
                            'likes_count', 'dislikes_count', 'comments_count']

    def get_pub_date(self, obj):  # Change the method name to 'get_pub_date'
        formatted_date = obj.pub_date.strftime("%B %d, %Y")
        formatted_time = obj.pub_date.strftime("%I:%M %p")
        return f"{formatted_date} at {formatted_time}"


class RelatedBlogByAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'cover_photo', 'title', 'pub_date']
        read_only_fields = ['id', 'pub_date']


class RelatedBlogByCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'cover_photo', 'title', 'pub_date']
        read_only_fields = ['id', 'pub_date']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'pub_date']
        read_only_fields = ['id', 'user', 'pub_date']


class CommentCreateSerializer(serializers.Serializer):
    text = serializers.CharField()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'blog']
        read_only_fields = ['id', 'user', 'blog']


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = ['id', 'user', 'blog']
        read_only_fields = ['id', 'user', 'blog']
