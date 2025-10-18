# HNG Profile API

A Django REST API that returns user profile information along with a random cat fact and current timestamp.

## Live Demo

**API Endpoint:** [https://hng-profile-api.onrender.com/me](https://hng-profile-api.onrender.com/me)

## Features

- Returns user profile information (email, name, stack)
- Fetches random cat facts from external API
- Generates real-time ISO 8601 timestamps
- CORS enabled for cross-origin requests
- PostgreSQL database support
- Deployed on Render with Railway PostgreSQL

## API Response Format

```json
{
  "status": "success",
  "user": {
    "email": "your.email@example.com",
    "name": "Your Name",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-18T12:34:56.789Z",
  "fact": "A random cat fact appears here..."
}
```

## Tech Stack

- **Backend Framework:** Django 5.2.7
- **Server:** Gunicorn
- **Database:** PostgreSQL (Railway)
- **Static Files:** WhiteNoise
- **External API:** Cat Facts Ninja API
- **Deployment:** Render.com

## Prerequisites

- Python 3.12 or higher
- Git
- PostgreSQL (for production) or SQLite (for local development)

## Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Olaitan34/hng-profile-api.git
cd hng-profile-api
```

### 2. Create Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the project root:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (optional - uses SQLite by default)
# DATABASE_URL=postgresql://user:password@host:port/dbname

# CORS Settings (optional)
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

**Generate a SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Start Development Server

```bash
python manage.py runserver
```

Visit: [http://localhost:8000/me](http://localhost:8000/me)

## Project Structure

```
hng-profile-api/
├── api/                      # Main API app
│   ├── models.py            # UserProfile model
│   ├── views.py             # API endpoint logic
│   ├── urls.py              # API URL routing
│   └── admin.py             # Admin configuration
├── profile_project/         # Django project settings
│   ├── settings.py          # Main settings
│   ├── urls.py              # Root URL configuration
│   └── wsgi.py              # WSGI configuration
├── build.sh                 # Render build script
├── Procfile                 # Process file for deployment
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (local)
├── .gitignore              # Git ignore rules
└── manage.py               # Django management script
```

## Dependencies

```
Django>=5.0,<6.0
requests>=2.31.0
django-cors-headers>=4.3.0
gunicorn>=21.2.0
whitenoise>=6.6.0
python-dotenv>=1.0.0
psycopg2-binary>=2.9.9
dj-database-url>=2.1.0
```

## Deployment

### Deploy to Render.com

1. **Fork/Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Create Render Account**
   - Sign up at [render.com](https://render.com)
   - Connect your GitHub account

3. **Create Web Service**
   - Click "New +" → "Web Service"
   - Select your repository
   - Configure:
     - **Build Command:** `./build.sh`
     - **Start Command:** `gunicorn profile_project.wsgi:application`
     - **Instance Type:** Free

4. **Set Environment Variables**
   ```
   SECRET_KEY=<your-secret-key>
   DEBUG=False
   ALLOWED_HOSTS=your-app.onrender.com
   DATABASE_URL=<your-postgresql-url>
   PYTHON_VERSION=3.12.2
   ```

5. **Deploy**
   - Click "Create Web Service"
   - Wait for build to complete
   - Access your API at: `https://your-app.onrender.com/me`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/me`    | Returns user profile with timestamp and cat fact |

### Example Request

```bash
curl https://hng-profile-api.onrender.com/me
```

### Example Response

```json
{
  "status": "success",
  "user": {
    "email": "your.email@example.com",
    "name": "Your Name",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-18T14:25:33.789Z",
  "fact": "Cats can jump up to six times their length."
}
```

## Configuration

### Update User Profile

Edit `api/views.py` to update your profile information:

```python
user = {
    "email": "your.email@example.com",
    "name": "Your Name",
    "stack": "Python/Django"
}
```

### CORS Configuration

To allow requests from specific domains, update `CORS_ALLOWED_ORIGINS` in `settings.py` or `.env`:

```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://your-frontend.com",
]
```

## Testing

### Manual Testing

```bash
# Using curl
curl http://localhost:8000/me

# Using Python
python -c "import requests; print(requests.get('http://localhost:8000/me').json())"
```

### Run Django Tests

```bash
python manage.py test api
```

## Troubleshooting

### Common Issues

**1. ModuleNotFoundError**
```bash
pip install -r requirements.txt
```

**2. Database Connection Error (Local)**
- Comment out `DATABASE_URL` in `.env` to use SQLite

**3. CSRF/CORS Errors**
- Check `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` in settings
- Verify `CORS_ALLOWED_ORIGINS` includes your frontend domain

**4. Static Files Not Loading**
```bash
python manage.py collectstatic --noinput
```

**5. Render Free Tier Cold Start**
- First request after inactivity takes 30-60 seconds
- App spins down after 15 minutes of no traffic

## Notes

- **Free Tier Limitation:** Render free tier spins down after 15 minutes of inactivity
- **Database:** Uses Railway PostgreSQL (ensure public URL is accessible)
- **Timestamp:** Generated dynamically on each request in ISO 8601 format
- **Cat Facts:** Fetched from [catfact.ninja](https://catfact.ninja) API

## Environment Variables Reference

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `SECRET_KEY` | Yes | - | Django secret key |
| `DEBUG` | No | False | Debug mode (True/False) |
| `ALLOWED_HOSTS` | No | localhost,127.0.0.1 | Comma-separated allowed hosts |
| `DATABASE_URL` | No | SQLite | PostgreSQL connection string |
| `CORS_ALLOWED_ORIGINS` | No | http://localhost:3000 | Comma-separated CORS origins |
| `PYTHON_VERSION` | No | 3.12.2 | Python version (Render) |

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

- **GitHub:** [@Olaitan34](https://github.com/Olaitan34)
- **Repository:** [hng-profile-api](https://github.com/Olaitan34/hng-profile-api)

## Acknowledgments

- Cat facts provided by [Cat Facts Ninja API](https://catfact.ninja)
- Hosted on [Render.com](https://render.com)
- Database hosted on [Railway](https://railway.app)

---

**Built with ❤️ using Django**
