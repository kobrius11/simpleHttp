from abc import ABC, abstractmethod


class BaseTemplate(ABC):
    @abstractmethod
    def render(self, template_path: str, **context):
        pass

    @abstractmethod
    def render_template(self, request, template_path: str, **context):
        pass

    @abstractmethod
    def template_exists(self, template_path: str) -> bool:
        pass

    @abstractmethod
    def set_template_dir(self, template_path: str):
        pass
    
