from task.app.main import run

run(
    deployment_name='gpt-4o',
    print_only_content=True,
    # presence_penalty=-2.0,
    # presence_penalty=1.5,
    presence_penalty=2.0,
)

# In the final result, we can see that the higher `presence_penalty` (2.0) the more LLM is trying to add topics that
# somehow related to the main topic.
# For Anthropic and Gemini this parameter will be ignored