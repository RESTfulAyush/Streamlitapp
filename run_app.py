import subprocess
import threading
import time
import os
import requests

# Function to run FastAPI
def run_fastapi():
    # Use the dynamic PORT provided by Render or fallback to 8000
    port = os.getenv("PORT", 8000)
    subprocess.Popen(["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", str(port)])

# Start FastAPI in a background thread
threading.Thread(target=run_fastapi).start()

# Wait for FastAPI to start up by checking the API endpoint
while True:
    try:
        # Use the dynamic port (or default to 8000 if not found)
        port = os.getenv("PORT", 8000)
        response = requests.get(f"http://localhost:{port}")
        if response.status_code == 200:
            break  # FastAPI is ready
    except requests.ConnectionError:
        time.sleep(2)  # Retry every 2 seconds

# Start Streamlit (main web UI)
# Use the dynamic port for Streamlit
port = os.getenv("PORT", 8000)
os.system(f"streamlit run streamlit_app.py --server.port {port} --server.address 0.0.0.0")
