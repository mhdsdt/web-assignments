from locust import HttpUser, between, task

class UserBehavior(HttpUser):
    wait_time = between(1, 5)

    @task(1)
    def load_django(self):
        self.client.get("http://django_backend")

    @task(1)
    def load_go(self):
        self.client.get("http://go_backend")
