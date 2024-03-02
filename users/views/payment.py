from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated

from users.models import Payment
from users.serializers.payment import PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['payment_date']
    search_fields = ['course_title', 'lesson_title', 'payment_method']
    permission_classes = [IsAuthenticated]
