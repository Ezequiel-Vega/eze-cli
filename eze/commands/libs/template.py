from eze.commands.libs.template_api import TemplateApi

class Template(object):
    def __init__(self, api: bool, name: str):
        self.api = api
        self.name = name
        self.create_template()

    def create_template(self):
        if self.api:
            template: TemplateApi = TemplateApi(self.name)
            template.create()
        else:
            pass
