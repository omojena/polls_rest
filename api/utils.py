from rest_framework import status
from rest_framework.permissions import BasePermission
from rest_framework.response import Response

from api.models.polls import Polls

USER = 1
ADMIN = 2
SUPER_ADMIN = 3


def calculate_percentage(votes, total):
    return votes * 100 / total


def valid_vote(user, poll_id):
    try:
        poll = Polls.objects.get(id=poll_id)
        votes_list = poll.user_votes.all()
        return bool(user in votes_list)
    except Polls.DoesNotExist as e:
        return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CanChangeUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.userType == SUPER_ADMIN)


class CanChangePoll(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and (request.user.userType == SUPER_ADMIN or request.user.userType == ADMIN))
