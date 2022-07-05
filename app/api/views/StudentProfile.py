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

from ..permissions import IsOwnerOrReadOnly, StudentPermission
from rest_framework import generics, permissions


# Student Profile #########################################################
class StudentProfileList(ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

    permission_classes = [permissions.AllowAny]


class StudentProfileCreate(ListCreateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileDetail(RetrieveAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileUpdate(RetrieveUpdateAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileDelete(RetrieveDestroyAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


# Student Profile Experience #########################################################
class StudentProfileExperienceList(ListAPIView):
    queryset = StudentProfileExperience.objects.all()
    serializer_class = StudentProfileExperiencesSerializer
    permission_classes = [permissions.AllowAny]


class StudentProfileExperienceCreate(ListCreateAPIView):
    queryset = StudentProfileExperience.objects.all()
    serializer_class = StudentProfileExperiencesSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileExperienceDetail(RetrieveAPIView):
    queryset = StudentProfileExperience.objects.all()
    serializer_class = StudentProfileExperiencesSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileExperienceUpdate(RetrieveUpdateAPIView):
    queryset = StudentProfileExperience.objects.all()
    serializer_class = StudentProfileExperiencesSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileExperienceDelete(RetrieveDestroyAPIView):
    queryset = StudentProfileExperience.objects.all()
    serializer_class = StudentProfileExperiencesSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


# Student Profile Skills #########################################################
class StudentProfileSkillList(ListAPIView):
    queryset = StudentProfileSkill.objects.all()
    serializer_class = StudentProfileSkillsSerializer
    permission_classes = [permissions.AllowAny]


class StudentProfileSkillCreate(ListCreateAPIView):
    queryset = StudentProfileSkill.objects.all()
    serializer_class = StudentProfileSkillsSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileSkillDetail(RetrieveAPIView):
    queryset = StudentProfileSkill.objects.all()
    serializer_class = StudentProfileSkillsSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileSkillUpdate(RetrieveUpdateAPIView):
    queryset = StudentProfileSkill.objects.all()
    serializer_class = StudentProfileSkillsSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileSkillDelete(RetrieveDestroyAPIView):
    queryset = StudentProfileSkill.objects.all()
    serializer_class = StudentProfileSkillsSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


# Student Profile Educations #########################################################
class StudentProfileEducationList(ListAPIView):
    queryset = StudentProfileEducation.objects.all()
    serializer_class = StudentProfileEducationsSerializer
    permission_classes = [permissions.AllowAny]


class StudentProfileEducationCreate(ListCreateAPIView):
    queryset = StudentProfileEducation.objects.all()
    serializer_class = StudentProfileEducationsSerializer

    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileEducationDetail(RetrieveAPIView):
    queryset = StudentProfileEducation.objects.all()
    serializer_class = StudentProfileEducationsSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileEducationUpdate(RetrieveUpdateAPIView):
    queryset = StudentProfileEducation.objects.all()
    serializer_class = StudentProfileEducationsSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileEducationDelete(RetrieveDestroyAPIView):
    queryset = StudentProfileEducation.objects.all()
    serializer_class = StudentProfileEducationsSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


# Student Profile Languages #########################################################
class StudentProfileLanguageList(ListAPIView):
    queryset = StudentProfileLanguage.objects.all()
    serializer_class = StudentProfileLanguagesSerializer
    permission_classes = [permissions.AllowAny]


class StudentProfileLanguageCreate(ListCreateAPIView):
    queryset = StudentProfileLanguage.objects.all()
    serializer_class = StudentProfileLanguagesSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileLanguageDetail(RetrieveAPIView):
    queryset = StudentProfileLanguage.objects.all()
    serializer_class = StudentProfileLanguagesSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileLanguageUpdate(RetrieveUpdateAPIView):
    queryset = StudentProfileLanguage.objects.all()
    serializer_class = StudentProfileLanguagesSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileLanguageDelete(RetrieveDestroyAPIView):
    queryset = StudentProfileLanguage.objects.all()
    serializer_class = StudentProfileLanguagesSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


# Student Profile Contacts #########################################################
class StudentProfileContactList(ListAPIView):
    queryset = StudentProfileContact.objects.all()
    serializer_class = StudentProfileContactsSerializer
    permission_classes = [permissions.AllowAny]


class StudentProfileContactCreate(ListCreateAPIView):
    queryset = StudentProfileContact.objects.all()
    serializer_class = StudentProfileContactsSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileContactDetail(RetrieveAPIView):
    queryset = StudentProfileContact.objects.all()
    serializer_class = StudentProfileContactsSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileContactUpdate(RetrieveUpdateAPIView):
    queryset = StudentProfileContact.objects.all()
    serializer_class = StudentProfileContactsSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileContactDelete(RetrieveDestroyAPIView):
    queryset = StudentProfileContact.objects.all()
    serializer_class = StudentProfileContactsSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


# Student Profile Works #########################################################
class StudentProfileWorkList(ListAPIView):
    queryset = StudentProfileWork.objects.all()
    serializer_class = StudentProfileWorksSerializer
    permission_classes = [permissions.AllowAny]


class StudentProfileWorkCreate(ListCreateAPIView):
    queryset = StudentProfileWork.objects.all()
    serializer_class = StudentProfileWorksSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileWorkDetail(RetrieveAPIView):
    queryset = StudentProfileWork.objects.all()
    serializer_class = StudentProfileWorksSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileWorkUpdate(RetrieveUpdateAPIView):
    queryset = StudentProfileWork.objects.all()
    serializer_class = StudentProfileWorksSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class StudentProfileWorkDelete(RetrieveDestroyAPIView):
    queryset = StudentProfileWork.objects.all()
    serializer_class = StudentProfileWorksSerializer
    
    # permission_classes = [IsOwnerOrReadOnly, StudentPermission]
    permission_classes = [permissions.AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)
