from task.app.main import run

run(
    deployment_name='gpt-4o',
    max_tokens=10
)

# Previously, we have seen that the `finish_reason` in choice was `stop`, but now it is `length`, and if you check the
# `content,` it is clearly unfinished.