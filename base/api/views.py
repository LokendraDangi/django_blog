from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.api.serializers import PostSerializer
from base.models import Post

@api_view(['GET'])
def getRoutes(request):
    # route_list for api
    routes=[
        'GET /api',
        'GET /api/posts',
        'GET /api/post/:id'
    ]

    return Response(routes)

@api_view(['GET'])
def getPosts(request):
    # get all post data from post model
    posts = Post.objects.all()
    # convert post list into JSON list
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPost(request,pk):
    # get post data by id
    post = Post.objects.get(id=pk)
    # convert post data list into JSON data list
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)