from src.app import App


app = App()


@app.route("GET", "/")
def home(request):
    return app.template_engine.render_template(request, "index.html")

@app.route("GET", "/about")
def about(request):
    return app.template_engine.render_template(request, "about.html")

@app.route("GET", "/hello")
def hello(request):
    request.send_response(200)
    request.send_header("Content-type", "text/html")
    request.end_headers()
    request.wfile.write(b"Hello, from the /hello route!")

if __name__ == "__main__":
    app.run()