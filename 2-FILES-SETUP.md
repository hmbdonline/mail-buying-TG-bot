# 2-Files Setup - Quick Reference

## 📦 What You Need

Just 2 files:

1. ✅ **bot.py** (already created)
2. ✅ **requirements.txt** (rename `requirements-simple.txt`)

## ⚡ 3-Step Setup

### 1. Get Files
```
bot.py
requirements.txt (rename requirements-simple.txt to requirements.txt)
```

### 2. Set Environment Variable
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

### 3. Upload & Run
Upload both files to your hosting platform and run!

## 🎯 Start Command

```bash
python bot.py
```

## 🌐 Popular Hosting Platforms

### Replit (Easiest)
1. Upload 2 files
2. Secrets → Add `TELEGRAM_BOT_TOKEN`
3. Click Run ▶️

### Railway.app (Best Free)
1. New Project
2. Upload files
3. Variables → Add token
4. Auto-deploys

### Render.com
1. New Web Service
2. Upload files
3. Environment → Add token
4. Deploy

### Heroku
1. Create app
2. Config Vars → Add token
3. Upload files
4. Enable worker

## ✅ Features

- ✅ User registration
- ✅ Admin panel (@s00s22)
- ✅ Transactions
- ✅ Statistics
- ✅ SQLite database
- ✅ Button interface

## 🔧 Customize

Change main admin in `bot.py`:
```python
MAIN_ADMIN_USERNAME = "@your_username"
```

## 🆘 Common Issues

**"Token not set"**
→ Add `TELEGRAM_BOT_TOKEN` environment variable

**"Module not found"**
→ Check `requirements.txt` has: `python-telegram-bot==20.7`

**Bot not responding**
→ Check logs, verify token, ensure bot not running elsewhere

## 📱 Test Locally

```bash
export TELEGRAM_BOT_TOKEN=your_token
pip install -r requirements.txt
python bot.py
```

## 🎉 Done!

Your bot is ready to deploy with just 2 files!

For detailed guide, see `SIMPLE_HOSTING_GUIDE.md`
