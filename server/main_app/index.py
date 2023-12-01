from quart import Quart, render_template, request, redirect, Blueprint
import uuid


blueprint = Blueprint("main_app", __name__)

our_dct = {}

@blueprint.route("/", methods=["GET"])
async def home():
    return await render_template("index.html", count_messages=len(our_dct))


@blueprint.route("/anonim", methods=["POST"])
async def anonim_form():
    global our_dct
    data = await request.form
    key = uuid.uuid4().hex
    our_dct[key] = {"pass_word": data["pass_word"], "secret_message": data["message"]}
    return await render_template("key.html", key=key)


@blueprint.route("/get_anonim", methods=["POST"])
async def give_message():
    global our_dct
    data = await request.form
    secret_message = our_dct.get(data["pass_key"], None)
    if secret_message:
        return await render_template(
            "secret_message.html",
            secret_message=secret_message["secret_message"]
        )
    return await render_template(
        "index.html",
        errors_give="Введено неправильний ключ"
    )