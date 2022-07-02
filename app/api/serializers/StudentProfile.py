from rest_framework import serializers
from app.models import (
    StudentProfile,
    StudentProfileExperience,
    StudentProfileSkill,
    StudentProfileEducation,
    StudentProfileLanguage,
    StudentProfileContact,
    StudentProfileWork,
)


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = "__all__"


class StudentProfileExperiencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfileExperience
        fields = "__all__"


class StudentProfileSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfileSkill
        fields = "__all__"


class StudentProfileEducationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfileEducation
        fields = "__all__"


class StudentProfileLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfileLanguage
        fields = "__all__"


class StudentProfileContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfileContact
        fields = "__all__"


class StudentProfileWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfileWork
        fields = "__all__"
