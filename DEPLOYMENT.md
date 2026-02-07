# Car Price Estimator - Deployment Guide

## Deployment Options

### Option 1: Deploy Frontend to Vercel (Recommended)

**Frontend (Static HTML)**
1. Go to [vercel.com](https://vercel.com) and sign up with GitHub
2. Click "Add New..." → "Project"
3. Select your GitHub repository
4. Set **Root Directory** to `frontend`
5. Click "Deploy"

Your frontend will be live! Frontend URL: `https://your-project.vercel.app`

### Option 2: Deploy Backend to Render

**Backend (Python Flask)**
1. Go to [render.com](https://render.com) and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Set the following:
   - **Name**: car-price-estimator-api
   - **Environment**: Python
   - **Root Directory**: backend
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Click "Create Web Service"

Your backend will be live! Backend URL: `https://your-api.onrender.com`

### Step 3: Update Frontend API URL

Once your backend is deployed, update the API URL in `frontend/index.html`:

Find this line around line 239:
```javascript
const API_URL = "http://localhost:5000/api";
```

Replace with:
```javascript
const API_URL = "https://your-api.onrender.com/api";
```

Then push the changes to GitHub, and Vercel will auto-redeploy.

### Alternative: Deploy Both to Railway.app

1. Go to [railway.app](https://railway.app)
2. Connect GitHub repository
3. Add plugins for Python and PostgreSQL
4. Set environment variables
5. Deploy both frontend and backend

### Alternative: Docker Deployment

Create `Dockerfile` in root:
```dockerfile
FROM python:3.14
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "backend/app.py"]
```

Deploy to:
- **Heroku** (with `Procfile`)
- **DigitalOcean App Platform**
- **AWS ECS**
- **Google Cloud Run**

## Setup for Production

### 1. Update Backend for Production

Update `backend/app.py`:
```python
app.run(debug=False)  # Set to False in production
```

### 2. Add Environment Variables

Create `.env` file (keep locally, don't commit):
```
FLASK_ENV=production
API_URL=your_production_backend_url
```

### 3. Update CORS for Production

In `backend/app.py`, update CORS:
```python
CORS(app, resources={
    r"/api/*": {
        "origins": ["https://your-frontend.vercel.app"],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})
```

## Recommended Deployment Stack

**Fastest Setup:**
- Frontend: Vercel (Free, auto-deploys from GitHub)
- Backend: Render (Free tier available)

**Most Reliable:**
- Frontend: Vercel
- Backend: Railway or DigitalOcean
- Database: Optional PostgreSQL

## Testing Live Deployment

After deployment:
1. Visit your frontend URL
2. Enter car details
3. Click "Estimate Price"
4. Should see results from live backend

## Troubleshooting

**CORS Error?**
- Check backend CORS configuration
- Verify frontend URL matches CORS origins
- Backend and frontend can be on different domains

**API 404 Error?**
- Verify backend deployment completed
- Check API endpoint structure
- Ensure API URL is correct in frontend

**Slow Response?**
- Check backend logs on hosting platform
- Render free tier may take 30s to wake up
- Consider upgrading to paid tier

## GitHub Setup for Auto-Deployment

1. Push code to GitHub
2. Add deployment platform (Vercel/Render)
3. Configure webhooks
4. Each push auto-deploys!

---

For questions, check platform documentation:
- Vercel: https://vercel.com/docs
- Render: https://render.com/docs
- Railway: https://railway.app/docs
