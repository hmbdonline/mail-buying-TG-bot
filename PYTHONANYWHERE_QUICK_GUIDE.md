# PythonAnywhere Quick Deployment Guide

## 🚀 Quick Setup (5 Minutes)

### 1. Create Account
- Go to [pythonanywhere.com](https://www.pythonanywhere.com)
- Sign up for free account

### 2. Upload Files
Open Bash console and run:
```bash
# Option A: From Git
git clone <your-repo-url>
cd telegram-mail-bot

# Option B: Upload manually via Files tab
```

### 3. Install Dependencies
```bash
cd ~/telegram-mail-bot
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Configure Bot
```bash
nano .env
```
Add:
```
TELEGRAM_BOT_TOKEN=your_token_here
DATABASE_PATH=/home/YOURUSERNAME/telegram-mail-bot/data/bot.db
CONFIG_PATH=/home/YOURUSERNAME/telegram-mail-bot/config
```
Replace `YOURUSERNAME` with your actual username!

### 5. Create Directories
```bash
mkdir -p data config
```

### 6. Create Startup Script
```bash
nano start_bot.sh
```
Paste:
```bash
#!/bin/bash
cd /home/YOURUSERNAME/telegram-mail-bot
source venv/bin/activate
if ! pgrep -f "python main.py" > /dev/null; then
    nohup python main.py > bot_output.log 2>&1 &
fi
```
Make executable:
```bash
chmod +x start_bot.sh
```

### 7. Start Bot
```bash
./start_bot.sh
```

### 8. Verify It's Running
```bash
ps aux | grep "python main.py"
tail -f bot.log
```

## 📱 Test Your Bot
Open Telegram and message your bot with `/start`

## 🔄 Daily Management

**Start Bot:**
```bash
cd ~/telegram-mail-bot && ./start_bot.sh
```

**Stop Bot:**
```bash
pkill -f "python main.py"
```

**View Logs:**
```bash
cd ~/telegram-mail-bot && tail -f bot.log
```

**Restart Bot:**
```bash
pkill -f "python main.py" && cd ~/telegram-mail-bot && ./start_bot.sh
```

## ⚠️ Important Notes

**Free Tier Limitations:**
- Bot may stop after 24 hours
- Need to restart manually or use scheduled tasks
- Limited CPU time (100 seconds/day)

**For 24/7 Operation:**
- Upgrade to paid account ($5/month)
- Or use alternative hosting (Railway, Render, Fly.io)

## 🔧 Troubleshooting

**Bot not responding?**
```bash
cd ~/telegram-mail-bot
cat bot.log  # Check for errors
./start_bot.sh  # Restart
```

**Module not found?**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

**Check if running:**
```bash
ps aux | grep "python main.py"
```

## 📋 Scheduled Task (Auto-Restart)

1. Go to PythonAnywhere "Tasks" tab
2. Add scheduled task:
   - Command: `/home/YOURUSERNAME/telegram-mail-bot/start_bot.sh`
   - Time: 00:00 UTC
   - Frequency: Daily

This restarts your bot daily automatically!

## ✅ Done!

Your bot is now running on PythonAnywhere! 🎉

For detailed instructions, see `PYTHONANYWHERE_DEPLOYMENT.md`
