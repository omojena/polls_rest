from rest_framework.permissions import BasePermission

from api.models.polls import Polls

USER = 1
ADMIN = 2
SUPER_ADMIN = 3


def calculate_percentage(votes, total):
    return votes * 100 / total


def valid_vote(user_id, poll_id):
    poll_votes = Polls.objects.get(id=poll_id).user_votes_set.all()
    return bool(user_id in poll_votes)


class CanChangeUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.userType == SUPER_ADMIN)


class CanChangePoll(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and (request.user.userType == SUPER_ADMIN or request.user.userType == ADMIN))
