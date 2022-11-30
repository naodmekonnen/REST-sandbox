from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birthday = models.DateField(null=True)

    def __str__(self):
        return self.username

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



class PostType(models.Model):
    name = models.CharField(max_length=225)

    def __str__ (self):
        return self.name


class Follow(models.Model):
    following_user_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='following')
    follower_user_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='follower')


class Post(models.Model):
    name = models.CharField(max_length=225)
    body = models.CharField(max_length=550)
    created_at = models.DateTimeField()
    post_type = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='post_tag')
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='user')
    # comment = models.ForeignKey(Comment, on_delete=models.PROTECT,null=True)

    
    def __str__ (self):
        return self.name + ' ' + self.body


class Comment(models.Model):
    user_comment = models.ForeignKey('Post',on_delete=models.CASCADE,related_name='post_comments')    
    # body = models.CharField(max_length=225)
    text = models.CharField(max_length=500, null=True)
    post_id = models.ForeignKey(Post, on_delete=models.PROTECT)
    user_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.name + ' ' + self.body


# class Post(models.Model):
#     id = models.UUIDField(primary_key=True,
#                           default=uuid.uuid4,
#                           editable=False)
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name='user_posts'
#     )
#     photo = models.ImageField(
#         upload_to=image_file_path,
#         blank=False,
#         editable=False)
#     text = models.TextField(max_length=500, blank=True)
#     location = models.CharField(max_length=30, blank=True)
#     posted_on = models.DateTimeField(auto_now_add=True)
#     likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
#                                    related_name="likers",
#                                    blank=True,
#                                    symmetrical=False)

#     class Meta:
#         ordering = ['-posted_on']

#     def number_of_likes(self):
#         if self.likes.count():
#             return self.likes.count()
#         else:
#             return 0

#     def __str__(self):
#         return f'{self.author}\'s post'


# class Comment(models.Model):
#     post = models.ForeignKey('Post',
#                              on_delete=models.CASCADE,
#                              related_name='post_comments')
#     author = models.ForeignKey(settings.AUTH_USER_MODEL,
#                                on_delete=models.CASCADE,
#                                related_name='user_comments')
#     text = models.CharField(max_length=100)
#     posted_on = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ['-posted_on']

#     def __str__(self):
#         return f'{self.author}\'s comment'