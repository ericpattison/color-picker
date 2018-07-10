import asyncio
from flask import Flask, request, render_template
import gensim.downloader as api

model = None

async def loadModel(future):
    print("loading...")
    loadedModel = api.load("fasttext-wiki-news-subwords-300")
    return loadedModel

def modelLoaded(future):
    print("loaded")
    model = future.result()

app = Flask(__name__)

@app.route('/')
def canary():
    return 'Hello, world!'

@app.route('/test')
def test_model():
    return 'Loading' if model==None else model.n_similarity(['sushi', 'shop'], ['japanese', 'restaurant'])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    asyncio.ensure_future(loadModel(future))
    future.add_done_callback(modelLoaded)
    try:
        loop.run_forever()
    finally:
        loop.close()
    app.run(debug=True,host='0.0.0.0')
