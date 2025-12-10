# Deployment Guide

## ✅ Option 1: Streamlit Community Cloud (Recommended - FREE)

### Steps:

1. **Push your code to GitHub** (if not already done)
   ```bash
   git add .
   git commit -m "Add deployment files"
   git push origin main
   ```

2. **Go to [share.streamlit.io](https://share.streamlit.io)**

3. **Sign in with GitHub**

4. **Click "New app"**

5. **Fill in the details:**
   - Repository: Your GitHub repo
   - Branch: `main`
   - Main file path: `ui.py`

6. **Add environment variable:**
   - Click "Advanced settings"
   - Add secret:
     ```
     GROQ_API_KEY = "your_groq_api_key_here"
     ```

7. **Click "Deploy"** - Your app will be live in 2-3 minutes!

---

## Option 2: Railway (Also supports Streamlit)

1. Go to [railway.app](https://railway.app)
2. Connect your GitHub repo
3. Add environment variable: `GROQ_API_KEY`
4. Railway will auto-detect Streamlit and deploy

---

## Option 3: Render

1. Go to [render.com](https://render.com)
2. Create a new "Web Service"
3. Connect your GitHub repo
4. Set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `streamlit run ui.py --server.port $PORT`
5. Add environment variable: `GROQ_API_KEY`

---

## ⚠️ Why NOT Vercel?

Vercel is designed for **serverless functions** and **static sites** (Next.js, React, etc.).

Streamlit requires a **persistent server** to maintain WebSocket connections, which Vercel doesn't support.

**If you must use Vercel**, you'd need to:
- Convert the app to FastAPI/Flask backend
- Build a React/Next.js frontend
- Connect them via API calls

This would be a complete rewrite.

---

## 📝 Local Testing

```bash
pip install -r requirements.txt
streamlit run ui.py
```

Visit: http://localhost:8501
