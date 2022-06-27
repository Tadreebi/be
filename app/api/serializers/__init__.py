from .users_serializers import (
    StudentSerializer,
    UniversitySerializer,
    CompanySerializer,
)
from .uni_stu_feedback import UniStuFeedback
from .comp_uni_feedback import CompUniFeedback

from .StudentReports import (
    StudentReportsSerializer,
    StudentReportSkillsSerializer,
    StudentReportAchievementsSerializer,
)
from .StudentProfile import (
    StudentProfileSerializer,
)

from .UniversityTips import UniversityTipsSerializer
from .StudentGoals import StudentGoalsSerializer, StudentGoalIndicatorsSerializer
from .StudentExperience import (
    StudentExperienceSerializer,
)

from .ComapnyRating import (
    ComapnyRatingSerializer,
)

from .CompanyReport import (
    CompanyReportSerializer,
)

from .InternshipPost import InternshipPostSerializer, InternshipRequirementsSerializer
from .StudentApplications import StudentApplicationSerializer
