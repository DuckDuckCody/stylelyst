class UserSettings:
    def __init__(self):
        self.websites = [2]
        self.gender = 1
        self.category = 1
        self.current_page = 1

    def save_settings(self, settings):
        self.websites = settings.get('websites')
        self.gender = settings.get('gender')
        self.category = settings.get('category')
