from flask import Flask, jsonify, request, render_template
import aiohttp
import asyncio
from sssinstagram import down,instagram
app = Flask(__name__)
async def make_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

@app.route("/")
async def index():
    return render_template("index.html")

@app.route('/ping')
async def ping():
    return 'Pong!'

@app.route("/main/")
async def main():
    url = request.args.get('url')
    try:
        result = await make_request(f"https://apis.supercoders.uz/soqqa/apinx.php?url={url}")
        if isinstance(result, list):
            return jsonify(result)
        else:
            return jsonify({"status_code": 500, "detail": result}), 200
    except Exception as e:
        return jsonify({"status_code": 500, "detail": "Something went wrong, please contact t.me/shahzodbeeck"}), 200

@app.route("/insta/")
async def insta():
    url = request.args.get('url')
    try:
        result = await down(url)
        if isinstance(result, list):
            return jsonify(result)
        else:
            return jsonify({"status_code": 500, "detail": result}), 200
    except Exception as e:
        return jsonify({"status_code": 500, "detail": "Something went wrong, please contact t.me/shahzodbeeck"}), 200
@app.route("/insta2/")
async def insta2():
    url = request.args.get('url')
    try:
        result = await instagram(url)
        resul = {"status": True, 'result': result}
        if result['status'] == True:
            return jsonify(resul)
        else:
            return jsonify({"status_code": 500, "detail": result}), 200
    except Exception as e:
        return jsonify({"status_code": 500, "detail": "Something went wrong, please contact t.me/shahzodbeeck"}), 200

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.run(host="127.0.0.1", port=8000, debug=True))
