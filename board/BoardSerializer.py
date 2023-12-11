from rest_framework import serializers

from board.models import Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ['title', 'content']
        # fields = ['id', 'title', 'nickname_author', 'dt_created', 'dt_modified']

    def create(self, validated_data):
        # 현재 로그인한 사용자를 작성자로 설정
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
