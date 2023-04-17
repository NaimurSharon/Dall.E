from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from app.models import *

from rest_framework.exceptions import NotFound

import openai
import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

OPENAI_KEY = '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'

openai.api_key = OPENAI_KEY
CLOUDINARY_API_NAME = 'ddnvj9ly8'
CLOUDINARY_API_KEY = '786182533819873'
CLOUDINARY_API_SECRET = '8Jasd6rS-pF85t_65naNAmIrYt4'


# # // Config
cloudinary.config(
    cloud_name="ddnvj9ly8",
    api_key="786182533819873",
    api_secret="8Jasd6rS-pF85t_65naNAmIrYt4",
    secure=True
)

# # // Upload
# upload("https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg",
#        public_id="olympic_flag")

# # // Transform
# url, options = cloudinary_url(
#     "olympic_flag", width=100, height=150, crop="fill")


@api_view(['POST', 'GET'])
def postAPI(request):
    if request.method == 'POST':
        try:
            prompt = request.data['prompt']

            response = openai.Image.create(
                prompt=request.data['prompt'],
                size='1024x1024',
            )
            img_url = response["data"][0]["url"]

            serializer = PostSerializer(data={"name": request.data["name"], "prompt": request.data["prompt"],
                                              "photo": img_url})
            if serializer.is_valid():
                serializer.save()
        except Exception as e:
            return Response({'error': str(e)}, status=500)
    if request.method == 'GET':
        item = Post.objects.all()
        serializer = PostSerializer(item, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def photoAPI(request):
    if request.method == 'POST':
        try:
            photo_uploader = upload(request.data['photo'],
                                    public_id=request.data['name'])
            serializer = photoSerializer(
                data={"name": photo_uploader["public_id"], "photo": photo_uploader["secure_url"], "prompt": request.data["prompt"]})
            if serializer.is_valid():
                serializer.save()

        except Exception as e:
            return Response({'error': str(e)}, status=500)
    if request.method == 'GET':
        item = Photo.objects.all()
        print(item)
        serializer = photoSerializer(item, many=True)
    return Response(serializer.data)
