import time


def retry(max_retries=3, backoff_factor=2):

    def decorator(func):

        def wrapper(*args, **kwargs):

            for attempt in range(max_retries):

                try:
                    return func(*args, **kwargs)

                except Exception as e:

                    if attempt == max_retries - 1:
                        raise e

                    wait_time = backoff_factor ** attempt

                    time.sleep(wait_time)

        return wrapper

    return decorator
