# Configuration File for Portfolio Website

# ==========================================
# BRANDING & CUSTOMIZATION
# ==========================================

# Website Name
WEBSITE_NAME = "Portfolio Pro"
TAGLINE = "Premium Creative Solutions"

# Colors (Update CSS variables in style.css for visual effect)
PRIMARY_COLOR = "#6366f1"        # Indigo
SECONDARY_COLOR = "#ec4899"      # Pink
ACCENT_COLOR = "#06b6d4"         # Cyan
DARK_BG = "#0f172a"              # Dark Navy
LIGHT_BG = "#f8fafc"             # Light Slate

# ==========================================
# CONTACT INFORMATION
# ==========================================

BUSINESS_NAME = "Portfolio Pro"
BUSINESS_EMAIL = "hello@portfoliopro.com"
BUSINESS_PHONE = "+91 99999 99999"
WHATSAPP_NUMBER = "919999999999"      # Format: country code + number (no +)
TELEGRAM_USERNAME = "@portfoliopro"
BUSINESS_ADDRESS = "Mumbai, India"

# ==========================================
# SERVICES & PRICING
# ==========================================

# Video Editing Service
VIDEO_EDITING_STARTER = 5000
VIDEO_EDITING_PRO = 12000
VIDEO_EDITING_PREMIUM = 25000

# Photo Editing Service
PHOTO_EDITING_STARTER = 2000
PHOTO_EDITING_PRO = 5000
PHOTO_EDITING_ENTERPRISE = 10000

# YouTube Management Service
YOUTUBE_STARTER = 8000
YOUTUBE_GROWTH = 15000
YOUTUBE_PREMIUM = 30000

# ==========================================
# FLASK CONFIGURATION
# ==========================================

# Secret Key (CHANGE THIS IN PRODUCTION!)
SECRET_KEY = "your-secret-key-change-this-in-production-12345"

# Database
DATABASE_URL = "sqlite:///users.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Flask Settings
DEBUG = True                    # Set to False in production
HOST = "0.0.0.0"
PORT = 5000
TESTING = False

# ==========================================
# SOCIAL MEDIA LINKS
# ==========================================

TWITTER_URL = "https://twitter.com/portfoliopro"
LINKEDIN_URL = "https://linkedin.com/company/portfoliopro"
GITHUB_URL = "https://github.com/portfoliopro"
INSTAGRAM_URL = "https://instagram.com/portfoliopro"
YOUTUBE_URL = "https://youtube.com/@portfoliopro"

# ==========================================
# PORTFOLIO IMAGES
# ==========================================

# Unsplash Image URLs (Free images)
PORTFOLIO_IMAGES = [
    "https://images.unsplash.com/photo-1561070791-2526d30994b5?w=600&h=600&fit=crop",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=600&h=600&fit=crop",
    "https://images.unsplash.com/photo-1552664730-d307ca884978?w=600&h=600&fit=crop",
    "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=600&h=600&fit=crop",
]

# YouTube Video IDs (Replace with your video IDs)
YOUTUBE_VIDEOS = [
    "dQw4w9WgXcQ",  # Video 1
    "dQw4w9WgXcQ",  # Video 2
    "dQw4w9WgXcQ",  # Video 3
]

# ==========================================
# ANALYTICS (Optional - Add later)
# ==========================================

# Google Analytics ID
GOOGLE_ANALYTICS_ID = "G-XXXXXXXXXX"

# Hotjar ID
HOTJAR_ID = "XXXXXXXXX"

# ==========================================
# EMAIL CONFIGURATION (Optional - Add later)
# ==========================================

# SMTP Settings for sending emails
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = "your-email@gmail.com"
MAIL_PASSWORD = "your-app-password"

# ==========================================
# FEATURE FLAGS
# ==========================================

ENABLE_EMAIL_NOTIFICATIONS = False     # Send email on new contact
ENABLE_SMS_NOTIFICATIONS = False       # Send SMS on new contact
ENABLE_DARK_MODE = True                # Dark mode toggle
ENABLE_CART_SYSTEM = False             # Shopping cart for services
ENABLE_BLOG = False                    # Blog section

# ==========================================
# LIMITS & SETTINGS
# ==========================================

# Rate limiting
MAX_LOGIN_ATTEMPTS = 5
LOGIN_ATTEMPT_TIMEOUT = 300            # 5 minutes in seconds

# File upload
MAX_FILE_SIZE = 5242880                # 5MB in bytes
ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png', 'gif', 'pdf']

# Session
SESSION_TIMEOUT = 3600                 # 1 hour in seconds
SESSION_REFRESH = True

# ==========================================
# DEPLOYMENT SETTINGS
# ==========================================

# Production URLs
PRODUCTION_URL = "https://your-domain.com"
ENVIRONMENT = "development"            # 'development' or 'production'

# CORS Settings (if needed)
CORS_ORIGINS = ["http://localhost:5000", "https://your-domain.com"]

# Security Headers
SECURITY_HEADERS = {
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'SAMEORIGIN',
    'X-XSS-Protection': '1; mode=block',
}

# ==========================================
# LOGGING
# ==========================================

LOG_LEVEL = "INFO"                     # DEBUG, INFO, WARNING, ERROR
LOG_FILE = "app.log"
MAX_LOG_SIZE = 10485760               # 10MB in bytes

# ==========================================
# NOTES FOR IMPLEMENTATION
# ==========================================

"""
To use this configuration file in Flask:

1. In app.py, add:
   from config import *
   app.config.from_object('config')

2. Or import specific values:
   from config import SECRET_KEY, BUSINESS_EMAIL

3. In HTML files, pass variables:
   @app.context_processor
   def inject_config():
       return dict(BUSINESS_EMAIL=BUSINESS_EMAIL, BUSINESS_PHONE=BUSINESS_PHONE)

4. In HTML:
   <a href="mailto:{{ BUSINESS_EMAIL }}">Email Us</a>
"""
