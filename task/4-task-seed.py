from task.app.main import run

run(
    deployment_name='gpt-4o',
    seed=42,
    n=5
)

# Check the content in choices. The expected result is that in almost all choices the result will be the same.
# If you restart the app and retry, it should be mostly the same.
# Also, try it without `seed` parameter.
# For Anthropic and Gemini this parameter will be ignored