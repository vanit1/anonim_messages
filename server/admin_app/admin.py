from quart import Quart, render_template, request, redirect, Blueprint
import uuid


blueprint = Blueprint("admin", __name__)

our_dct = {}

@blueprint.route("/admin", methods=["GET"])
async def admin():
    return "ADMIN"