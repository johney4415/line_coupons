from django.http.response import JsonResponse


def test(request):
    return JsonResponse(data={'response': 'succeess'})
