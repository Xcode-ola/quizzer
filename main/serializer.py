from rest_framework import serializers
from .models import *

#homepage serializer for the website. The page contains all the courses and a link to the contact address
class IndexPageSerializer(serializers.ModelSerializer):
    chapter = serializers.HyperlinkedIdentityField(view_name='chapter',lookup_field = "name")
    quiz = serializers.HyperlinkedIdentityField(view_name='quiz_list',lookup_field = "name")
    theory = serializers.HyperlinkedIdentityField(view_name='practice_list',lookup_field = "name")
    class Meta:
        model = CourseList
        fields = [
            'id',
            'name',
            'chapter',
            'quiz',
            'theory',
        ]

class ChapterSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)

class ChapterListSerializer(serializers.ModelSerializer):
    #summary = serializers.HyperlinkedIdentityField(view_name='main:summary',lookup_field = 'slug',)

    class Meta:
        model = ChapterList
        fields = [
            'id',
            'course',
            'name',
            'slug',
            #'summary',
        ]

class SummaryPageSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(read_only=True)
    class Meta:
        model = Summary
        fields = [
            'id',
            'chapter',
            'body',
        ]

class QuizHomePageSerializer(serializers.ModelSerializer):
    #quiz = serializers.HyperlinkedIdentityField(view_name='quiz_list',lookup_field = "name")

    class Meta:
        model = CourseList
        fields = [
            'id',
            'name',
            #'quiz',
        ]

class CourseSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)

class QuizListSerializer(serializers.ModelSerializer):
    course = ChapterSerializer(read_only=True)
    #quiz = serializers.HyperlinkedIdentityField(view_name='start_quiz',lookup_field = "id",)
    class Meta:
        model = Quiz
        fields = [
            'id',
            'course',
            'name',
            #'quiz',
        ]

class QuestionStemSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionStem
        fields = [
            'que_stem',
            'ans',
        ]

class QuizSerializer(serializers.ModelSerializer):
    answer = QuestionStemSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = [
            'id',
            'question',
            'answer',
        ]

class TheorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeQuestion
        fields = [
            'id',
            'question',
            'answer',
        ]
#practice-list