from .models import Store
from .models import Faq
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
