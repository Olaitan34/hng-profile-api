from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from datetime import datetime
import requests
from .models import UserProfile


@require_http_methods(["GET"])
def get_profile(request):
    """
    GET endpoint that returns profile information.
    """
    # Get the first user profile from the database (or create a default one)
    try:
        profile = UserProfile.objects.first()
        if not profile:
            # Create a default profile if none exists
            profile = UserProfile.objects.create(
                email="your.email@example.com",
                name="Your Name",
                stack="Python/Django"
            )
        
        user = {
            "email": profile.email,
            "name": profile.name,
            "stack": profile.stack
        }
    except Exception as e:
        # Fallback to hardcoded data if database is not available
        user = {
            "email": "your.email@example.com",
            "name": "Your Name",
            "stack": "Python/Django"
        }
    
    # Get current UTC time formatted as ISO 8601 string
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    
    # Fetch cat fact from external API
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
