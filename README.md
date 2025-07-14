##Project Explanation video:-
https://drive.google.com/file/d/1i-OIS-QZ3gonk7SdE4zqVyKSoRUhiFci/view?usp=sharing

## Overview

This project is an AI-powered tool designed to generate detailed user personas by analyzing a Reddit user's public comments and posts. 
It leverages **FastAPI** for the backend API, **Streamlit** for an interactive web interface, and **Anthropic's Claude** Large Language Model (LLM) for persona generation.

The application scrapes a specified Reddit user's recent activity, processes this data, and then feeds it to an LLM to infer personality traits, motivations, frustrations, and more, providing citations from the Reddit data for transparency.

## Features

-   **Reddit Data Scraping**: Fetches a user's latest comments and posts using the PRAW library.
-   **AI-Powered Persona Generation**: Utilizes Anthropic's Claude LLM to create comprehensive user personas based on scraped data.
-   **Structured Persona Output**: Generates personas with sections like Basic Info, Personality Traits, Motivations, Goals & Needs, Frustrations, Behavior & Habits, and a representative Quote.
-   **Data Citation**: Each inferred characteristic in the persona is cited with the original Reddit comment/post ID and permalink.
-   **Interactive Web UI**: A user-friendly interface built with Streamlit allows easy input of Reddit URLs and displays the generated persona.
-   **Download Option**: Users can download the generated persona as a plain text file.
-   **Modular Design**: Clean separation of concerns with dedicated modules for scraping, persona building, backend API, and frontend UI.
-   **Secure API Key Handling**: Uses `.env` files to manage sensitive API credentials.

## Project Structure
Bilkul, bhai! GitHub repo ke liye yeh saari cheezein bahut zaroori hain. Ek proper README.md, executable instructions, aur sample output files—yeh sab professional dikhta hai.

Chalo, main tumhe README.md ka content bana ke deta hu, aur sample txt files ke liye kya content hoga, woh bhi outline kar deta hu. Tumhe bas yeh files banani hongi aur content paste karna hoga.

1. README.md File Content

Tumhe apne project root directory mein README.md naam ki file banani hogi aur usmein yeh content paste karna hoga.
Markdown

# Reddit User Persona Builder

## Overview

This project is an AI-powered tool designed to generate detailed user personas by analyzing a Reddit user's public comments and posts. It leverages **FastAPI** for the backend API, **Streamlit** for an interactive web interface, and **Anthropic's Claude** Large Language Model (LLM) for persona generation.

The application scrapes a specified Reddit user's recent activity, processes this data, and then feeds it to an LLM to infer personality traits, motivations, frustrations, and more, providing citations from the Reddit data for transparency.

## Features

-   **Reddit Data Scraping**: Fetches a user's latest comments and posts using the PRAW library.
-   **AI-Powered Persona Generation**: Utilizes Anthropic's Claude LLM to create comprehensive user personas based on scraped data.
-   **Structured Persona Output**: Generates personas with sections like Basic Info, Personality Traits, Motivations, Goals & Needs, Frustrations, Behavior & Habits, and a representative Quote.
-   **Data Citation**: Each inferred characteristic in the persona is cited with the original Reddit comment/post ID and permalink.
-   **Interactive Web UI**: A user-friendly interface built with Streamlit allows easy input of Reddit URLs and displays the generated persona.
-   **Download Option**: Users can download the generated persona as a plain text file.
-   **Modular Design**: Clean separation of concerns with dedicated modules for scraping, persona building, backend API, and frontend UI.
-   **Secure API Key Handling**: Uses `.env` files to manage sensitive API credentials.

## Project Structure

reddit-persona-app/
├── .env                  # Environment variables (API keys)
├── main.py               # FastAPI backend application
├── app.py                # Streamlit frontend application
├── requirements.txt      # Python dependencies
├── README.md             # This file
└── src/
├── init.py       # Makes 'src' a Python package
├── persona_builder.py  # Logic for AI persona generation
└── reddit_scraper.py   # Logic for scraping Reddit data



## Prerequisites

Go to 
https://www.reddit.com/prefs/apps

 Create a Reddit Developer Account

Step 1: Log In and Navigate
First, ensure you are logged in to your Reddit account. Then, open your browser and go to this URL:
https://www.reddit.com/prefs/apps

Step 2: Start a New Application
On that page, you will see an option to either "Are you a developer? Create an app..." or, if you already have apps, "Create another app." Click on it.

Step 3: Fill Out the Application Form
A form will appear. You need to fill in the following details:

    name: Give your application a meaningful name, like "MyPersonaBuilder".

    Choose app type: Select "script". This type is best suited for private applications that run on your local machine.

    description: This field is optional; you can write anything you like or leave it blank.

    about url: This is also optional; you can leave it empty.

    redirect uri: This is crucial! You must enter it exactly as follows: http://localhost:8080 (This is the standard for script-type applications).

Step 4: Create the Application
After filling in all the details, click on the "create app" button.

Step 5: Retrieve Your Credentials
Once your application is successfully created, you will find two important pieces of information under the "personal use script" section:

    Client ID: This is your REDDIT_CLIENT_ID.

    Secret: This is your REDDIT_CLIENT_SECRET.

Step 6: Define Your User Agent
You will need to define your own User Agent. This is a string that identifies your application to the Reddit server. The best format is:
platform:App-Name:vX.Y.Z (by /u/YourRedditUsername)

For example:
windows:MyPersonaBuilder:v1.0.0 (by /u/YourRedditUsername)

That's it! Your Reddit Developer Account is now set up, and you can proceed with building your application.






Before you begin, ensure you have the following installed:

-   **Python 3.10+**
-   **pip** (Python package installer)
-   **Git** (for cloning the repository)

## Setup Instructions

Follow these steps to get the project up and running on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/varunrathour1/reddit-persona-app.git
cd reddit-persona-app



# Create a virtual environment
python -m venv news_hunter_env

# Activate the virtual environment
# On Windows:
.\news_hunter_env\Scripts\activate
# On macOS/Linux:
source news_hunter_env/bin/activate

OR USE COBDA  ENV 

 Install Dependencies
pip install -r requirements.txt


Set up Environment Variables
# Reddit API Credentials (Get these from Reddit App Preferences: [https://www.reddit.com/prefs/apps/](https://www.reddit.com/prefs/apps/))
REDDIT_CLIENT_ID="YOUR_REDDIT_CLIENT_ID"
REDDIT_CLIENT_SECRET="YOUR_REDDIT_CLIENT_SECRET"
REDDIT_USER_AGENT="YourAppNameByYourRedditUsernameV1.0" # e.g., "PersonaBuilderAppByYourRedditUsernameV1.0"

# Anthropic API Key (Get this from Anthropic Console: [https://console.anthropic.com/settings/api-keys](https://console.anthropic.com/settings/api-keys))
ANTHROPIC_API_KEY="YOUR_ANTHROPIC_API_KEY"




1. Start the FastAPI Backend
# Make sure your virtual environment is active

# .\news_hunter_env\Scripts\activate (Windows) 
                OR 
source news_hunter_env/bin/activate (macOS/Linux)


uvicorn main:app --reload 
 on one terminal keepi it running 


on another terminal start frontend streamlit
# Make sure your virtual environment is active
# .\news_hunter_env\Scripts\activate (Windows) OR source news_hunter_env/bin/activate (macOS/Linux)

streamlit run app.py



How to Use the App

    Once the Streamlit app is open in your browser, you will see a text input field for "Reddit User Profile URL".

    Paste the full URL of the Reddit user's profile whose persona you want to generate (e.g., https://www.reddit.com/user/kojied/ or https://www.reddit.com/user/reddit/).

    Click the "Build Persona" button.

    The app will display a loading spinner while it scrapes data and generates the persona.

    After a few moments, the detailed AI-generated persona will appear on the screen, including citations to original Reddit content.

    You can use the "Download Persona as Text" button to save the generated persona to your local machine




















