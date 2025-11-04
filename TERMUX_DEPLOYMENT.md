# Deploying Telegram Mail Bot on Termux (Android)

This guide will help you run your Telegram bot 24/7 on your Android phone using Termux.

## Prerequisites

- Android phone (Android 7.0 or higher)
- Termux app installed from F-Droid (NOT Google Play Store)
- Stable internet connection
- Your Telegram bot token

## Why Termux?

✅ **Advantages:**
- Free 24/7 hosting
- Full control over your bot
- No external server needed
- Works offline (local network)
- Low power consumption

⚠️ **Considerations:**
- Phone must stay on
- Requires stable internet
- Battery drain (use charger)
- May need to disable battery optimization

## Step-by-Step Setup

### Step 1: Install Termux

**Important:** Install from F-Droid, NOT Google Play Store!

1. Download F-Droid from [https://f-droid.org](https://f-droid.org)
2. Install F-Droid APK
3. Open F-Droid and search for "Termux"
4. Install Termux

**Why F-Droid?** The Google Play version is outdated and has issues.

### Step 2: Initial Termux Setup

Open Termux and run these commands:

```bash
# Update packages
pkg update && pkg upgrade -y

# Install required packages
pkg install python git nano wget -y

# Install pip
pip install --upgrade pip
```

### Step 3: Get Your Bot Files

**Option A: From Git (Recommended)**

```bash
# Clone your repository
git clone <your-repository-url>
cd telegram-mail-bot
```

**Option B: Manual Transfer**

1. Copy your bot folder to phone storage
2. In Termux:
```bash
# Allow Termux to access storage
termux-setup-storage

# Copy from phone storage
cp -r ~/storage/downloads/telegram-mail-bot ~/
cd ~/telegram-mail-bot
```

### Step 4: Install Python Dependencies

```bash
# Make sure you're in the bot directory
cd ~/telegram-mail-bot

# Install dependencies
pip install -r requirements.txt
```

**If you get errors**, try:
```bash
pip install python-telegram-bot python-dotenv
```

### Step 5: Configure Your Bot

Create the `.env` file:

```bash
nano .env
```

Add your configuration:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
DATABASE_PATH=/data/data/com.termux/files/home/telegram-mail-bot/data/bot.db
CONFIG_PATH=/data/data/com.termux/files/home/telegram-mail-bot/config
LOG_LEVEL=INFO
LOG_FILE=/data/data/com.termux/files/home/telegram-mail-bot/bot.log
```

**Save:** Press `Ctrl+X`, then `Y`, then `Enter`

### Step 6: Create Required Directories

```bash
mkdir -p data
mkdir -p config
```

### Step 7: Test Your Bot

```bash
python main.py
```

You should see:
```
INFO - Starting Telegram Mail Bot...
INFO - Database initialization completed successfully
INFO - Bot is running...
```

Test it by messaging your bot on Telegram with `/start`

Press `Ctrl+C` to stop the bot.

### Step 8: Create Startup Script

Create a script to run the bot in the background:

```bash
nano start_bot.sh
```

Add this content:
```bash
#!/data/data/com.termux/files/usr/bin/bash

cd ~/telegram-mail-bot

# Check if bot is already running
if pgrep -f "python main.py" > /dev/null; then
    echo "Bot is already running!"
    exit 0
fi

# Start the bot in background
nohup python main.py > bot_output.log 2>&1 &

echo "Bot started! PID: $!"
echo "View logs: tail -f ~/telegram-mail-bot/bot.log"
```

Make it executable:
```bash
chmod +x start_bot.sh
```

### Step 9: Create Stop Script

```bash
nano stop_bot.sh
```

Add:
```bash
#!/data/data/com.termux/files/usr/bin/bash

if pgrep -f "python main.py" > /dev/null; then
    pkill -f "python main.py"
    echo "Bot stopped!"
else
    echo "Bot is not running."
fi
```

Make it executable:
```bash
chmod +x stop_bot.sh
```

### Step 10: Start Your Bot

```bash
./start_bot.sh
```

Check if it's running:
```bash
ps aux | grep python
```

View logs:
```bash
tail -f bot.log
```

## Keep Bot Running 24/7

### Method 1: Using Termux:Boot (Recommended)

Install Termux:Boot from F-Droid to auto-start bot on phone reboot.

1. Install Termux:Boot from F-Droid
2. Create boot script:
```bash
mkdir -p ~/.termux/boot
nano ~/.termux/boot/start-bot.sh
```

Add:
```bash
#!/data/data/com.termux/files/usr/bin/bash
termux-wake-lock
cd ~/telegram-mail-bot
./start_bot.sh
```

Make executable:
```bash
chmod +x ~/.termux/boot/start-bot.sh
```

3. Reboot your phone - bot will auto-start!

### Method 2: Using Termux:Widget

Create a home screen widget to start/stop bot easily.

1. Install Termux:Widget from F-Droid
2. Create shortcuts:
```bash
mkdir -p ~/.shortcuts
```

Create start shortcut:
```bash
nano ~/.shortcuts/start-bot.sh
```
Add:
```bash
#!/data/data/com.termux/files/usr/bin/bash
cd ~/telegram-mail-bot && ./start_bot.sh
```

Create stop shortcut:
```bash
nano ~/.shortcuts/stop-bot.sh
```
Add:
```bash
#!/data/data/com.termux/files/usr/bin/bash
cd ~/telegram-mail-bot && ./stop_bot.sh
```

Make executable:
```bash
chmod +x ~/.shortcuts/*.sh
```

3. Add Termux:Widget to home screen
4. Tap widget to start/stop bot

## Battery Optimization

To prevent Android from killing Termux:

### Disable Battery Optimization

1. Go to **Settings** → **Apps** → **Termux**
2. Tap **Battery** → **Battery optimization**
3. Select **All apps**
4. Find **Termux** and set to **Don't optimize**

### Acquire Wake Lock

In Termux:
```bash
termux-wake-lock
```

This prevents the device from sleeping while bot runs.

To release:
```bash
termux-wake-unlock
```

### Keep Screen On (Optional)

Add to your start script:
```bash
termux-wake-lock
```

## Daily Management

### Quick Commands

**Start bot:**
```bash
cd ~/telegram-mail-bot && ./start_bot.sh
```

**Stop bot:**
```bash
cd ~/telegram-mail-bot && ./stop_bot.sh
```

**Restart bot:**
```bash
cd ~/telegram-mail-bot && ./stop_bot.sh && ./start_bot.sh
```

**View logs:**
```bash
cd ~/telegram-mail-bot && tail -f bot.log
```

**Check if running:**
```bash
ps aux | grep "python main.py"
```

**View bot output:**
```bash
cd ~/telegram-mail-bot && tail -f bot_output.log
```

### Update Bot

```bash
cd ~/telegram-mail-bot
git pull  # If using git
pip install -r requirements.txt --upgrade
./stop_bot.sh
./start_bot.sh
```

## Monitoring Your Bot

### Create Status Script

```bash
nano status.sh
```

Add:
```bash
#!/data/data/com.termux/files/usr/bin/bash

echo "=== Bot Status ==="
if pgrep -f "python main.py" > /dev/null; then
    echo "✅ Bot is RUNNING"
    echo "PID: $(pgrep -f 'python main.py')"
    echo ""
    echo "Last 5 log entries:"
    tail -5 ~/telegram-mail-bot/bot.log
else
    echo "❌ Bot is NOT running"
fi
```

Make executable:
```bash
chmod +x status.sh
```

Run it:
```bash
./status.sh
```

## Troubleshooting

### Bot Stops After Screen Lock

**Solution:** Disable battery optimization and use wake lock
```bash
termux-wake-lock
```

### "Permission Denied" Errors

```bash
chmod +x *.sh
```

### "Module not found" Error

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install python-telegram-bot python-dotenv
```

### Bot Not Responding

1. Check if running:
```bash
ps aux | grep python
```

2. Check logs:
```bash
tail -50 bot.log
```

3. Restart:
```bash
./stop_bot.sh && ./start_bot.sh
```

### Termux Closes Automatically

- Disable battery optimization for Termux
- Use `termux-wake-lock`
- Install Termux:Boot for auto-restart

### Database Locked Error

```bash
# Stop bot
./stop_bot.sh

# Remove lock
rm data/bot.db-journal

# Restart
./start_bot.sh
```

## Advanced: Run Bot as Service

Create a more robust service script:

```bash
nano bot_service.sh
```

Add:
```bash
#!/data/data/com.termux/files/usr/bin/bash

while true; do
    if ! pgrep -f "python main.py" > /dev/null; then
        echo "$(date): Bot stopped, restarting..." >> ~/telegram-mail-bot/service.log
        cd ~/telegram-mail-bot
        nohup python main.py > bot_output.log 2>&1 &
    fi
    sleep 60  # Check every minute
done
```

Run it:
```bash
chmod +x bot_service.sh
nohup ./bot_service.sh &
```

This will automatically restart your bot if it crashes!

## Tips for Best Performance

1. **Keep phone plugged in** - Prevents battery drain
2. **Use WiFi** - More stable than mobile data
3. **Disable battery optimization** - Prevents Termux from being killed
4. **Use wake lock** - Keeps bot running
5. **Monitor logs regularly** - Catch issues early
6. **Set up auto-restart** - Use Termux:Boot
7. **Keep Termux updated** - Run `pkg upgrade` weekly

## Backup Your Bot

### Backup Script

```bash
nano backup.sh
```

Add:
```bash
#!/data/data/com.termux/files/usr/bin/bash

BACKUP_DIR=~/telegram-mail-bot-backup-$(date +%Y%m%d)
mkdir -p $BACKUP_DIR

cp -r ~/telegram-mail-bot/data $BACKUP_DIR/
cp -r ~/telegram-mail-bot/config $BACKUP_DIR/
cp ~/telegram-mail-bot/.env $BACKUP_DIR/
cp ~/telegram-mail-bot/*.log $BACKUP_DIR/

echo "Backup created at: $BACKUP_DIR"
```

Run weekly:
```bash
chmod +x backup.sh
./backup.sh
```

## Summary

Your bot is now running 24/7 on your Android phone! 🎉

**Essential Commands:**
- Start: `./start_bot.sh`
- Stop: `./stop_bot.sh`
- Status: `./status.sh`
- Logs: `tail -f bot.log`

**Remember:**
- Keep phone charged
- Disable battery optimization
- Use `termux-wake-lock`
- Install Termux:Boot for auto-start

## Alternative: Use VPS

If running on phone is not ideal, consider:
- **Oracle Cloud** - Free VPS forever
- **Google Cloud** - $300 free credit
- **AWS** - 12 months free tier
- **DigitalOcean** - $200 free credit

Would you like a guide for any of these?
