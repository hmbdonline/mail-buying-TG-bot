# How to Add Your Bot Token

## 📝 Simple Method - Edit bot.py File

### Step 1: Get Your Bot Token

1. Open Telegram and search for **@BotFather**
2. Send `/newbot` and follow instructions
3. Copy your bot token (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### Step 2: Open bot.py

Open the `bot.py` file in any text editor.

### Step 3: Find This Section (at the top)

Look for these lines near the top of the file:

```python
# ============================================
# CONFIGURATION - Add your bot token here
# ============================================
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace with your actual bot token
MAIN_ADMIN_USERNAME = "@s00s22"     # Replace with your Telegram username
# ============================================
```

### Step 4: Replace the Token

Change this line:
```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
```

To (use your actual token):
```python
BOT_TOKEN = "123456789:ABCdefGHIjklMNOpqrsTUVwxyz"
```

### Step 5: Change Admin Username (Optional)

If your Telegram username is NOT @s00s22, change this line:
```python
MAIN_ADMIN_USERNAME = "@s00s22"
```

To your username:
```python
MAIN_ADMIN_USERNAME = "@your_username"
```

### Step 6: Save the File

Save `bot.py` and you're done!

## ✅ Example

**Before:**
```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
MAIN_ADMIN_USERNAME = "@s00s22"
```

**After:**
```python
BOT_TOKEN = "123456789:ABCdefGHIjklMNOpqrsTUVwxyz"
MAIN_ADMIN_USERNAME = "@myusername"
```

## 🚀 Now You Can Upload

Now you have 2 files ready to upload:
1. ✅ `bot.py` (with your token inside)
2. ✅ `requirements.txt` (rename from `requirements-simple.txt`)

Just upload both files to your hosting platform and run!

## 🔒 Security Note

⚠️ **Important:** Never share your `bot.py` file with anyone after adding your token!

Your bot token is like a password. Keep it secret!

## 🆘 Troubleshooting

### "Please set your BOT_TOKEN"

You forgot to replace `YOUR_BOT_TOKEN_HERE` with your actual token.

### "Unauthorized" Error

Your bot token is wrong. Get a new one from @BotFather.

### Bot Not Responding

1. Check token is correct
2. Make sure bot is not running elsewhere
3. Check hosting platform logs

## 📱 Test Locally First

Before uploading, test on your computer:

```bash
# Install requirements
pip install python-telegram-bot==20.7

# Run bot
python bot.py
```

If you see "Bot started!" - it's working! ✅

Message your bot on Telegram with `/start`

## 🎯 Quick Checklist

- [ ] Got bot token from @BotFather
- [ ] Opened bot.py file
- [ ] Replaced `YOUR_BOT_TOKEN_HERE` with actual token
- [ ] Changed `@s00s22` to your username (if needed)
- [ ] Saved the file
- [ ] Ready to upload!

That's it! Your bot is ready to deploy! 🚀
