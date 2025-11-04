#!/usr/bin/env python3
"""
Telegram Mail Bot - Main Entry Point

This is the main entry point for the Telegram Mail Bot.
It initializes the bot, loads configuration, and starts the bot service.
"""

import os
import sys
import logging
from dotenv import load_dotenv
from bot.database.schema import initialize_database, verify_schema
from bot.utils import initialize_default_configs, verify_configs


def setup_logging():
    """Configure logging for the application"""
    log_level = os.getenv('LOG_LEVEL', 'INFO')
    log_file = os.getenv('LOG_FILE', 'bot.log')
    
    logging.basicConfig(
        level=getattr(logging, log_level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout)
        ]
    )


def initialize_system():
    """Initialize database and configuration files"""
    logger = logging.getLogger(__name__)
    
    # Get paths from environment or use defaults
    db_path = os.getenv('DATABASE_PATH', 'data/bot.db')
    config_dir = os.getenv('CONFIG_PATH', 'config')
    
    # Ensure data directory exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Initialize database
    logger.info("Initializing database...")
    if not initialize_database(db_path):
        logger.error("Database initialization failed")
        return False
    
    # Verify database schema
    if not verify_schema(db_path):
        logger.error("Database schema verification failed")
        return False
    
    # Initialize configuration files
    logger.info("Initializing configuration files...")
    if not initialize_default_configs(config_dir):
        logger.error("Configuration initialization failed")
        return False
    
    # Verify configuration files
    if not verify_configs(config_dir):
        logger.error("Configuration verification failed")
        return False
    
    logger.info("System initialization completed successfully")
    return True


def main():
    """Main function to start the bot"""
    # Load environment variables
    load_dotenv()
    
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Get bot token from environment
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not bot_token:
        logger.error("TELEGRAM_BOT_TOKEN not found in environment variables")
        sys.exit(1)
    
    logger.info("Starting Telegram Mail Bot...")
    
    # Initialize system (database and configs)
    if not initialize_system():
        logger.error("System initialization failed")
        sys.exit(1)
    
    # Initialize and start the bot
    from bot.bot_main import TelegramMailBot
    
    db_path = os.getenv('DATABASE_PATH', 'data/bot.db')
    config_path = os.getenv('CONFIG_PATH', 'config')
    
    bot = TelegramMailBot(bot_token, db_path, config_path)
    bot.start()


if __name__ == '__main__':
    main()
