# Termux Troubleshooting Guide

## Common Issues and Solutions

### Issue 1: "ModuleNotFoundError: No module named 'telegram'"

**Error:**
```
ModuleNotFoundError: No module named 'telegram'
```

**Solution:**
```bash
# Install the telegram library
pip install python-telegram-bot

# If that doesn't work, try:
pip install python-telegram-bot==20.7

# Or install all dependencies:
pip install python-telegram-bot python-dotenv
```

### Issue 2: "No module named '_sqlite3'"

**Error:**
```
ModuleNotFoundError: No module named '_sqlite3'
```

**Solution:**
```bash
# Install Python with sqlite support
pkg uninstall python -y
pkg install python -y

# Then reinstall dependencies
pip install -r requirements.txt
```

### Issue 3: "Permission denied" when running scripts

**Error:**
```
bash: ./start_bot.sh: Permission denied
```

**Solution:**
```bash
# Make scripts executable
chmod +x start_bot.sh
chmod +x stop_bot.sh

# Or run with bash
bash start_bot.sh
```

### Issue 4: "python: command not found"

**Solution:**
```bash
# Install Python
pkg install python -y

# Verify installation
python --version
```

### Issue 5: Requirements.txt Installation Fails

**Error:**
```
ERROR: Could not find a version that satisfies the requirement...
```

**Solution - Install Manually:**
```bash
# Install core dependencies one by one
pip install python-telegram-bot
pip install python-dotenv

# If specific version needed:
pip install python-telegram-bot==20.7
```

### Issue 6: "TELEGRAM_BOT_TOKEN not found"

**Error:**
```
TELEGRAM_BOT_TOKEN not found in environment variables
```

**Solution:**
```bash
# Create .env file
cd ~/telegram-mail-bot
nano .env
```

Add this (replace with your actual token):
```
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
DATABASE_PATH=/data/data/com.termux/files/home/telegram-mail-bot/data/bot.db
CONFIG_PATH=/data/data/com.termux/files/home/telegram-mail-bot/config
LOG_LEVEL=INFO
LOG_FILE=/data/data/com.termux/files/home/telegram-mail-bot/bot.log
```

Save: `Ctrl+X` → `Y` → `Enter`

### Issue 7: Bot Starts But Doesn't Respond

**Check 1: Is bot running?**
```bash
ps aux | grep python
```

**Check 2: View logs**
```bash
cd ~/telegram-mail-bot
cat bot.log
```

**Check 3: Test bot token**
```bash
# In Python
python
>>> import os
>>> from dotenv import load_dotenv
>>> load_dotenv()
>>> print(os.getenv('TELEGRAM_BOT_TOKEN'))
>>> exit()
```

**Check 4: Internet connection**
```bash
ping -c 3 google.com
```

### Issue 8: "Database is locked"

**Solution:**
```bash
# Stop the bot
pkill -f "python main.py"

# Remove lock file
rm ~/telegram-mail-bot/data/bot.db-journal

# Restart bot
cd ~/telegram-mail-bot
./start_bot.sh
```

### Issue 9: Bot Stops After Screen Lock

**Solution:**
```bash
# Acquire wake lock
termux-wake-lock

# Disable battery optimization:
# Settings → Apps → Termux → Battery → Don't optimize
```

### Issue 10: "ImportError: cannot import name 'Update'"

**Solution:**
```bash
# Update python-telegram-bot
pip install --upgrade python-telegram-bot

# Or install specific version
pip install python-telegram-bot==20.7
```

## Step-by-Step Debugging

### Step 1: Check Python Installation
```bash
python --version
# Should show: Python 3.x.x
```

### Step 2: Check Dependencies
```bash
pip list | grep telegram
# Should show: python-telegram-bot
```

### Step 3: Test Import
```bash
python -c "import telegram; print('OK')"
# Should print: OK
```

### Step 4: Check .env File
```bash
cat .env
# Should show your bot token
```

### Step 5: Test Bot Manually
```bash
cd ~/telegram-mail-bot
python main.py
# Watch for errors
```

### Step 6: Check Logs
```bash
cat bot.log
# Look for error messages
```

## Quick Fix Script

Create this script to fix common issues:

```bash
nano fix_bot.sh
```

Add:
```bash
#!/data/data/com.termux/files/usr/bin/bash

echo "=== Fixing Common Issues ==="

# Stop bot
echo "Stopping bot..."
pkill -f "python main.py"

# Update packages
echo "Updating packages..."
pkg update -y

# Reinstall Python
echo "Checking Python..."
python --version

# Reinstall dependencies
echo "Reinstalling dependencies..."
pip install --upgrade pip
pip install python-telegram-bot python-dotenv

# Fix permissions
echo "Fixing permissions..."
cd ~/telegram-mail-bot
chmod +x *.sh

# Remove lock files
echo "Removing lock files..."
rm -f data/bot.db-journal

# Create directories
echo "Creating directories..."
mkdir -p data config

echo "=== Fix Complete ==="
echo "Try starting bot: ./start_bot.sh"
```

Make executable and run:
```bash
chmod +x fix_bot.sh
./fix_bot.sh
```

## Minimal Test Script

Create a minimal test to verify setup:

```bash
nano test_bot.sh
```

Add:
```bash
#!/data/data/com.termux/files/usr/bin/bash

echo "=== Testing Bot Setup ==="

# Test 1: Python
echo -n "Python: "
python --version

# Test 2: Telegram library
echo -n "Telegram library: "
python -c "import telegram; print('OK')" 2>&1

# Test 3: .env file
echo -n ".env file: "
if [ -f .env ]; then
    echo "EXISTS"
else
    echo "MISSING!"
fi

# Test 4: Bot token
echo -n "Bot token: "
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('OK' if os.getenv('TELEGRAM_BOT_TOKEN') else 'MISSING')" 2>&1

# Test 5: Directories
echo -n "Data directory: "
if [ -d data ]; then echo "EXISTS"; else echo "MISSING"; fi

echo -n "Config directory: "
if [ -d config ]; then echo "EXISTS"; else echo "MISSING"; fi

echo "=== Test Complete ==="
```

Run:
```bash
chmod +x test_bot.sh
./test_bot.sh
```

## Still Not Working?

### Get Detailed Error Info

Run bot with full error output:
```bash
cd ~/telegram-mail-bot
python main.py 2>&1 | tee error.log
```

Then share the error from `error.log`

### Check System Info
```bash
echo "=== System Info ==="
uname -a
python --version
pip --version
pkg list-installed | grep python
```

### Reinstall Everything
```bash
# Complete reinstall
cd ~
rm -rf telegram-mail-bot
pkg uninstall python -y
pkg install python git nano -y
pip install --upgrade pip

# Get bot files again
git clone <your-repo-url>
cd telegram-mail-bot

# Install dependencies
pip install python-telegram-bot python-dotenv

# Configure
nano .env
# Add your bot token

# Create directories
mkdir -p data config

# Test
python main.py
```

## Get Help

If still not working, provide:

1. **Error message** - Full error text
2. **Python version** - `python --version`
3. **Installed packages** - `pip list`
4. **Log file** - `cat bot.log`
5. **What you tried** - Steps you followed

## Common Error Messages Explained

### "Conflict: terminated by other getUpdates request"
**Meaning:** Another instance of bot is running
**Fix:** `pkill -f "python main.py"`

### "Unauthorized"
**Meaning:** Invalid bot token
**Fix:** Check token in .env file

### "Network is unreachable"
**Meaning:** No internet connection
**Fix:** Check WiFi/mobile data

### "Read-only file system"
**Meaning:** Storage permission issue
**Fix:** `termux-setup-storage`

### "Cannot allocate memory"
**Meaning:** Phone out of RAM
**Fix:** Close other apps, restart phone

## Prevention Tips

1. **Always use F-Droid Termux** (not Play Store)
2. **Keep Termux updated** - `pkg upgrade`
3. **Use wake lock** - `termux-wake-lock`
4. **Disable battery optimization**
5. **Keep phone charged**
6. **Use stable WiFi**
7. **Check logs regularly** - `tail -f bot.log`

---

**Need more help?** Share the specific error message you're getting!
