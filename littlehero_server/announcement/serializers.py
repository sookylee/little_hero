from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Post
        fields = (
            'url',
            'title',
            'address_city',
            'address_gu',
            'address_remainder',
            'recruit_status',
            'adult_status',
            'domain',
            'telephone',
            'do_date',
            'do_time',
            'do_week',
            'recruit_date',
            'recruit_company',
            'recruit_member',
            'text',
        )
        #light_only_fields=(
        # )