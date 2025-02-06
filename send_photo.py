import asyncio
import os
from aiogram import Bot
from dotenv import load_dotenv
from aiogram.types.input_file import FSInputFile

# Load environment variables from .env file
load_dotenv()

# Get sensitive data from environment variables
API_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")


async def send_photo():
    if not API_TOKEN or not CHANNEL_ID:
        print(
            "Error: BOT_TOKEN or CHANNEL_ID is missing from the environment variables."
        )
        return

    # Initialize bot
    bot = Bot(token=API_TOKEN)

    # Open the photo file in binary mode
    photo_path = "horizontal_2.jpg"  # Update with actual photo path
    try:
        with open(photo_path, "rb") as photo:
            # Send the photo with a caption
            photo = FSInputFile(photo_path, filename=os.path.basename(photo_path))
            await bot.send_photo(
                chat_id=CHANNEL_ID,
                photo=photo,
                caption="This is the caption text that goes with the photo.",
            )
    except FileNotFoundError:
        print(f"Error: The file '{photo_path}' was not found.")

    # Close bot session
    await bot.session.close()


# Run the function
if __name__ == "__main__":
    asyncio.run(send_photo())
