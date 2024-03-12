from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


from pirate_speak.chain import chain as pirate_speak_chain

add_routes(
    app,
    pirate_speak_chain,
    path="/pirate-speak",
    playground_type="chat",
    enable_feedback_endpoint=True,
    enable_public_trace_link_endpoint=True
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
