from django.db import models
from .User import StudentUser
from .StudentReportRemark import StudentReportRemark

choices = [("Weekly", "Weekly"), ("Monthly", "Monthly"), ("Final", "Final")]

# Module Access
###################
# Student: to submit reports
# Uni Super: to remark n accept / reject
# Comapny: can't access at all

# Relations
###################
# many-to-one
# one-to-many
# one-to-one

# Notifications
###################
# many-to-one
# one-to-many
# one-to-one

# Model Access (Permissions)
###################
# Student: can create, read, update & delete
# Uni Super: can only read
# Comapny: can't access at all

# API Call Result
###################
# {
#   id: 2,
#   title: "Report X",
#   student: {
#               id: 5,
#               name: "Ahmad",
#               type: "Student",
#               .
#               .
#               .
#            },
#   type: "Weekly",
#   startDate: "2022-16-15",
#   endDate: "2022-16-22",
#   intro: "This is the introduction of the report",
#   conclusion: "This is the conclusion of the report",
#   remark: {
#               id: 1,
#               remarks: "Nice work",
#               accepted: True,
#               .
#               .
#               .
#            },
#   skills: [{
#               id: 1,
#               title: "Web App Dev",
#               details: "basics of web app",
#               .
#               .
#               .
#            },
#            {
#               id: 2,
#               title: "Mobile App Dev",
#               details: "basics of mobile app",
#               .
#               .
#               .
#            }],
#   achievements: [{
#               id: 1,
#               title: "First web app stage 1",
#               details: "landing page of my first ever web app",
#               .
#               .
#               .
#            },
#            {
#               id: 2,
#               title: "First web app stage 2",
#               details: "dashboard page of my web app",
#               .
#               .
#               .
#            }],
# }
class StudentReport(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    student = models.ForeignKey(
        StudentUser, related_name="student_idStudentReport", on_delete=models.CASCADE
    )
    type = models.CharField(max_length=256, choices=choices)
    # Start & end of period covered by the report
    startDate = models.DateField()
    endDate = models.DateField()
    # Report intro & conclusion paragraphs
    intro = models.TextField(null=True, blank=True)
    conclusion = models.TextField(null=True, blank=True)
    # Supervisor notes
    remarks = models.ForeignKey(
        StudentReportRemark,
        related_name="report_idStudentReport",
        on_delete=models.CASCADE,
        unique=True,
    )
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class StudentReportSkill(models.Model):
    title = models.CharField(max_length=256)
    report = models.ForeignKey(StudentReport, on_delete=models.CASCADE)
    details = models.TextField(null=True, blank=True)
    # For student profile customization (to decide is this is to include in the profile)
    profile = models.BooleanField(default=True)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class StudentReportAchievement(models.Model):
    title = models.CharField(max_length=256)
    report = models.ForeignKey(StudentReport, on_delete=models.CASCADE)
    details = models.TextField(null=True, blank=True)
    # For student profile customization (to decide is this is to include in the profile)
    profile = models.BooleanField(default=True)
    # Timestamps
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
