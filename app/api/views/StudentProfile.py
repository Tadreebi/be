from app.models import (
    StudentProfile,
    StudentProfileExperience,
    StudentProfileSkill,
    StudentProfileEducation,
    StudentProfileLanguage,
    StudentProfileContact,
    StudentProfileWork,
)
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
)

from app.api.serializers import (
    StudentProfileSerializer,
    StudentProfileExperiencesSerializer,
    StudentProfileSkillsSerializer,
    StudentProfileEducationsSerializer,
    StudentProfileLanguagesSerializer,
    StudentProfileContactsSerializer,
    StudentProfileWorksSerializer,
)

from app.api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions


# Student Profile #########################################################
class StudentProfileList(ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileCreate(ListCreateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileDetail(RetrieveAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileUpdate(RetrieveUpdateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileDelete(RetrieveDestroyAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

    permission_classes = [permissions.IsAuthenticated]


# Student Profile Experience #########################################################
class StudentProfileExperienceList(ListAPIView):
    queryset = StudentProfileExperience.objects.all()
    serializer_class = StudentProfileExperiencesSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileExperienceCreate(ListCreateAPIView):
    queryset = StudentProfileExperience.objects.all()
    serializer_class = StudentProfileExperiencesSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileExperienceDetail(RetrieveAPIView):
    queryset = StudentProfileExperience.objects.all()
    serializer_class = StudentProfileExperiencesSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileExperienceUpdate(RetrieveUpdateAPIView):
    queryset = StudentProfileExperience.objects.all()
    serializer_class = StudentProfileExperiencesSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileExperienceDelete(RetrieveDestroyAPIView):
    queryset = StudentProfileExperience.objects.all()
    serializer_class = StudentProfileExperiencesSerializer

    permission_classes = [permissions.IsAuthenticated]


# Student Profile Skills #########################################################
class StudentProfileSkillList(ListAPIView):
    queryset = StudentProfileSkill.objects.all()
    serializer_class = StudentProfileSkillsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileSkillCreate(ListCreateAPIView):
    queryset = StudentProfileSkill.objects.all()
    serializer_class = StudentProfileSkillsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileSkillDetail(RetrieveAPIView):
    queryset = StudentProfileSkill.objects.all()
    serializer_class = StudentProfileSkillsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileSkillUpdate(RetrieveUpdateAPIView):
    queryset = StudentProfileSkill.objects.all()
    serializer_class = StudentProfileSkillsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileSkillDelete(RetrieveDestroyAPIView):
    queryset = StudentProfileSkill.objects.all()
    serializer_class = StudentProfileSkillsSerializer

    permission_classes = [permissions.IsAuthenticated]


# Student Profile Educations #########################################################
class StudentProfileEducationList(ListAPIView):
    queryset = StudentProfileEducation.objects.all()
    serializer_class = StudentProfileEducationsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileEducationCreate(ListCreateAPIView):
    queryset = StudentProfileEducation.objects.all()
    serializer_class = StudentProfileEducationsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileEducationDetail(RetrieveAPIView):
    queryset = StudentProfileEducation.objects.all()
    serializer_class = StudentProfileEducationsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileEducationUpdate(RetrieveUpdateAPIView):
    queryset = StudentProfileEducation.objects.all()
    serializer_class = StudentProfileEducationsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileEducationDelete(RetrieveDestroyAPIView):
    queryset = StudentProfileEducation.objects.all()
    serializer_class = StudentProfileEducationsSerializer

    permission_classes = [permissions.IsAuthenticated]


# Student Profile Languages #########################################################
class StudentProfileLanguageList(ListAPIView):
    queryset = StudentProfileLanguage.objects.all()
    serializer_class = StudentProfileLanguagesSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileLanguageCreate(ListCreateAPIView):
    queryset = StudentProfileLanguage.objects.all()
    serializer_class = StudentProfileLanguagesSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileLanguageDetail(RetrieveAPIView):
    queryset = StudentProfileLanguage.objects.all()
    serializer_class = StudentProfileLanguagesSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileLanguageUpdate(RetrieveUpdateAPIView):
    queryset = StudentProfileLanguage.objects.all()
    serializer_class = StudentProfileLanguagesSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileLanguageDelete(RetrieveDestroyAPIView):
    queryset = StudentProfileLanguage.objects.all()
    serializer_class = StudentProfileLanguagesSerializer

    permission_classes = [permissions.IsAuthenticated]


# Student Profile Contacts #########################################################
class StudentProfileContactList(ListAPIView):
    queryset = StudentProfileContact.objects.all()
    serializer_class = StudentProfileContactsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileContactCreate(ListCreateAPIView):
    queryset = StudentProfileContact.objects.all()
    serializer_class = StudentProfileContactsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileContactDetail(RetrieveAPIView):
    queryset = StudentProfileContact.objects.all()
    serializer_class = StudentProfileContactsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileContactUpdate(RetrieveUpdateAPIView):
    queryset = StudentProfileContact.objects.all()
    serializer_class = StudentProfileContactsSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileContactDelete(RetrieveDestroyAPIView):
    queryset = StudentProfileContact.objects.all()
    serializer_class = StudentProfileContactsSerializer

    permission_classes = [permissions.IsAuthenticated]


# Student Profile Works #########################################################
class StudentProfileWorkList(ListAPIView):
    queryset = StudentProfileWork.objects.all()
    serializer_class = StudentProfileWorksSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileWorkCreate(ListCreateAPIView):
    queryset = StudentProfileWork.objects.all()
    serializer_class = StudentProfileWorksSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileWorkDetail(RetrieveAPIView):
    queryset = StudentProfileWork.objects.all()
    serializer_class = StudentProfileWorksSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileWorkUpdate(RetrieveUpdateAPIView):
    queryset = StudentProfileWork.objects.all()
    serializer_class = StudentProfileWorksSerializer

    permission_classes = [permissions.IsAuthenticated]


class StudentProfileWorkDelete(RetrieveDestroyAPIView):
    queryset = StudentProfileWork.objects.all()
    serializer_class = StudentProfileWorksSerializer

    permission_classes = [permissions.IsAuthenticated]
