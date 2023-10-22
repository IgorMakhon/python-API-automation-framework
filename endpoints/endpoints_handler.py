class Endpoint:
    status = None

    def check_status_is_ok(self):
        assert self.status in [200, 201]
