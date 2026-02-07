# 📚 COMPLETE STEP-BY-STEP DEPLOYMENT GUIDE

## Table of Contents
1. [Part 1: Create GitHub Account & Repository](#part-1-create-github-account--repository)
2. [Part 2: Push Code to GitHub](#part-2-push-code-to-github)
3. [Part 3: Deploy Frontend to Vercel](#part-3-deploy-frontend-to-vercel)
4. [Part 4: Deploy Backend to Render](#part-4-deploy-backend-to-render)
5. [Part 5: Connect Frontend to Backend](#part-5-connect-frontend-to-backend)
6. [Part 6: Test Your Live App](#part-6-test-your-live-app)

---

# PART 1: Create GitHub Account & Repository

## Step 1.1: Create GitHub Account (if you don't have one)

1. Open your web browser (Chrome, Edge, Firefox)
2. Go to **https://github.com**
3. Click **"Sign Up"** button (top right)
4. Enter an email address (e.g., your@email.com)
5. Create a password (remember this!)
6. Enter a username (e.g., `mananmatlani` or `your-name-here`)
7. Choose "No" for emails
8. Click **"Create account"**
9. You'll see "Verify your email" - check your email inbox
10. Click the link GitHub sent you
11. ✅ **You now have a GitHub account!**

## Step 1.2: Create a New Repository

1. Log in to GitHub at https://github.com
2. Click the **"+"** icon (top right) → **"New repository"**
3. Fill in the form:
   - **Repository name**: `car-price-estimator` (this is the project name)
   - **Description**: `A web app to estimate fair car selling prices` (optional but nice)
   - **Public** or **Private**: Choose **Public** (so it's free)
   - Leave everything else as default
4. Click **"Create repository"**

✅ **You now have an empty GitHub repository!**

You'll see a screen with instructions. Keep this page open - you'll need the URL shown there.

---

# PART 2: Push Code to GitHub

## Step 2.1: Open Terminal/PowerShell

Windows:
1. Press **Windows Key + R**
2. Type `powershell` and press Enter
3. A black/blue window opens - this is your terminal

## Step 2.2: Navigate to Your Project Folder

In the PowerShell window, type:
```powershell
cd "C:\Users\Manan Matlani\Documents\my chatbot"
```

Then press **Enter**

You should see something like:
```
PS C:\Users\Manan Matlani\Documents\my chatbot>
```

## Step 2.3: Initialize Git in Your Project

Type this command:
```powershell
git init
```

Press **Enter**

You should see:
```
Initialized empty Git repository in C:\Users\Manan Matlani\Documents\my chatbot\.git\
```

✅ **Git is now tracking your project!**

## Step 2.4: Configure Git (First Time Only)

Type these commands one by one:

```powershell
git config --global user.name "Your Name"
```
Replace `"Your Name"` with your actual name (keep the quotes)

Then:
```powershell
git config --global user.email "your@email.com"
```
Replace `your@email.com` with the email you used for GitHub

## Step 2.5: Add All Files to Git

Type:
```powershell
git add .
```

This command tells Git: "Track all files in this folder"

The `.` means "everything"

## Step 2.6: Create Your First Commit

Type:
```powershell
git commit -m "Initial commit - Car price estimator app"
```

You should see something like:
```
[main (root-commit) abc1234] Initial commit - Car price estimator app
 8 files changed, 500 insertions(+)
 create mode 100644 README.md
 create mode 100644 backend/app.py
 ...
```

✅ **Your files are now saved as a "commit"**

## Step 2.7: Rename Branch to Main

Type:
```powershell
git branch -M main
```

This ensures your default branch is called `main` (GitHub's standard)

## Step 2.8: Add GitHub Repository URL

Go back to your GitHub repository page you created in Part 1.

You should see a URL like: `https://github.com/YOUR-USERNAME/car-price-estimator.git`

Copy that URL, then in PowerShell type:
```powershell
git remote add origin https://github.com/YOUR-USERNAME/car-price-estimator.git
```

Replace the URL with the one you copied

## Step 2.9: Push Code to GitHub

Type:
```powershell
git push -u origin main
```

First time, it might ask:
- "Credentials for 'https://github.com'" 
- Enter your GitHub **username**
- Enter your GitHub **password** (or Personal Access Token)

After a few seconds, you should see:
```
Enumerating objects: 8, done.
...
To https://github.com/YOUR-USERNAME/car-price-estimator.git
 * [new branch]      main -> main
Branch 'main' is set up to track remote branch 'main' from 'origin'.
```

✅ **Your code is now on GitHub!**

## Step 2.10: Verify on GitHub

1. Go to https://github.com/YOUR-USERNAME/car-price-estimator
2. You should see your files listed:
   - `backend/` folder
   - `frontend/` folder
   - `README.md`
   - etc.

🎉 **Code pushed successfully!**

---

# PART 3: Deploy Frontend to Vercel

## Step 3.1: Create Vercel Account

1. Open browser and go to **https://vercel.com**
2. Click **"Sign Up"** (top right)
3. Click **"Continue with GitHub"**
4. GitHub will ask "Authorize Vercel"
5. Click **"Authorize Vercel"**
6. You'll be logged into Vercel ✅

## Step 3.2: Create New Project

1. On Vercel dashboard, click **"Add New..."** (top left)
2. Click **"Project"**
3. You'll see a list of repositories from GitHub
4. Find **`car-price-estimator`** and click **"Import"**

## Step 3.3: Configure Project Settings

Now you'll see a form. Important step here:

**Root Directory:**
- By default it might be empty or set to root
- Click the dropdown and look for an option to set Root Directory
- Or in the form, find where it says "Root Directory"
- Set it to: `frontend`

This tells Vercel: "The website files are in the frontend folder"

**Framework Preset:**
- Leave as "Other" (since we're using plain HTML/React)

**Leave everything else as default**

## Step 3.4: Deploy

Click **"Deploy"** button

You'll see a progress bar. Vercel is uploading and building your frontend.

Wait about 1-2 minutes...

You'll see:
```
✅ Production
https://car-price-estimator.vercel.app
```

**Your frontend URL is: `https://car-price-estimator.vercel.app`** (yours will have a different name)

✅ **Frontend deployed!**

---

# PART 4: Deploy Backend to Render

## Step 4.1: Create Render Account

1. Open browser and go to **https://render.com**
2. Click **"Sign Up"** (top right)
3. Click **"Continue with GitHub"**
4. GitHub will ask "Authorize Render"
5. Click **"Authorize Render"**
6. You'll be logged into Render ✅

## Step 4.2: Create New Web Service

1. On Render dashboard, click **"New +"** (top left)
2. Click **"Web Service"**
3. You'll see a list of repositories
4. Find **`car-price-estimator`** and click **"Connect"**

## Step 4.3: Configure Backend Settings

You'll see a form. Fill in these **exact** settings:

**Name:**
```
car-price-estimator-api
```

**Runtime:**
```
Python 3
```

**Root Directory:**
```
backend
```

**Build Command:**
```
pip install -r requirements.txt
```
(This installs all Python packages needed)

**Start Command:**
```
gunicorn app:app --bind 0.0.0.0:$PORT
```
(This starts the server)

**Branch:**
```
main
```

**Everything else:** Leave as default

## Step 4.4: Deploy

Scroll down and click **"Create Web Service"**

Render will start deploying. You'll see logs showing:
```
Building...
Installing dependencies...
...
✓ Deployment successful
```

This takes about 3-5 minutes. You can watch the logs scroll by.

Once complete, you'll see:
```
https://car-price-estimator-api.onrender.com
```

**Your backend URL is: `https://car-price-estimator-api.onrender.com`** (yours will have a different name)

✅ **Backend deployed!**

---

# PART 5: Connect Frontend to Backend

Now the frontend and backend need to talk to each other.

## Step 5.1: Update Frontend with Backend URL

1. Open VS Code (or your editor)
2. Open the file: `frontend/index.html`
3. Press **Ctrl+F** to open Find
4. Search for: `const API_URL = `
5. You should find this line around line 239:
   ```javascript
   const API_URL = "http://localhost:5000/api";
   ```

## Step 5.2: Replace with Production URL

Replace that entire line with:
```javascript
const API_URL = "https://car-price-estimator-api.onrender.com/api";
```

**Important:** Use the backend URL you got from Render in Part 4. If your URL is different, replace mine with yours.

## Step 5.3: Save the File

Press **Ctrl+S** to save

## Step 5.4: Push Changes to GitHub

In PowerShell (in your project folder):

```powershell
git add frontend/index.html
```

```powershell
git commit -m "Update API URL for production backend"
```

```powershell
git push
```

You should see:
```
Updating abc1234..def5678
1 file changed, 1 insertion(+), 1 deletion(-)
```

## Step 5.5: Vercel Auto-Redeploys

Go to your Vercel dashboard at https://vercel.com

Click on your project. You should see it's automatically redeploying because you pushed new code!

Wait 1-2 minutes for it to finish.

✅ **Frontend and Backend are now connected!**

---

# PART 6: Test Your Live App

## Step 6.1: Open Your Frontend

1. Open your browser
2. Go to: `https://car-price-estimator.vercel.app` (replace with your URL)
3. You should see the Car Price Estimator form

## Step 6.2: Test the App

1. Fill in the form:
   - Brand: Select "Toyota"
   - Model: Type "Camry"
   - Year: "2018"
   - Mileage: "75000"
   - Condition: "Good"
2. Click **"🔍 Estimate Price"**
3. Wait a moment (first request takes ~30 seconds on free tier)
4. You should see the results page with an estimated price

✅ **Your app is working live on the internet!**

If you get an error:
- Check the backend URL in your code matches your Render URL
- Wait 30 seconds (Render free tier takes time to wake up)
- Refresh the page

---

# TROUBLESHOOTING

## "Can't connect to API" Error

**Solution:**
1. Check your API URL in `frontend/index.html` is correct
2. Go to Render dashboard, copy the exact URL from your web service
3. Make sure it ends with `/api` in the frontend code
4. Push changes: `git push`
5. Refresh Vercel page

## "502 Bad Gateway" Error from Backend

**Solution:**
1. Go to Render dashboard → your web service
2. Check the "Logs" tab for errors
3. If you see errors, check that all files are correct
4. Redeploy: Click "Manual Deploy" on Render

## "frontend/index.html file not found"

**Solution:**
1. Make sure Vercel Root Directory is set to `frontend`
2. In Vercel → Settings → check Root Directory is `frontend`

## Changes not showing up

**Solution:**
1. In PowerShell, make sure you `git push`
2. Wait 1-2 minutes for auto-redeploy
3. Refresh your browser (Ctrl+F5 for hard refresh)

---

# NEXT TIME YOU MAKE CHANGES

Once everything is set up, to make updates:

1. Edit your code in VS Code
2. In PowerShell:
   ```powershell
   git add .
   git commit -m "Description of changes"
   git push
   ```
3. Vercel/Render auto-redeploy
4. Your live site updates automatically! 🎉

---

# YOUR LIVE URLS

**Save these somewhere safe:**

- **Frontend:** https://YOUR-USERNAME.vercel.app/
- **Backend API:** https://your-app-name.onrender.com/api
- **GitHub:** https://github.com/YOUR-USERNAME/car-price-estimator

**Share the frontend URL with anyone to use your app!** 🚀

---

# UPGRADE TO PAID (Optional)

**Free tier works great, but:**
- Render free tier sleeps after 15 minutes
- First request takes ~30 seconds to wake up

**To fix:**
- Upgrade Render to $7/month
- Provides 24/7 uptime and instant responses

**Don't worry if it's slow on first request - it's just waking up!**

---

# CONGRATULATIONS! 🎉

Your app is now:
✅ Deployed on Vercel (frontend)
✅ Deployed on Render (backend)
✅ Live on the internet
✅ Accessible from anywhere
✅ Free to use

**You've successfully built and published a full-stack web application!**

Share it with friends: https://YOUR-FRONTEND-URL.vercel.app
