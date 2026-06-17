from app.utils.retry import retry


@retry()
def failing_function():

    raise Exception("Temporary Failure")


failing_function()