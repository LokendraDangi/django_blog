from rest_framework.serializers import ModelSerializer
from base.models import Post

# Post class serializer to convert all post data list into JSON list
class PostSerializer(ModelSerializer):
    # it tells the Post model to use and what fields to serialize
    class Meta:
        model= Post
        # all fields of Post Model are serialized
        fields = '__all__'