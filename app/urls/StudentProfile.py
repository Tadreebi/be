from app.api.views import (
    StudentProfileList,
    StudentProfileCreate,
    StudentProfileDetail,
    StudentProfileUpdate,
    StudentProfileDelete,
    StudentProfileExperienceList,
    StudentProfileExperienceCreate,
    StudentProfileExperienceDetail,
    StudentProfileExperienceUpdate,
    StudentProfileExperienceDelete,
    StudentProfileSkillList,
    StudentProfileSkillCreate,
    StudentProfileSkillDetail,
    StudentProfileSkillUpdate,
    StudentProfileSkillDelete,
    StudentProfileEducationList,
    StudentProfileEducationCreate,
    StudentProfileEducationDetail,
    StudentProfileEducationUpdate,
    StudentProfileEducationDelete,
    StudentProfileLanguageList,
    StudentProfileLanguageCreate,
    StudentProfileLanguageDetail,
    StudentProfileLanguageUpdate,
    StudentProfileLanguageDelete,
    StudentProfileContactList,
    StudentProfileContactCreate,
    StudentProfileContactDetail,
    StudentProfileContactUpdate,
    StudentProfileContactDelete,
    StudentProfileWorkList,
    StudentProfileWorkCreate,
    StudentProfileWorkDetail,
    StudentProfileWorkUpdate,
    StudentProfileWorkDelete,
)
from django.urls import path

urlpatterns = [
    # Student Profile #########################################################
    path(
        "",
        StudentProfileList.as_view(),
        name="Student Profile List",
    ),
    path(
        "create/",
        StudentProfileCreate.as_view(),
        name="Student Profile Create",
    ),
    path(
        "<int:pk>",
        StudentProfileDetail.as_view(),
        name="Student Profile Details",
    ),
    path(
        "update/<int:pk>",
        StudentProfileUpdate.as_view(),
        name="Student Profile Update",
    ),
    path(
        "delete/<int:pk>",
        StudentProfileDelete.as_view(),
        name="Student Profile Delete",
    ),
    # Student Profile Experiences #########################################################
    path(
        "experiences/",
        StudentProfileExperienceList.as_view(),
        name="Student Profile Experiences List",
    ),
    path(
        "experiences/create/",
        StudentProfileExperienceCreate.as_view(),
        name="Student Profile Experiences Create",
    ),
    path(
        "experiences/<int:pk>",
        StudentProfileExperienceDetail.as_view(),
        name="Student Profile Experiences Details",
    ),
    path(
        "experiences/update/<int:pk>",
        StudentProfileExperienceUpdate.as_view(),
        name="Student Profile Experiences Update",
    ),
    path(
        "experiences/delete/<int:pk>",
        StudentProfileExperienceDelete.as_view(),
        name="Student Profile Experiences Delete",
    ),
    # Student Profile Skills #########################################################
    path(
        "skills/",
        StudentProfileSkillList.as_view(),
        name="Student Profile Skills List",
    ),
    path(
        "skills/create/",
        StudentProfileSkillCreate.as_view(),
        name="Student Profile Skills Create",
    ),
    path(
        "skills/<int:pk>",
        StudentProfileSkillDetail.as_view(),
        name="Student Profile Skills Details",
    ),
    path(
        "skills/update/<int:pk>",
        StudentProfileSkillUpdate.as_view(),
        name="Student Profile Skills Update",
    ),
    path(
        "skills/delete/<int:pk>",
        StudentProfileSkillDelete.as_view(),
        name="Student Profile Skills Delete",
    ),
    # Student Profile Educations #########################################################
    path(
        "educations/",
        StudentProfileEducationList.as_view(),
        name="Student Profile Educations List",
    ),
    path(
        "educations/create/",
        StudentProfileEducationCreate.as_view(),
        name="Student Profile Educations Create",
    ),
    path(
        "educations/<int:pk>",
        StudentProfileEducationDetail.as_view(),
        name="Student Profile Educations Details",
    ),
    path(
        "educations/update/<int:pk>",
        StudentProfileEducationUpdate.as_view(),
        name="Student Profile Educations Update",
    ),
    path(
        "educations/delete/<int:pk>",
        StudentProfileEducationDelete.as_view(),
        name="Student Profile Educations Delete",
    ),
    # Student Profile Languages #########################################################
    path(
        "languages/",
        StudentProfileLanguageList.as_view(),
        name="Student Profile Languages List",
    ),
    path(
        "languages/create/",
        StudentProfileLanguageCreate.as_view(),
        name="Student Profile Languages Create",
    ),
    path(
        "languages/<int:pk>",
        StudentProfileLanguageDetail.as_view(),
        name="Student Profile Languages Details",
    ),
    path(
        "languages/update/<int:pk>",
        StudentProfileLanguageUpdate.as_view(),
        name="Student Profile Languages Update",
    ),
    path(
        "languages/delete/<int:pk>",
        StudentProfileLanguageDelete.as_view(),
        name="Student Profile Languages Delete",
    ),
    # Student Profile Contacts #########################################################
    path(
        "contacts/",
        StudentProfileContactList.as_view(),
        name="Student Profile Contacts List",
    ),
    path(
        "contacts/create/",
        StudentProfileContactCreate.as_view(),
        name="Student Profile Contacts Create",
    ),
    path(
        "contacts/<int:pk>",
        StudentProfileContactDetail.as_view(),
        name="Student Profile Contacts Details",
    ),
    path(
        "contacts/update/<int:pk>",
        StudentProfileContactUpdate.as_view(),
        name="Student Profile Contacts Update",
    ),
    path(
        "contacts/delete/<int:pk>",
        StudentProfileContactDelete.as_view(),
        name="Student Profile Contacts Delete",
    ),
    # Student Profile Works #########################################################
    path(
        "works/",
        StudentProfileWorkList.as_view(),
        name="Student Profile Works List",
    ),
    path(
        "works/create/",
        StudentProfileWorkCreate.as_view(),
        name="Student Profile Works Create",
    ),
    path(
        "works/<int:pk>",
        StudentProfileWorkDetail.as_view(),
        name="Student Profile Works Details",
    ),
    path(
        "works/update/<int:pk>",
        StudentProfileWorkUpdate.as_view(),
        name="Student Profile Works Update",
    ),
    path(
        "works/delete/<int:pk>",
        StudentProfileWorkDelete.as_view(),
        name="Student Profile Works Delete",
    ),
]
