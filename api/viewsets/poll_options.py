from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.models.options_poll import OptionsPoll
from api.serializers.options_poll_serializer import OptionPollSerializer, OptionPollSerializerList
from api.utils import CanChangePoll


class PollOptionsViewSet(viewsets.ModelViewSet):
    queryset = OptionsPoll.objects.all()
    serializer_class = OptionPollSerializer
    permission_classes = (IsAuthenticated, CanChangePoll)

    def get_serializer_class(self):
        if self.action == 'list':
            return OptionPollSerializerList
        return OptionPollSerializer
