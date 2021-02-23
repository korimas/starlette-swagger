from starlette.responses import HTMLResponse, FileResponse
from starlette.applications import Starlette
from starlette_openapi import OpenApi
import os


class SwaggerUI(object):

    def __init__(
            self,
            app: Starlette,
            openapi: OpenApi,
            url='/docs',
            css_url="/swagger-ui/swagger-ui.css",
            js_url="/swagger-ui/swagger-ui-bundle.js"
    ):
        self.app = app
        self.doc_url = url
        self.openapi = openapi
        self.css_url = css_url
        self.js_url = js_url
        self.setup_route()

    def setup_route(self):
        self.app.add_route(self.doc_url, self.get_html_content, include_in_schema=False)
        self.app.add_route(self.css_url, self.get_css_content, include_in_schema=False)
        self.app.add_route(self.js_url, self.get_js_content, include_in_schema=False)

    def get_css_content(self, request):
        css_path = os.path.dirname(__file__) + "/static/swagger-ui.css"
        return FileResponse(css_path)

    def get_js_content(self, request):
        js_path = os.path.dirname(__file__) + "/static/swagger-ui-bundle.js"
        return FileResponse(js_path)

    def get_html_content(self, request):
        title = "SwaggerUI"
        oauth2_redirect_url = None  # TODO
        init_oauth = None  # TODO
        html = f"""
                 <!DOCTYPE html>
                 <html>
                 <head>
                 <link type="text/css" rel="stylesheet" href="{self.css_url}">
                 <title>{title}</title>
                 </head>
                 <body>
                 <div id="swagger-ui">
                 </div>
                 <script src="{self.js_url}"></script>
                 <!-- `SwaggerUIBundle` is now available on the page -->
                 <script>
                 const ui = SwaggerUIBundle({{
                     url: '{self.openapi.api_url}',
                 """

        if oauth2_redirect_url:
            html += f"oauth2RedirectUrl: window.location.origin + '{oauth2_redirect_url}',"

        html += """
                     dom_id: '#swagger-ui',
                     presets: [
                     SwaggerUIBundle.presets.apis,
                     SwaggerUIBundle.SwaggerUIStandalonePreset
                     ],
                     layout: "BaseLayout",
                     deepLinking: true,
                     showExtensions: true,
                     showCommonExtensions: true
                 })"""

        # if init_oauth:
        #     html += f"""
        #         ui.initOAuth({json.dumps(jsonable_encoder(init_oauth))})
        #         """

        html += """
                 </script>
                 </body>
                 </html>
                 """
        return HTMLResponse(html)

    def set_theme(self):
        pass
