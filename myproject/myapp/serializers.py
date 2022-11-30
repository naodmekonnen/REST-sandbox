from rest_framework import serializers
from .models import *


class CustomUserSerializer(serializers.ModelSerializer):
    # some_relationship_fk = SomeRelationshipSerializer(required=False)   
    class Meta:
        model = CustomUser
        fields = (
              'email',
              'username',
              'first_name',
              'last_name',
              
        ) 

        """ 
        only pull in the PROVIDED DJANGO USER FIELDS that are going to be used in creating a user, 
        and then add your extended fields,
        '__all__' pulls in all fields and creates an error for the validation step below
        """
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     password = validated_data.pop('password', None)
    #     instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
    #     if password is not None:
    #         instance.set_password(password)
    #     instance.save()
    #     return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,read_only=True)    
    
    class Meta:
        model = Post
        fields = ('name', 'body', 'created_at', 'post_type', 'author', 'comments')
        
    
class PostTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostType
        fields = '__all__'

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'

class ReadOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

