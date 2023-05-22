from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignUpForm

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'

    form = SignUpForm({
        'name': data.get('name'),
        'email': data.get('email'),
        'password': data.get('password'),
        'first_name': data.get('first_name'),
        'last_name': data.get('last_name')
    })

    if form.is_valid():
        form.save()

        #Work on Send Verification Email Later
    else:
        message = 'error'

    return JsonResponse({'status': message})
