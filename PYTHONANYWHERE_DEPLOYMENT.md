# Deploying Telegram Mail Bot on PythonAnywhere

This guide will walk you through deploying your Telegram Mail Bot on PythonAnywhere.

## Prerequisites

1. A PythonAnywhere account (free tier works fine)
2. Your Telegram bot token from @BotFather
3. Your bot files ready to upload

## Step-by-Step Deployment

### Step 1: Sign Up for PythonAnywhere

1. Go to [https://www.pythonanywhere.com](https://www.pythonanywhere.com)
2. Click "Start running Python online in less than a minute!"
3. Create a free account (Beginner account is sufficient)

### Step 2: Upload Your Bot Files

**Option A: Using Git (Recommended)**

1. Go to the "Consoles" tab in PythonAnywhere
2. Click "Bash" to open a bash console
3. Clone your repository:
   ```bash
   git clone <your-repository-url>
   cd telegram-mail-bot
   ```

**Option B: Manual Upload**

1. Go to the "Files" tab
2. Create a new directory: `telegram-mail-bot`
3. Upload all your bot files to this directory
4. Or use the "Upload a file" button to upload a zip file and extract it

### Step 3: Set Up Virtual Environment

In the Bash console:

```bash
# Navigate to your bot directory
cd ~/telegram-mail-bot

# Create a virtual environment
python3.10 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file:

```bash
# In the bash console
cd ~/telegram-mail-bot
nano .env
```

Add your configuration:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
DATABASE_PATH=/home/yourusername/telegram-mail-bot/data/bot.db
CONFIG_PATH=/home/yourusername/telegram-mail-bot/config
LOG_LEVEL=INFO
LOG_FILE=/home/yourusername/telegram-mail-bot/bot.log
```

**Important:** Replace `yourusername` with your actual PythonAnywhere username!

Press `Ctrl+X`, then `Y`, then `Enter` to save.

### Step 5: Create Required Directories

```bash
mkdir -p data
mkdir -p config
```

### Step 6: Test Your Bot Locally

```bash
# Make sure you're in the virtual environment
source venv/bin/activate

# Run the bot
python main.py
```

If it starts without errors, press `Ctrl+C` to stop it. You should see:
```
INFO - Starting Telegram Mail Bot...
INFO - Database initialization completed successfully
INFO - Bot is running...
```

### Step 7: Create an Always-On Task

PythonAnywhere free accounts don't support always-on tasks, but you can use a **scheduled task** to keep your bot running.

#### Create a Startup Script

Create a file called `start_bot.sh`:

```bash
cd ~/telegram-mail-bot
nano start_bot.sh
```

Add this content:
```bash
#!/bin/bash
cd /home/yourusername/telegram-mail-bot
source venv/bin/activate

# Check if bot is already running
if pgrep -f "python main.py" > /dev/null
then
    echo "Bot is already running"
else
    echo "Starting bot..."
    nohup python main.py > bot_output.log 2>&1 &
    echo "Bot started"
fi
```

Make it executable:
```bash
chmod +x start_bot.sh
```

#### Set Up Scheduled Task

1. Go to the "Tasks" tab in PythonAnywhere
2. In the "Scheduled tasks" section, add a new task:
   - **Command:** `/home/yourusername/telegram-mail-bot/start_bot.sh`
   - **Hour:** Choose any hour (e.g., 00:00 UTC)
   - **Frequency:** Daily

This will restart your bot once per day if it stops.

### Step 8: Start Your Bot

Run the startup script manually:
```bash
cd ~/telegram-mail-bot
./start_bot.sh
```

Check if it's running:
```bash
ps aux | grep "python main.py"
```

You should see your bot process running.

### Step 9: Monitor Your Bot

Check the logs:
```bash
cd ~/telegram-mail-bot
tail -f bot.log
```

Or check the output log:
```bash
tail -f bot_output.log
```

Press `Ctrl+C` to stop viewing logs.

## Important Notes for PythonAnywhere Free Tier

### Limitations

1. **No Always-On Tasks**: Free accounts can't run processes 24/7
2. **Daily Restart Required**: Your bot will need to be restarted daily
3. **Console Timeout**: Bash consoles timeout after inactivity
4. **CPU Seconds**: Limited to 100 CPU seconds per day

### Workarounds

**Option 1: Upgrade to Paid Account ($5/month)**
- Allows always-on tasks
- Your bot runs 24/7 without interruption
- More CPU seconds

**Option 2: Use Scheduled Tasks (Free)**
- Set up the scheduled task as described above
- Bot restarts daily
- May have downtime between restarts

**Option 3: Use a Keep-Alive Script**

Create `keep_alive.sh`:
```bash
#!/bin/bash
while true; do
    if ! pgrep -f "python main.py" > /dev/null; then
        cd /home/yourusername/telegram-mail-bot
        source venv/bin/activate
        nohup python main.py > bot_output.log 2>&1 &
    fi
    sleep 300  # Check every 5 minutes
done
```

Run it in a console:
```bash
chmod +x keep_alive.sh
nohup ./keep_alive.sh &
```

**Note:** This console will timeout after inactivity on free tier.

## Managing Your Bot

### Stop the Bot

```bash
pkill -f "python main.py"
```

### Restart the Bot

```bash
pkill -f "python main.py"
./start_bot.sh
```

### Update the Bot

```bash
cd ~/telegram-mail-bot
git pull  # If using git
source venv/bin/activate
pip install -r requirements.txt --upgrade
pkill -f "python main.py"
./start_bot.sh
```

### View Logs

```bash
cd ~/telegram-mail-bot
tail -f bot.log
```

### Check Database

```bash
cd ~/telegram-mail-bot
sqlite3 data/bot.db
# SQLite commands:
# .tables          - List all tables
# .schema admins   - Show table structure
# SELECT * FROM admins;  - View admins
# .quit            - Exit
```

## Troubleshooting

### Bot Not Starting

1. Check the logs:
   ```bash
   cat bot.log
   cat bot_output.log
   ```

2. Verify environment variables:
   ```bash
   cat .env
   ```

3. Test manually:
   ```bash
   source venv/bin/activate
   python main.py
   ```

### "Module not found" Error

```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Database Permission Error

```bash
chmod 755 ~/telegram-mail-bot/data
chmod 644 ~/telegram-mail-bot/data/bot.db
```

### Bot Token Invalid

1. Get a new token from @BotFather
2. Update `.env` file
3. Restart the bot

## Alternative: Using Webhook (Advanced)

For better reliability on PythonAnywhere, you can modify your bot to use webhooks instead of polling:

1. This requires a paid PythonAnywhere account (for HTTPS)
2. Modify `bot_main.py` to use webhooks
3. Set up a Flask web app to receive updates

This is more complex but more reliable for free hosting.

## Recommended: Better Free Alternatives

If PythonAnywhere's limitations are too restrictive, consider:

1. **Railway.app** - Free tier with always-on support
2. **Render.com** - Free tier with 750 hours/month
3. **Fly.io** - Free tier with always-on support
4. **Heroku alternatives** - Various free options

Would you like a guide for any of these alternatives?

## Summary

Your bot is now deployed on PythonAnywhere! 

**Quick Commands:**
- Start: `./start_bot.sh`
- Stop: `pkill -f "python main.py"`
- Logs: `tail -f bot.log`
- Status: `ps aux | grep "python main.py"`

For 24/7 operation, consider upgrading to a paid PythonAnywhere account ($5/month) or using an alternative hosting service.
