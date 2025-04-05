from .template import BaseTemplate
from jinja2 import Environment, FileSystemLoader, TemplateNotFound


class JinjaTemplate(BaseTemplate):
    _instance = None  # Singleton instance

    def __new__(cls, template_dir: str = "templates"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.template_dir = template_dir
            cls._instance.env = Environment(
                loader=FileSystemLoader(template_dir),
                autoescape=True
            )
        return cls._instance

    def render(self, template_path: str, **context):
        if not template_path:
            raise ValueError("Template path is required.")
        if not self.template_exists(template_path):
            raise ValueError(f"Template does not exist: {template_path}")

        template = self.env.get_template(template_path)
        return template.render(**context)

    def render_template(self, request, template_path: str, **context):
        rendered = self.render(template_path, **context)
        request.send_response(200)
        request.send_header("Content-type", "text/html")
        request.end_headers()
        request.wfile.write(rendered.encode("utf-8"))

    def template_exists(self, template_path: str) -> bool:
        try:
            self.env.get_template(template_path)
            return True
        except TemplateNotFound:
            return False

    def set_template_dir(self, template_dir: str):
        self.template_dir = template_dir
        self.env.loader = FileSystemLoader(template_dir)