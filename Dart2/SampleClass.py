authUsername = 'my_user_name'
authPassword = 'my_password'
apiEndpoint = 'https://postman-echo.com/'


class HttpConstants:
    def __init__(self):
        self.authUsername = 'my_user_name'
        self.authPassword = 'my_password'
        self.apiEndpoint = 'https://postman-echo.com/'

    def authUsername(self):
        return self.authUsername

    def authPassword(self):
        return self.authPassword

    def apiEndpoint(self):
        return self.apiEndpoint
