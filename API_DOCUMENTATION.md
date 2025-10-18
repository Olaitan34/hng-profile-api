# HNG Profile API - Documentation

## Overview

The HNG Profile API is a RESTful web service built with Django that provides user profile information, real-time timestamps, and random cat facts. This API demonstrates integration with external APIs, database management, and deployment best practices.

**Base URL:** `https://hng-profile-api.onrender.com`

**Version:** 1.0.0

**Author:** HNG Internship Cohort

---

## Table of Contents

1. [Authentication](#authentication)
2. [Endpoints](#endpoints)
3. [Request/Response Format](#requestresponse-format)
4. [Error Handling](#error-handling)
5. [Rate Limiting](#rate-limiting)
6. [Examples](#examples)
7. [Status Codes](#status-codes)

---

## Authentication

Currently, this API does not require authentication. All endpoints are publicly accessible.

---

## Endpoints

### Get Profile Information

Retrieves user profile information along with a timestamp and a random cat fact.

**Endpoint:** `/me`

**Method:** `GET`

**Headers:** None required

**Query Parameters:** None

**Success Response:**

- **Code:** 200 OK
- **Content-Type:** `application/json`

**Response Schema:**

```json
{
  "status": "string",
  "user": {
    "email": "string",
    "name": "string",
    "stack": "string"
  },
  "timestamp": "string (ISO 8601 format)",
  "fact": "string"
}
```

**Response Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | Status of the request (always "success" for 200 responses) |
| `user.email` | string | User's email address |
| `user.name` | string | User's full name |
| `user.stack` | string | Technology stack (e.g., "Python/Django") |
| `timestamp` | string | Current UTC time in ISO 8601 format (YYYY-MM-DDTHH:MM:SS.sssZ) |
| `fact` | string | Random cat fact fetched from external API |

---

## Request/Response Format

### Sample Request

```bash
curl -X GET https://hng-profile-api.onrender.com/me
```

### Sample Response

```json
{
  "status": "success",
  "user": {
    "email": "developer@example.com",
    "name": "John Doe",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-18T14:30:45.123Z",
  "fact": "Cats sleep for 70% of their lives."
}
```

---

## Error Handling

### Error Response Format

```json
{
  "status": "error",
  "message": "Error description",
  "code": "ERROR_CODE"
}
```

### Common Errors

| Status Code | Error Message | Description |
|-------------|---------------|-------------|
| 405 | Method Not Allowed | Only GET requests are accepted |
| 500 | Internal Server Error | Server-side error occurred |
| 503 | Service Unavailable | External API (cat facts) is unavailable |

### Example Error Response

```json
{
  "detail": "Method \"POST\" not allowed."
}
```

---

## Rate Limiting

Currently, there are no rate limits imposed on this API. However, please use the API responsibly to avoid overwhelming the server.

**Recommendations:**
- Cache responses where possible
- Implement exponential backoff for retries
- Respect HTTP status codes

---

## Examples

### Using cURL

```bash
# Basic request
curl https://hng-profile-api.onrender.com/me

# Pretty print with jq
curl https://hng-profile-api.onrender.com/me | jq

# Save response to file
curl https://hng-profile-api.onrender.com/me -o response.json

# Include response headers
curl -i https://hng-profile-api.onrender.com/me
```

### Using Python

```python
import requests

# Make GET request
response = requests.get('https://hng-profile-api.onrender.com/me')

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    print(f"Name: {data['user']['name']}")
    print(f"Email: {data['user']['email']}")
    print(f"Stack: {data['user']['stack']}")
    print(f"Timestamp: {data['timestamp']}")
    print(f"Cat Fact: {data['fact']}")
else:
    print(f"Error: {response.status_code}")
```

### Using JavaScript (Fetch API)

```javascript
// Using fetch
fetch('https://hng-profile-api.onrender.com/me')
  .then(response => response.json())
  .then(data => {
    console.log('User:', data.user);
    console.log('Timestamp:', data.timestamp);
    console.log('Cat Fact:', data.fact);
  })
  .catch(error => console.error('Error:', error));

// Using async/await
async function getProfile() {
  try {
    const response = await fetch('https://hng-profile-api.onrender.com/me');
    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error('Error:', error);
  }
}

getProfile();
```

### Using Postman

1. Open Postman
2. Create a new request
3. Set method to `GET`
4. Enter URL: `https://hng-profile-api.onrender.com/me`
5. Click "Send"
6. View the JSON response in the response pane

---

## Status Codes

| Status Code | Meaning | Description |
|-------------|---------|-------------|
| 200 | OK | Request successful, profile data returned |
| 405 | Method Not Allowed | HTTP method not supported (only GET allowed) |
| 500 | Internal Server Error | Server encountered an unexpected error |
| 503 | Service Unavailable | Server temporarily unable to handle request |

---

## Data Validation

### Timestamp Format

- **Format:** ISO 8601 (YYYY-MM-DDTHH:MM:SS.sssZ)
- **Timezone:** UTC (indicated by 'Z')
- **Precision:** Milliseconds
- **Example:** `2025-10-18T14:30:45.123Z`

### Dynamic Data

The following fields are **dynamically generated** on each request:

1. **timestamp** - Generated at request time using `datetime.utcnow()`
2. **fact** - Fetched from [Cat Facts Ninja API](https://catfact.ninja/fact) on each request

### Static Data

The following fields are **static** (configured in the application):

1. **user.email** - Set in application configuration
2. **user.name** - Set in application configuration
3. **user.stack** - Set in application configuration

---

## Performance Considerations

### Response Time

- **Average:** 200-500ms (first request after sleep may take 30-60 seconds)
- **Factors:**
  - External API call to cat facts service
  - Database query (if using UserProfile model)
  - Server cold start (Render free tier)

### Caching

- No caching is currently implemented
- Each request fetches fresh data
- Timestamp and cat facts are always unique

---

## CORS Policy

**CORS is enabled** for this API, allowing cross-origin requests from web browsers.

**Allowed Methods:** GET

**Allowed Headers:** Standard headers

**Configuration:** Managed via `django-cors-headers`

---

## External Dependencies

This API integrates with the following external services:

### Cat Facts Ninja API

- **URL:** https://catfact.ninja/fact
- **Purpose:** Provides random cat facts
- **Timeout:** 5 seconds
- **Fallback:** Returns "Could not retrieve cat fact." on failure

---

## Changelog

### Version 1.0.0 (2025-10-18)

- Initial release
- GET `/me` endpoint
- User profile information
- Real-time timestamp generation
- Cat facts integration
- Deployed on Render.com
- PostgreSQL database (Railway)

---

## Support & Contact

- **GitHub Repository:** https://github.com/Olaitan34/hng-profile-api
- **Issues:** https://github.com/Olaitan34/hng-profile-api/issues
- **Documentation:** https://github.com/Olaitan34/hng-profile-api/blob/main/API_DOCUMENTATION.md

---

## Testing

### Manual Testing

```bash
# Test the endpoint
curl https://hng-profile-api.onrender.com/me

# Verify status is "success"
curl https://hng-profile-api.onrender.com/me | jq '.status'

# Verify timestamp format (ISO 8601)
curl https://hng-profile-api.onrender.com/me | jq '.timestamp'

# Check response time
curl -w "\nTime: %{time_total}s\n" https://hng-profile-api.onrender.com/me
```

### Automated Testing

The project includes Django test cases in `api/tests.py`:

```bash
# Run all tests
python manage.py test api

# Run with verbosity
python manage.py test api --verbosity=2
```

---

## Security

### HTTPS

- All requests are served over HTTPS
- TLS/SSL encryption enabled by default (Render)

### Security Headers

- `X-Frame-Options: DENY`
- `X-Content-Type-Options: nosniff`
- `Secure` cookie flags in production

### Data Privacy

- No personal data is stored from API consumers
- User profile data is static/configured
- No tracking or analytics

---

## Limitations

1. **Free Tier Hosting (Render):**
   - Service spins down after 15 minutes of inactivity
   - First request after sleep: 30-60 seconds response time
   
2. **External API Dependency:**
   - Cat facts may be unavailable if external API fails
   - Fallback message returned on failure

3. **No Authentication:**
   - All endpoints are publicly accessible
   - No user-specific data

---

## Future Enhancements

- [ ] Add more endpoints (e.g., `/health`, `/version`)
- [ ] Implement caching for cat facts
- [ ] Add request logging and analytics
- [ ] API versioning (e.g., `/v1/me`)
- [ ] Rate limiting per IP
- [ ] API key authentication (optional)
- [ ] WebSocket support for real-time updates
- [ ] Additional profile fields

---

## License

This API is open source and available under the MIT License.

---

**Last Updated:** October 18, 2025

**API Version:** 1.0.0
