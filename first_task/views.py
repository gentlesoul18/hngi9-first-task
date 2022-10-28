from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def details(request):
    return Response({"slackUsername": "Gentlesoul", "backend": True, "Age": 22, "bio": "Gentlesoul is a backend developer but note the small 'in-view' because i am still a beginner"})