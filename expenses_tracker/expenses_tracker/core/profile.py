from expenses_tracker.profiles.models import Profile


def get_profile():
    return Profile.objects.first()
