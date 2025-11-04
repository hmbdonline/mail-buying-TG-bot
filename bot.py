"""
Telegram Mail Bot - Single File Version
Simplified version for easy hosting
"""

import os
import logging
import sqlite3
import json
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ============================================
# CONFIGURATION - Add your bot token here
# ============================================
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace with your actual bot token
MAIN_ADMIN_USERNAME = "@s00s22"     # Replace with your Telegram username
# ============================================

# Initialize database
def init_database():
    """Initialize SQLite database"""
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            is_blocked INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admins (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            is_main_admin INTEGER DEFAULT 0,
            permissions TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id TEXT PRIMARY KEY,
            user_id INTEGER NOT NULL,
            amount REAL,
            status TEXT,
            details TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            completed_at TIMESTAMP
        )
    ''')
    
    # Create main admin if not exists
    cursor.execute(
        "INSERT OR IGNORE INTO admins (user_id, username, is_main_admin) VALUES (?, ?, ?)",
        (0, MAIN_ADMIN_USERNAME, 1)
    )
    
    conn.commit()
    conn.close()
    logger.info("Database initialized")

# Database helper functions
def register_user(user_id, username, first_name, last_name):
    """Register or update user"""
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO users (user_id, username, first_name, last_name)
        VALUES (?, ?, ?, ?)
    ''', (user_id, username, first_name, last_name))
    conn.commit()
    conn.close()

def is_admin(user_id):
    """Check if user is admin"""
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM admins WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def is_main_admin(user_id):
    """Check if user is main admin"""
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute("SELECT user_id FROM admins WHERE user_id = ? AND is_main_admin = 1", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result is not None

def is_user_blocked(user_id):
    """Check if user is blocked"""
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute("SELECT is_blocked FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result and result[0] == 1

# Command handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    user = update.effective_user
    
    # Register user
    register_user(user.id, user.username, user.first_name, user.last_name)
    
    # Check if blocked
    if is_user_blocked(user.id):
        await update.message.reply_text(
            "You have been blocked from using this bot."
        )
        return
    
    # Welcome message
    welcome_text = (
        f"👋 Welcome to Mail Purchase Bot!\n\n"
        f"Hello {user.first_name}!\n\n"
        f"Use /help to see available commands."
    )
    
    # Create keyboard
    keyboard = [
        [InlineKeyboardButton("📧 Buy Mail", callback_data="buy_mail")],
        [InlineKeyboardButton("📊 My Transactions", callback_data="my_transactions")],
        [InlineKeyboardButton("❓ Help", callback_data="help")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    help_text = (
        "📖 *Help*\n\n"
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/admin - Admin panel (admins only)\n\n"
        "Use the buttons to navigate and make purchases."
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /admin command"""
    user_id = update.effective_user.id
    
    if not is_admin(user_id):
        await update.message.reply_text("🚫 This command is only available to administrators.")
        return
    
    # Admin menu
    keyboard = [
        [InlineKeyboardButton("👥 Manage Users", callback_data="admin_users")],
        [InlineKeyboardButton("💰 View Transactions", callback_data="admin_transactions")],
        [InlineKeyboardButton("📊 Statistics", callback_data="admin_stats")],
        [InlineKeyboardButton("❌ Close", callback_data="admin_close")]
    ]
    
    if is_main_admin(user_id):
        keyboard.insert(0, [InlineKeyboardButton("👑 Manage Admins", callback_data="admin_manage_admins")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👑 *Admin Panel*\n\nSelect an option:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button callbacks"""
    query = update.callback_query
    await query.answer()
    
    callback_data = query.data
    user_id = update.effective_user.id
    
    # Handle different callbacks
    if callback_data == "buy_mail":
        await query.message.reply_text(
            "📧 *Mail Purchase*\n\n"
            "Please contact support to complete your purchase.\n"
            "This feature will be fully implemented soon!",
            parse_mode='Markdown'
        )
    
    elif callback_data == "my_transactions":
        # Get user transactions
        conn = sqlite3.connect('bot.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT transaction_id, amount, status, created_at FROM transactions WHERE user_id = ? ORDER BY created_at DESC LIMIT 5",
            (user_id,)
        )
        transactions = cursor.fetchall()
        conn.close()
        
        if transactions:
            text = "📊 *Your Recent Transactions*\n\n"
            for txn in transactions:
                text += f"ID: {txn[0]}\n"
                text += f"Amount: ${txn[1]}\n"
                text += f"Status: {txn[2]}\n"
                text += f"Date: {txn[3]}\n\n"
        else:
            text = "You have no transactions yet."
        
        await query.message.reply_text(text, parse_mode='Markdown')
    
    elif callback_data == "help":
        await help_command(update, context)
    
    elif callback_data.startswith("admin_"):
        if not is_admin(user_id):
            await query.message.reply_text("🚫 Admin access required.")
            return
        
        if callback_data == "admin_close":
            await query.message.delete()
        
        elif callback_data == "admin_users":
            conn = sqlite3.connect('bot.db')
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM users")
            user_count = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM users WHERE is_blocked = 1")
            blocked_count = cursor.fetchone()[0]
            conn.close()
            
            await query.message.reply_text(
                f"👥 *User Statistics*\n\n"
                f"Total Users: {user_count}\n"
                f"Blocked Users: {blocked_count}\n"
                f"Active Users: {user_count - blocked_count}",
                parse_mode='Markdown'
            )
        
        elif callback_data == "admin_transactions":
            conn = sqlite3.connect('bot.db')
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM transactions")
            total = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM transactions WHERE status = 'completed'")
            completed = cursor.fetchone()[0]
            cursor.execute("SELECT SUM(amount) FROM transactions WHERE status = 'completed'")
            total_amount = cursor.fetchone()[0] or 0
            conn.close()
            
            await query.message.reply_text(
                f"💰 *Transaction Statistics*\n\n"
                f"Total Transactions: {total}\n"
                f"Completed: {completed}\n"
                f"Total Amount: ${total_amount:.2f}",
                parse_mode='Markdown'
            )
        
        elif callback_data == "admin_stats":
            conn = sqlite3.connect('bot.db')
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM users")
            users = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM transactions")
            transactions = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM admins")
            admins = cursor.fetchone()[0]
            conn.close()
            
            await query.message.reply_text(
                f"📊 *Bot Statistics*\n\n"
                f"👥 Users: {users}\n"
                f"💰 Transactions: {transactions}\n"
                f"👑 Admins: {admins}",
                parse_mode='Markdown'
            )
        
        else:
            await query.message.reply_text(
                "This feature is not yet implemented."
            )

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors"""
    logger.error(f"Exception while handling an update: {context.error}")

def main():
    """Start the bot"""
    if not BOT_TOKEN or BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        logger.error("Please set your BOT_TOKEN in the bot.py file!")
        logger.error("Replace 'YOUR_BOT_TOKEN_HERE' with your actual bot token")
        return
    
    # Initialize database
    init_database()
    
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("admin", admin_command))
    application.add_handler(CallbackQueryHandler(button_callback))
    application.add_error_handler(error_handler)
    
    # Start bot
    logger.info("Bot started!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
