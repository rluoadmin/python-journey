import os

from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Now use your variables
api_key = os.environ.get("API")
print(api_key)  # This should print 'abc' if the .env file is correctly loaded
