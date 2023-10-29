class Endpoint:
    status = None
    id = None

    def check_status_is_ok(self):
        print("status:", self.status)
        assert self.status in [200, 201]

    def check_id_is_int_type(self):
        print("id", self.id)
        assert isinstance(self.id, int)
