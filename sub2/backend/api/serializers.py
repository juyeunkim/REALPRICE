from rest_framework import serializers
from .models import *

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

class StoreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreDetail
        fields = [
            "id",
            "store",
            "store_name",
            "address",
            "img_src",
            "tag",
            "char",
        ]       
class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = [
            "faq_no",
            "faq_category",
            "faq_title",
            "faq_content",
            "faq_writer",
            "faq_write_date",
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
        ]

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",      
            "store",   
            "user",    
            "score",   
            "content", 
            "reg_time",
        ]

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = [
            "history_no",
            "time",
            "expenditure",
            "user",
            "store"
        ]

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = [
            "id",      
            "store",   
            "menu_name",    
            "price"
        ]


from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('gender', 'born_year', 'name', 'address', 'phone', 'tag','photo')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)
    # url = serializers.HyperlinkedIdentityField(view_name="api:user-detail") 안먹힘
    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password) #hash로 저장된다고 함
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.gender = profile_data.get('gender', profile.gender)
        profile.born_year = profile_data.get('born_year', profile.born_year)
        profile.name = profile_data.get('name', profile.name)
        profile.address = profile_data.get('address', profile.address)
        profile.phone = profile_data.get('phone', profile.phone)
        profile.tag = profile_data.get('tag', profile.tag)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.save()

        return instance
