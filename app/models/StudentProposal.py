from pickle import FALSE
from .User import StudentUser, CompanyUser, UniversityEmployeeUser, AppUser
from .StudentApplication import StudentApplication
from django.db import models


class StudentUniProposal(models.Model):
    student = models.ForeignKey(
        StudentUser,
        on_delete=models.CASCADE,
        related_name="student_idStudentUniProposal",
        default=1,
    )
    company = models.ForeignKey(
        CompanyUser,
        on_delete=models.CASCADE,
        related_name="company_idStudentUniProposal",
        default=1,
    )
    internship_application = models.ForeignKey(
        StudentApplication,
        on_delete=models.CASCADE,
        related_name="post_idStudentUniProposal",
        default=1,
    )  # Double check of default neccssaty
    # Uni Supervisor notes

    # Timestamps
    remarks = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )

    def __str__(self):
        return str(self.id)


class UniProposalResponse(models.Model):
    proposal = models.OneToOneField(
        StudentUniProposal, on_delete=models.CASCADE, unique=True
    )
    remarks = models.TextField(null=True, blank=True)
    accepted = models.BooleanField(default=False)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.proposal.student.username} proposal"
