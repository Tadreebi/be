from .ComapnyRating import (
    ComapnyRatingSerializer,
)

from .CompanyReport import (
    CompanyReportSerializer,
)

from .InternshipPost import InternshipPostSerializer, InternshipRequirementsSerializer

from .StudentApplication import StudentApplicationSerializer

from .StudentExperience import (
    StudentExperienceSerializer,
)
from .StudentGoal import StudentGoalsSerializer, StudentGoalIndicatorsSerializer
from .StudentProfile import (
    StudentProfileSerializer,
)
from .StudentProposal import (
    StudentprposalSerializer,
    UniProposalResponseSerializer
)

from .StudentReport import (
    StudentReportsSerializer,
    StudentReportSkillsSerializer,
    StudentReportAchievementsSerializer,
)
from .UniversityFeedback import UniversityFeedbackSerializer
from .UniversityTip import UniversityTipsSerializer

from .User import (
    StudentSerializer,
    UniversitySerializer,
    CompanySerializer,
)


from .Faculty import FacultySerializer
from .SupervisedBy import SupervisedBySerializer
from .Token import TokenSerializer

