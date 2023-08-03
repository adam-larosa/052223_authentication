from werkzeug.exceptions import NotFound
from config import app


@app.errorhandler( NotFound )
def not_found( e ):
    return { 'error': 'route not found' }

