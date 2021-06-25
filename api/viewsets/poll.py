from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models.options_poll import OptionsPoll
from api.models.polls import Polls
from api.serializers.poll_serializer import PollSerializer, PollSerializerList
from api.utils import calculate_percentage, CanChangePoll, valid_vote


class PollViewSet(viewsets.ModelViewSet):
    queryset = Polls.objects.all()
    serializer_class = PollSerializer
    permission_classes = (IsAuthenticated, CanChangePoll)

    def get_serializer_class(self):
        if self.action == 'list':
            return PollSerializerList
        return PollSerializer


class ChangeIsActive(APIView):
    permission_classes = (IsAuthenticated, CanChangePoll)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            poll_id = data.get('id')
            poll = Polls.objects.get(id=poll_id)
            value = not poll.is_active
            poll.is_active = value
            poll.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Poll updated successfully',
                'data': []
            }
            return Response(response)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VotePoll(APIView):

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            poll_id = data.get('id')
            if valid_vote(request.user, poll_id):
                return Response({"message": "User already voted in this poll"}, status=status.HTTP_406_NOT_ACCEPTABLE)
            option_id = data.get('option')
            poll = Polls.objects.get(id=poll_id)
            poll.total_votes = poll.total_votes + 1
            poll.user_votes.add(request.user)
            options = OptionsPoll.objects.filter(fk_poll=poll_id)
            poll.save()
            for item in options:
                if item.id == option_id:
                    item.total_votes = item.total_votes + 1
                item.percentage = calculate_percentage(item.total_votes, poll.total_votes)
                item.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Vote successfully',
                'data': []
            }
            return Response(response)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
