class Response:

    def __init__(self, response):
        self.response = response
        self.response_status_code = response.status_code
        self.response_json = response.json()

    def validate(self, model):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                model(**item)
        else:
            model(**self.response_json)
        return self

    def assert_status_code(self, status_code: int):
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, self
        else:
            assert self.response_status_code == status_code, self
        return self

    def __str__(self):
        return \
            f"\nStatus code: {self.response_status_code}\n" \
            f"Request url: {self.response.url}\n" \
            f"Response body: {self.response_json}"
