import subprocess
import threading
import time
import os
import requests

# Function to run FastAPI
def run_fastapi():
    subprocess.Popen(["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"])

# Start FastAPI in a background thread
threading.Thread(target=run_fastapi).start()

# Wait for FastAPI to start up by checking the API endpoint
while True:
    try:
        response = requests.get("http://localhost:8000")
        if response.status_code == 200:
            break  # FastAPI is ready
    except requests.ConnectionError:
        time.sleep(2)  # Retry every 2 seconds

# Start Streamlit (main web UI)
os.system("streamlit run streamlit_app.py --server.port 10000 --server.address 0.0.0.0")
