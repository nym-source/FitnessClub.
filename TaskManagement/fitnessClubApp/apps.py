from django.apps import AppConfig


class FitnessclubappConfig(AppConfig):
    name = 'fitnessClubApp'
    def ready(self):
        import fitnessClubApp.mysignal
