from .models import Store
from .models import Faq
from rest_framework import serializers


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = [
            "id",
            "store_name",
            "branch",
            "area",
            "tel",
            "address",
            "latitude",
            "longitude",
            "category_list",
        ]

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = [
            "faq_no",
            # "faq_group_no",
            # "faq_group_order",
            # "faq_depth",
            "faq_title",
            "faq_content",
            "faq_writer",
            "faq_write_date",
            "faq_count",
        ]