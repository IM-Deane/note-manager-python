from client import create_app

app = create_app()

# Execute if file is run directly
if __name__ == '__main__':
    app.run(debug=True)