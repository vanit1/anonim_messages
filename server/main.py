from quart import Quart, render_template, request, redirect, Blueprint
import uuid
from server.main_app.index import blueprint as main_blueprint
from server.admin_app.admin import blueprint as admin_blueprint

app = Quart(__name__, template_folder="../templates", static_folder="../static")


def main():
    app.register_blueprint(main_blueprint)
    app.register_blueprint(admin_blueprint)


if __name__ == "__main__":
    main()
    app.run(debug=True, port=8081)