from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from datetime import datetime
import requests


@require_http_methods(["GET"])
def get_profile(request):
    """
    GET endpoint that returns profile information.
    """
    # Static user profile information
    user = {
        "email": "emmfatsneh@gmail.com",
        "name": "Fatoki Olaitan",
        "stack": "Python/Django"
    }
    
    # Get current UTC time formatted as ISO 8601 string (DYNAMIC)
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    
    # Fetch cat fact from external API (DYNAMIC)
    try:
        response = requests.get('https://catfact.ninja/fact', timeout=5)
        response.raise_for_status()
        fact = response.json().get('fact', 'Could not retrieve cat fact.')
    except requests.RequestException:
        fact = 'Could not retrieve cat fact.'
    
    # Assemble the final response
    data = {
        "status": "success",
        "user": user,
        "timestamp": timestamp,
        "fact": fact
    }
    
    return JsonResponse(data, status=200)
