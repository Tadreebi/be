from .CompanyRating import (
    CompanyRatingSerializer,
)

from .CompanyReport import (
    CompanyReportSerializer,
)

from .InternshipPost import InternshipPostSerializer
from .StudentApplication import StudentApplicationSerializer,StudentApplicationResponseSerializer

from .StudentExperience import (
    StudentExperienceSerializer,
)
from .StudentGoal import StudentGoalsSerializer, StudentGoalIndicatorsSerializer
from .StudentProfile import (
    StudentProfileSerializer,
    StudentProfileExperiencesSerializer,
    StudentProfileSkillsSerializer,
    StudentProfileEducationsSerializer,
    StudentProfileLanguagesSerializer,
    StudentProfileContactsSerializer,
    StudentProfileWorksSerializer,
)
from .StudentProposal import (
    StudentprposalSerializer,
    UniProposalResponseSerializer
)

from .StudentReport import (
    StudentReportsSerializer,
    StudentReportSkillsSerializer,
    StudentReportAchievementsSerializer,
    StudentReportRemarksSerializer,
)
from .UniversityFeedback import UniversityFeedbackSerializer
from .UniversityTip import UniversityTipsSerializer, UniversityTipTopicsSerializer

from .User import (
    StudentSerializer,
    UniversitySerializer,
    CompanySerializer,
)


from .Faculty import FacultySerializer
from .SupervisedBy import SupervisedBySerializer
from .Token import TokenSerializer
