import os
from ext import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Use Railway's assigned port
    app.run(host="0.0.0.0", port=port)
