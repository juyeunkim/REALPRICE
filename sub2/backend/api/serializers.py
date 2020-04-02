from .models import Store
from .models import Qna
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


class QnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qna
        fields = [
            "qna_no",
            "qna_group_no",
            "qna_group_order",
            "qna_depth",
            "qna_title",
            "qna_content",
            "qna_writer",
            "qna_write_date",
            "qna_count",
        ]
