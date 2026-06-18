# portfolio
# Portfolio Website - Complete Setup Guide

## 🚀 Quick Start

### 1. Install Python Requirements
```bash
pip install -r requirements.txt
```

### 2. Run the Flask Server
```bash
python app.py
```

### 3. Open in Browser
```
http://localhost:5000
```

## 📁 Project Structure

```
dheeraj/
├── app.py                 # Flask backend with authentication
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # HTML files
│   ├── login.html        # Login page
│   ├── signup.html       # Signup page
│   ├── home.html         # Home page
│   ├── services.html     # Services page
│   └── contact.html      # Contact page
├── static/
│   ├── style.css         # All CSS styling
│   └── script.js         # Client-side JavaScript
└── users.db             # SQLite database (auto-created)
```

## 🔐 Authentication Features

✅ **Secure Login System**
- Email + Password authentication
- Password hashing with Werkzeug
- Session-based authentication
- Protected routes (login_required decorator)

✅ **User Registration**
- Email validation
- Password confirmation
- Minimum password length (6 characters)
- Duplicate email prevention

✅ **Session Management**
- User sessions stored securely
- Logout functionality
- Automatic redirection to login if not authenticated

## 🎨 Design Features

### Glassmorphism UI
- Frosted glass effects
- Semi-transparent backgrounds
- Backdrop blur effects

### Animations
- Smooth fade-in animations
- Scroll-triggered animations
- Hover effects with transforms
- Counter animations for stats
- Floating shapes in background

### Responsive Design
- Mobile-first approach
- Tablet optimizations
- Desktop enhancements
- Hamburger menu on mobile
- Flexible grid layouts

## 🛠️ Technology Stack

**Frontend:**
- HTML5 (Semantic markup)
- CSS3 (Advanced animations & effects)
- Vanilla JavaScript (No dependencies)
- Font Awesome Icons
- Google Fonts (System fonts fallback)

**Backend:**
- Python Flask
- SQLAlchemy ORM
- SQLite Database
- Werkzeug (Security)

## 📄 Pages Overview

### 1. Login Page (`/login`)
- Email and password inputs
- Form validation
- Error messages
- Link to signup page
- Guest access option

### 2. Signup Page (`/signup`)
- Email registration
- Password confirmation
- Form validation
- Link to login page

### 3. Home Page (`/home`)
- Split hero section (Designer × Coder)
- Hero image with reveal effect
- Stats section with counter animation
- Featured work portfolio grid
- YouTube video showcase
- Tools & technologies section
- Call-to-action section

### 4. Services Page (`/services`)
- Video Editing service with 3 pricing tiers
- Photo Editing service with 3 pricing tiers
- YouTube Management service with 3 pricing tiers
- FAQ section
- WhatsApp integration for payments

### 5. Contact Page (`/contact`)
- Contact form with validation
- Contact information display
- WhatsApp, Email, Telegram buttons
- Embedded Google Map
- Multiple CTA buttons

## 🎯 Key Features

### Security
✅ Secure password hashing
✅ Session-based authentication
✅ CSRF protection ready (add in production)
✅ Protected routes with login_required decorator
✅ SQL injection prevention via SQLAlchemy

### User Experience
✅ Smooth animations and transitions
✅ Responsive design (Mobile, Tablet, Desktop)
✅ Fast loading times
✅ Accessible navigation
✅ WhatsApp integration for quick contact
✅ Floating action button

### Performance
✅ Minimal JavaScript (Vanilla JS, no frameworks)
✅ CSS animations (GPU accelerated)
✅ Optimized images
✅ Debounced event listeners
✅ Lazy loading ready

## 🔧 Configuration

### Change Secret Key (Important for Production!)
Edit `app.py` line 10:
```python
app.config['SECRET_KEY'] = 'your-unique-secret-key-here'
```

### Update WhatsApp Number
Update in HTML files (contact.html, services.html, home.html):
```html
<!-- Replace 919999999999 with your WhatsApp number -->
https://wa.me/919999999999
```

### Update Contact Information
Edit in `templates/contact.html`:
- Email address
- Phone number
- WhatsApp number
- Telegram handle
- Office location

## 📱 WhatsApp Integration

The website includes WhatsApp integration:
- **Floating WhatsApp button** on all pages
- **Service inquiry buttons** on services page
- **Contact form integration** on contact page
- Click to start a chat directly from the website

## 🎓 Learning Points

This project demonstrates:

1. **Full-Stack Development**
   - Backend: Flask REST APIs
   - Frontend: Responsive HTML/CSS/JS
   - Database: SQLAlchemy ORM

2. **Authentication Flow**
   - User registration with validation
   - Login with password hashing
   - Session management
   - Protected routes

3. **Modern UI/UX**
   - Glassmorphism design
   - Smooth animations
   - Responsive layouts
   - Accessibility considerations

4. **Best Practices**
   - Clean code structure
   - Separation of concerns
   - DRY (Don't Repeat Yourself)
   - Progressive enhancement
   - Mobile-first design

## 🚀 Deployment

### Before Deploying:

1. **Set Production Mode**
   ```python
   app.run(debug=False)  # Turn off debug mode
   ```

2. **Update Secret Key**
   ```python
   app.config['SECRET_KEY'] = 'generate-strong-random-key'
   ```

3. **Use Production Server**
   ```bash
   pip install gunicorn
   gunicorn app:app
   ```

4. **Enable HTTPS**
   - Use a reverse proxy (Nginx)
   - Get SSL certificate (Let's Encrypt)

### Hosting Options:
- Heroku
- Railway
- PythonAnywhere
- AWS/Google Cloud
- DigitalOcean

## 📞 Support

For issues or questions:
1. Check browser console for errors (F12)
2. Check Flask terminal output
3. Verify all files are in correct locations
4. Ensure Python 3.8+ is installed

## 📄 License

This project is provided for educational purposes.

## ✨ Features Checklist

- [x] Premium agency-level design
- [x] Secure authentication system
- [x] Login/Signup pages
- [x] Session management
- [x] Protected routes
- [x] Responsive design (Mobile, Tablet, Desktop)
- [x] Smooth animations
- [x] Glassmorphism UI
- [x] Portfolio showcase
- [x] Services with pricing
- [x] Contact page with forms
- [x] WhatsApp integration
- [x] YouTube video integration
- [x] Tools/Tech stack section
- [x] Floating action button
- [x] Navigation bar
- [x] Footer with social links
- [x] FAQ section
- [x] Scroll animations
- [x] Form validation
- [x] Error handling

---

**Made with ❤️ for Premium Portfolio Websites**
