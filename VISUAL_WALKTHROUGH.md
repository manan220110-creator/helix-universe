# 📖 VISUAL WALKTHROUGH & SCREENSHOTS GUIDE

This guide describes what you should see at each step. Match your screen to these descriptions.

---

## STEP 1: GitHub Setup

### 1.1 - Creating Repository

**What you should see:**
```
GitHub Dashboard
├─ "+" menu (top right)
├─ "New repository" option
└─ Repository creation form:
    ├─ Repository name: car-price-estimator
    ├─ Description: (optional)
    ├─ Public/Private: ⦿ Public
    └─ [Create repository] button
```

**After clicking Create:**
You'll see a page that says:
```
Quick setup — if you've done this kind of thing before
Set up in Desktop   HTTPS   SSH   GitHub CLI

Get started by creating a new file or uploading an existing file.
We recommend every repository include a README, LICENSE, and gitignore.
```

**Copy the HTTPS URL shown** (looks like: `https://github.com/YOUR-USERNAME/car-price-estimator.git`)

---

## STEP 2: PowerShell Commands

### 2.1 - Open PowerShell

**What you should see when PowerShell opens:**
```
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\Manan Matlani>
```

The `>` at the end means it's ready for commands.

### 2.2 - Navigate to Project

**Type:**
```powershell
cd "C:\Users\Manan Matlani\Documents\my chatbot"
```

**What you should see after pressing Enter:**
```
PS C:\Users\Manan Matlani\Documents\my chatbot>
```

Notice the path changed to your project folder.

### 2.3 - Initialize Git

**Type:**
```powershell
git init
```

**What you should see:**
```
Initialized empty Git repository in C:\Users\Manan Matlani\Documents\my chatbot\.git\
```

✅ Git is now tracking your folder!

### 2.4 - Configure Git

**Type (replace with your info):**
```powershell
git config --global user.name "Manan Matlani"
```

**Type:**
```powershell
git config --global user.email "manan@example.com"
```

These should run silently (no output = success ✅)

### 2.5 - Add All Files

**Type:**
```powershell
git add .
```

**What you should see:**
```
PS C:\Users\Manan Matlani\Documents\my chatbot>
```

(No output = success ✅)

### 2.6 - Create Commit

**Type:**
```powershell
git commit -m "Initial commit - Car price estimator app"
```

**What you should see:**
```
[main (root-commit) a1b2c3d] Initial commit - Car price estimator app
 8 files changed, 2500 insertions(+)
 create mode 100644 README.md
 create mode 100644 backend/app.py
 create mode 100644 backend/requirements.txt
 create mode 100644 frontend/index.html
 ...
```

The numbers may be different, but you should see files listed. ✅

### 2.7 - Set Main Branch

**Type:**
```powershell
git branch -M main
```

(No output = success ✅)

### 2.8 - Add Remote (GitHub)

**Type (use the URL you copied earlier):**
```powershell
git remote add origin https://github.com/YOUR-USERNAME/car-price-estimator.git
```

(No output = success ✅)

### 2.9 - Push to GitHub

**Type:**
```powershell
git push -u origin main
```

**First time, you might see:**
```
Credentials for 'https://github.com/YOUR-USERNAME/car-price-estimator.git'
Username for 'https://github.com': 
```

**Enter your GitHub username** (not email) and press Enter

Then it asks:
```
Password for 'https://YOUR-USERNAME@github.com':
```

**Enter your GitHub password** and press Enter

(Password won't show as you type - that's normal!)

**What you should see after ~10 seconds:**
```
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 8 threads.
Compressing objects: 100% (6/6), done.
Writing objects: 100% (8/8), 1.23 KiB | 1.23 MiB/s, done.

Total 8 (delta 0), reused 0 (delta 0), pack-reused 0

To https://github.com/YOUR-USERNAME/car-price-estimator.git
 * [new branch]      main -> main
Branch 'main' is set up to track remote branch 'main' from 'origin'.

PS C:\Users\Manan Matlani\Documents\my chatbot>
```

✅ Your code is now on GitHub!

---

## STEP 3: Deploy to Vercel (Frontend)

### 3.1 - Go to Vercel.com

**What you should see:**
```
Vercel Dashboard
├─ [Sign Up] or [Log in] button (top right)
└─ Vercel logo (top left)
```

### 3.2 - Sign Up with GitHub

**Click [Sign Up]**

**You'll see:**
```
Vercel Signup
├─ "Continue with GitHub" button
├─ "Continue with GitLab" button
└─ "Continue with Bitbucket" button
```

**Click "Continue with GitHub"**

### 3.3 - Authorize Vercel

**GitHub asks:**
```
GitHub Authorization
├─ "Authorize Vercel" button
└─ "Request: Your email addresses (read-only)"
```

**Click "Authorize Vercel"**

### 3.4 - Back on Vercel

**You should see:**
```
Vercel Dashboard
├─ Your profile icon (top right)
├─ "Add New..." button (left side)
└─ No projects yet (empty)
```

### 3.5 - Import Project

**Click "Add New..." → "Project"**

**You'll see:**
```
Import Project
├─ "Search your repositories"
├─ List of your GitHub repos:
│  ├─ car-price-estimator ← Click this!
│  └─ (other repos)
└─ [Import] button (when you hover)
```

**Find `car-price-estimator` and click it**

### 3.6 - Configure Root Directory

**After clicking Import, you'll see:**
```
Configure Project
├─ Project Name: car-price-estimator
├─ Root Directory: [dropdown] ← IMPORTANT!
│  ├─ .
│  ├─ frontend ← Select this!
│  ├─ backend
│  └─ ...
├─ Framework: Other (default is OK)
└─ [Deploy] button (blue)
```

**Click Root Directory dropdown and select `frontend`**

### 3.7 - Deploy

**Click blue [Deploy] button**

**You'll see:**
```
Deploying...
├─ ✓ Installed dependencies
├─ ✓ Build completed
├─ ✓ Generated files
├─ ✓ Creating deployment
└─ ✓ Deployment complete!

🎉 Your site is live at:
   https://car-price-estimator-abc1234.vercel.app
```

(Your URL will be different)

✅ **Frontend is deployed! Copy this URL.**

---

## STEP 4: Deploy to Render (Backend)

### 4.1 - Go to Render.com

**What you should see:**
```
Render Dashboard
├─ [Sign Up] button (top right)
└─ Render logo (top left)
```

### 4.2 - Sign Up with GitHub

**Click [Sign Up]**

**Click "Continue with GitHub"**

**GitHub asks for authorization - click "Authorize Render"**

### 4.3 - Create Web Service

**You should see:**
```
Render Dashboard
├─ "New +" button (left side)
└─ (empty, no services yet)
```

**Click "New +" → "Web Service"**

### 4.4 - Connect Repository

**You'll see:**
```
Connect a Repository
├─ "Search repositories"
├─ car-price-estimator ← Select this!
└─ [Connect] button
```

### 4.5 - Configure Settings

**After connecting, you'll see a form:**

```
Web Service Configuration
├─ Name: [field] ← Enter: car-price-estimator-api
├─ Environment: [dropdown] ← Select: Python 3
├─ Build Command: [field] ← Enter: pip install -r requirements.txt
├─ Start Command: [field] ← Enter: gunicorn app:app --bind 0.0.0.0:$PORT
├─ Root Directory: [field] ← Enter: backend
├─ Branch: main ✓
└─ [Create Web Service] button
```

**Fill in each field exactly as shown**

### 4.6 - Deploy

**Click [Create Web Service]**

**You'll see logs scrolling:**
```
Building your service...
├─ Building from main branch
├─ Installing dependencies...
│  ├─ pip install Flask...
│  ├─ pip install flask-cors...
│  └─ ...
├─ Build successful ✓
├─ Starting service...
└─ Live on: https://car-price-estimator-api.onrender.com
```

(Your URL will be different, but will look similar)

✅ **Backend is deployed! Copy this URL.**

---

## STEP 5: Connect Frontend to Backend

### 5.1 - Open VS Code

Open the file: `frontend/index.html`

### 5.2 - Find API URL

**Press Ctrl+F (Find)**

**Search for:** `const API_URL = `

**You should see highlighted:**
```javascript
const API_URL = "http://localhost:5000/api";
```

### 5.3 - Replace URL

Replace that line with:
```javascript
const API_URL = "https://your-api-name.onrender.com/api";
```

Use your actual Render URL! (not "your-api-name")

### 5.4 - Save File

**Press Ctrl+S**

### 5.5 - Push Changes

**In PowerShell (in your project folder):**

```powershell
git add frontend/index.html
```

```powershell
git commit -m "Update API URL for production"
```

```powershell
git push
```

**What you should see:**
```
Updating abc1234..def5678
1 file changed, 1 insertion(+), 1 deletion(-)
```

### 5.6 - Wait for Vercel

**Go to Vercel dashboard**

**You should see:**
```
Your Project
├─ Production (building...)
└─ (wait 1-2 minutes)

Then you'll see:
✓ Production
├─ https://your-app.vercel.app
└─ Latest deployment successful
```

✅ Everything is connected!

---

## STEP 6: Test Your Live App

### 6.1 - Open Your Frontend

**In browser, go to:** `https://your-app.vercel.app`

**You should see:**
```
🚗 Car Price Estimator
Get a fair estimate of your car's selling price

[Form with fields]
├─ Brand: [dropdown]
├─ Model: [text field]
├─ Year: [number field]
├─ Mileage: [number field]
├─ Condition: [dropdown]
├─ Maintenance: [dropdown]
├─ Checkbox: Has accident history
├─ [🔍 Estimate Price] button
└─ [Reset] button
```

### 6.2 - Fill Form

**Fill in:**
```
Brand: Toyota
Model: Camry
Year: 2018
Mileage: 75000
Condition: Good
Maintenance: Average
Accident: No (unchecked)
```

### 6.3 - Click Estimate

**Click [🔍 Estimate Price]**

**You might see:**
```
Loading... (spinner)
```

**Wait about 30 seconds** (Render free tier waking up)

**You should then see:**
```
✓ Your Car's Value
Toyota Camry • 2018 • 75000 km

Estimated Fair Selling Price
$12,450.00

Min: $11,205.00    Max: $13,695.00

Confidence Level: 85%

Vehicle Details
├─ Condition: Good
├─ Maintenance: Average
└─ Accidents: No

[← Back to Form] button
```

✅ **Everything works! Your app is live!**

---

## Troubleshooting - What Went Wrong?

### Error: "Cannot GET /index.html"

**Problem:** Vercel Root Directory is wrong

**Fix:**
1. Go to Vercel Dashboard → Your Project
2. Click "Settings"
3. Find "Root Directory"
4. Change to `frontend`
5. Redeploy manually if needed

### Error: "Failed to fetch" or "Network Error"

**Problem:** Frontend can't reach backend API

**Fix:**
1. Check your API URL in `frontend/index.html`
2. Make sure it matches your Render URL
3. It should end with `/api`
4. If not correct: Update → `git add` → `git commit` → `git push`

### Error: "502 Bad Gateway"

**Problem:** Backend crashed or not responding

**Fix:**
1. Go to Render Dashboard → Your Service
2. Click "Logs" tab
3. Look for error messages
4. Click "Manual Deploy" to retry

### Changes not showing

**Problem:** Forgot to push or files didn't update

**Fix:**
```powershell
git status  # See what changed
git add .
git commit -m "Changes"
git push
```

Then wait 1-2 minutes for Vercel to redeploy.

---

## Success Checklist

- [ ] GitHub code is pushed (can see it on github.com)
- [ ] Frontend deployed to Vercel (have a vercel.app URL)
- [ ] Backend deployed to Render (have a onrender.com URL)
- [ ] Frontend has correct API URL
- [ ] Can fill form and see results
- [ ] Results show estimated price
- [ ] "Back to Form" button works

✅ **If all checked - YOU'RE DONE! APP IS LIVE!**

---

## Share Your App

Copy your frontend URL:
```
https://your-app.vercel.app
```

Send it to friends! They can use it from anywhere in the world.

🎉 **You've built and deployed a full-stack web application!**
