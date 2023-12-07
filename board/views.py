from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .BoardSerializer import BoardSerializer
from .models import Board


class BoardList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response({'boards': serializer.data}, status=status.HTTP_200_OK)


@permission_classes([permissions.IsAuthenticated])
class BoardDetail(APIView):
    def get(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        serializer = BoardSerializer(board)
        return JsonResponse({'board': serializer.data})

    def post(self, request):
        serializer = BoardSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        self.check_object_permissions(request, board)

        serializer = BoardSerializer(board, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': '글이 성공적으로 수정되었습니다.'})
        return JsonResponse({'error': serializer.errors}, status=400)

    def delete(self, request, pk):
        board = get_object_or_404(Board, pk=pk)
        self.check_object_permissions(request, board)
        board.delete()
        return JsonResponse({'message': '글이 성공적으로 삭제되었습니다.'})