from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def load_django(self):
        self.client.get("/api/?n=2&k=4")
