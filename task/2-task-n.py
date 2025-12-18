from task.app.main import run

# Models to try:
# - gpt-4o
# - claude-3-7-sonnet@20250219
# - gemini-2.5-pro

run(
    # deployment_name='gemini-2.5-pro',
    deployment_name='gpt-4o',
    # n=1,
    # n=3,
    n=5
)

# Pay attention to the number of choices in the response!
# If you have worked with ChatGPT, you have probably seen responses where ChatGPT offers you a choice between two
# responses to select which one you prefer. This is done with the `n` parameter.
