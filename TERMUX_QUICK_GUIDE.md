# Termux Quick Setup Guide

## 📱 5-Minute Setup

### 1. Install Termux
- Download from **F-Droid** (NOT Play Store!)
- [https://f-droid.org](https://f-droid.org)

### 2. Setup Termux
```bash
pkg update && pkg upgrade -y
pkg install python git nano -y
pip install --upgrade pip
```

### 3. Get Bot Files
```bash
# Option A: Git
git clone <your-repo-url>
cd telegram-mail-bot

# Option B: From phone storage
termux-setup-storage
cp -r ~/storage/downloads/telegram-mail-bot ~/
cd ~/telegram-mail-bot
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Bot
```bash
nano .env
```
Add:
```
TELEGRAM_BOT_TOKEN=your_token_here
DATABASE_PATH=/data/data/com.termux/files/home/telegram-mail-bot/data/bot.db
CONFIG_PATH=/data/data/com.termux/files/home/telegram-mail-bot/config
```
Save: `Ctrl+X` → `Y` → `Enter`

### 6. Create Directories
```bash
mkdir -p data config
```

### 7. Create Start Script
```bash
nano start_bot.sh
```
Paste:
```bash
#!/data/data/com.termux/files/usr/bin/bash
cd ~/telegram-mail-bot
if ! pgrep -f "python main.py" > /dev/null; then
    nohup python main.py > bot_output.log 2>&1 &
    echo "Bot started!"
else
    echo "Bot already running!"
fi
```
Make executable:
```bash
chmod +x start_bot.sh
```

### 8. Start Bot
```bash
./start_bot.sh
```

### 9. Test
Message your bot on Telegram: `/start`

## 🔄 Daily Commands

**Start:**
```bash
cd ~/telegram-mail-bot && ./start_bot.sh
```

**Stop:**
```bash
pkill -f "python main.py"
```

**Restart:**
```bash
pkill -f "python main.py" && cd ~/telegram-mail-bot && ./start_bot.sh
```

**Logs:**
```bash
cd ~/telegram-mail-bot && tail -f bot.log
```

**Status:**
```bash
ps aux | grep "python main.py"
```

## 🔋 Keep Running 24/7

### Disable Battery Optimization
1. Settings → Apps → Termux
2. Battery → Don't optimize

### Use Wake Lock
```bash
termux-wake-lock
```

### Auto-Start on Boot
1. Install **Termux:Boot** from F-Droid
2. Create boot script:
```bash
mkdir -p ~/.termux/boot
nano ~/.termux/boot/start-bot.sh
```
Add:
```bash
#!/data/data/com.termux/files/usr/bin/bash
termux-wake-lock
cd ~/telegram-mail-bot && ./start_bot.sh
```
Make executable:
```bash
chmod +x ~/.termux/boot/start-bot.sh
```

## 🏠 Home Screen Widget

1. Install **Termux:Widget** from F-Droid
2. Create shortcuts:
```bash
mkdir -p ~/.shortcuts

# Start shortcut
echo '#!/data/data/com.termux/files/usr/bin/bash
cd ~/telegram-mail-bot && ./start_bot.sh' > ~/.shortcuts/start-bot.sh

# Stop shortcut
echo '#!/data/data/com.termux/files/usr/bin/bash
pkill -f "python main.py" && echo "Bot stopped!"' > ~/.shortcuts/stop-bot.sh

chmod +x ~/.shortcuts/*.sh
```
3. Add widget to home screen

## 🔧 Troubleshooting

**Bot stops after screen lock?**
```bash
termux-wake-lock
```

**Module not found?**
```bash
pip install python-telegram-bot python-dotenv
```

**Permission denied?**
```bash
chmod +x *.sh
```

**Check if running:**
```bash
ps aux | grep python
```

**View errors:**
```bash
tail -50 bot.log
```

## 📊 Monitor Bot

Create status script:
```bash
echo '#!/data/data/com.termux/files/usr/bin/bash
if pgrep -f "python main.py" > /dev/null; then
    echo "✅ Bot is RUNNING"
    tail -5 ~/telegram-mail-bot/bot.log
else
    echo "❌ Bot is NOT running"
fi' > status.sh

chmod +x status.sh
```

Run: `./status.sh`

## ⚡ Pro Tips

1. **Keep phone plugged in**
2. **Use WiFi** (more stable)
3. **Disable battery optimization**
4. **Use wake lock**
5. **Install Termux:Boot**
6. **Check logs daily**

## 🎯 Essential Apps

Download from F-Droid:
- ✅ Termux (main app)
- ✅ Termux:Boot (auto-start)
- ✅ Termux:Widget (home shortcuts)
- ✅ Termux:API (optional, for notifications)

## ✅ Done!

Your bot is running 24/7 on your phone! 🎉

**Quick Access:**
- Start: `./start_bot.sh`
- Stop: `pkill -f "python main.py"`
- Logs: `tail -f bot.log`

For detailed guide, see `TERMUX_DEPLOYMENT.md`
