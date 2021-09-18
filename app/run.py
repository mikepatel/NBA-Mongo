################################################################################
# Imports
# import from other modules in /app/
from app import app
from layouts import index_layout
import callbacks


################################################################################
app.title = "NBA Prime"
app.layout = index_layout


################################################################################
# Main
if __name__ == "__main__":
    app.run_server(debug=True)
