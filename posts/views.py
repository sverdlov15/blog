import logging
from django.http import HttpResponse

from posts.models import Post

logger = logging.getLogger(__name__)


def index(request):
    if request.GET.get('title'):
        post_list = Post.objects.filter(title__contains=request.GET.get('title'))
    else:
        post_list = Post.objects.all()
    return HttpResponse(", migrations".join([x.title for x in post_list]))