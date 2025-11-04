# Simple Hosting Guide (2 Files Only)

This guide is for hosting platforms that only accept `bot.py` and `requirements.txt`.

## 📁 Files You Need

You only need these 2 files:

1. **bot.py** - The main bot file (already created)
2. **requirements.txt** - Use `requirements-simple.txt` and rename it

## 🚀 Quick Setup

### Step 1: Prepare Your Files

1. Take the `bot.py` file from your project
2. Rename `requirements-simple.txt` to `requirements.txt`
3. You now have 2 files ready!

### Step 2: Set Environment Variable

Your hosting platform needs this environment variable:

```
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

**How to set it depends on your hosting platform:**

- **Heroku**: Settings → Config Vars
- **Railway**: Variables tab
- **Render**: Environment → Add Variable
- **Replit**: Secrets (lock icon)
- **PythonAnywhere**: .env file or environment settings

### Step 3: Upload Files

Upload both files to your hosting platform:
- `bot.py`
- `requirements.txt`

### Step 4: Start Command

Most platforms auto-detect, but if asked for start command:

```bash
python bot.py
```

Or:

```bash
python3 bot.py
```

## 📋 Platform-Specific Instructions

### Replit

1. Create new Python Repl
2. Upload `bot.py` and `requirements.txt`
3. Click Secrets (🔒 icon)
4. Add: `TELEGRAM_BOT_TOKEN` = `your_token`
5. Click Run

### Railway.app

1. New Project → Deploy from GitHub or Upload
2. Upload `bot.py` and `requirements.txt`
3. Variables → Add `TELEGRAM_BOT_TOKEN`
4. Deploy

### Render.com

1. New → Web Service
2. Connect repository or upload files
3. Environment → Add `TELEGRAM_BOT_TOKEN`
4. Start Command: `python bot.py`
5. Deploy

### Heroku

1. Create new app
2. Settings → Config Vars → Add `TELEGRAM_BOT_TOKEN`
3. Deploy → Upload files
4. Resources → Enable worker dyno

### Glitch

1. New Project → Import from GitHub
2. Upload `bot.py` and `requirements.txt`
3. `.env` file → Add `TELEGRAM_BOT_TOKEN=your_token`
4. Start

## ✅ Features Included

The simplified `bot.py` includes:

✅ User registration
✅ Admin system (main admin: @s00s22)
✅ Basic commands (/start, /help, /admin)
✅ Transaction tracking
✅ User statistics
✅ Admin panel
✅ SQLite database
✅ Button interface

## 🔧 Customization

### Change Main Admin

Edit this line in `bot.py`:

```python
MAIN_ADMIN_USERNAME = "@s00s22"
```

Change to your username:

```python
MAIN_ADMIN_USERNAME = "@your_username"
```

### Add More Features

The `bot.py` file is simplified but functional. You can:

1. Add more buttons in `start_command()`
2. Add more admin features in `button_callback()`
3. Implement full transaction system
4. Add payment integration

## 🆘 Troubleshooting

### "TELEGRAM_BOT_TOKEN not set"

Make sure you set the environment variable in your hosting platform.

### "Module not found"

Make sure `requirements.txt` contains:
```
python-telegram-bot==20.7
```

### Bot doesn't respond

1. Check if bot is running (check logs)
2. Verify bot token is correct
3. Make sure bot is not running elsewhere (conflict)

### Database errors

The bot creates `bot.db` automatically. Make sure your hosting platform allows file creation.

## 📊 Testing Locally

Before uploading, test locally:

```bash
# Set environment variable
export TELEGRAM_BOT_TOKEN=your_token_here

# Install requirements
pip install -r requirements.txt

# Run bot
python bot.py
```

On Windows:
```cmd
set TELEGRAM_BOT_TOKEN=your_token_here
pip install -r requirements.txt
python bot.py
```

## 🎯 What's Different from Full Version?

**Simplified version:**
- ✅ Single file (easy to upload)
- ✅ Core features only
- ✅ SQLite database (no external DB needed)
- ✅ Basic admin system
- ✅ Works on any Python hosting

**Full version:**
- Multiple files (better organization)
- More features (button manager, message manager, etc.)
- JSON configuration files
- Advanced permission system
- More robust error handling

## 🔄 Upgrading to Full Version

If you need more features later:

1. Use the full project structure
2. Deploy to a platform that supports multiple files
3. Use the complete `requirements.txt`

## 📝 Summary

**You need:**
1. `bot.py` ✅
2. `requirements.txt` (rename from `requirements-simple.txt`) ✅
3. Set `TELEGRAM_BOT_TOKEN` environment variable ✅

**That's it!** Your bot will run on any Python hosting platform! 🚀

## 🌟 Recommended Free Hosting

Best platforms for this setup:

1. **Railway.app** - Easy, free tier, always-on
2. **Render.com** - Free tier, good for bots
3. **Replit** - Super easy, free tier
4. **Fly.io** - Free tier, reliable
5. **Glitch** - Free, simple interface

All support the 2-file setup! 🎉
