from ext import create_app
from routes import*
app = create_app()

app.run(host="0.0.0.0",)
