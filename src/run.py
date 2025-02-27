from src.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

# vercel serverless
def handler(event, context):
    return app(event, context)