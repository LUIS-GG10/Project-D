from waitress import serve
from app import app  # Asegúrate de importar tu aplicación Flask

if __name__ == '__main__':
    serve(app, host='127.0.0.1', port=800)
