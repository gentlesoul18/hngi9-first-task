from django.http import JsonResponse


def details(request):
    output = {"slackUsername": "Gentlesoul", "backend": True, "Age": 22, "bio": "Gentlesoul is a backend developer but note the small 'in-view' because i am still a beginner"}

    return JsonResponse(output)