from locust import HttpUser, task, between


class SupervisorUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def run_workflow(self):
        self.client.get(
        "/stream",
        timeout=30
    )