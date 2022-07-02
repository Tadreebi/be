from .ComapnyRating import (
    ComapnyRatingList,
    ComapnyRatingCreate,
    ComapnyRatingDetail,
    ComapnyRatingUpdate,
    ComapnyRatingDelete,
)

from .CompanyReport import (
    CompanyReportList,
    CompanyReportCreate,
    CompanyReportDetail,
    CompanyReportUpdate,
    CompanyReportDelete,
)
from .InternshipPost import (
    InternshipPostList,
    InternshipPostRetrieveUpdateDestroy,
    InternshipPostsViewSets,
    InternshipPostRequirementsList,
    InternshipPostRequirementsRetrieveUpdateDestroy,
    InternshipPostRequirementsViewSets,
)


from .StudentApplication import (
    StudentApplicationsList,
    StudentApplicationsRetrieveUpdateDestroy,
    ApplicationsViewSets,
)
from .StudentExperience import (
    StudentExperienceCreate,
    StudentExperienceDelete,
    StudentExperienceDetail,
    StudentExperienceList,
    StudentExperienceUpdate,
)
from .StudentGoal import (
    StudentGoalsList,
    StudentGoalsCreate,
    StudentGoalsDetail,
    StudentGoalsUpdate,
    StudentGoalsDelete,
    StudentGoalIndicatorsList,
    StudentGoalIndicatorsCreate,
    StudentGoalIndicatorsDetail,
    StudentGoalIndicatorsUpdate,
    StudentGoalIndicatorsDelete,
)
from .StudentProfile import (
    StudentProfileList,
    StudentProfileCreate,
    StudentProfileDetail,
    StudentProfileUpdate,
    StudentProfileDelete,
)
from .StudentProposal import (
    Proposal_List_View,
    proposal_create,
    proposal_detail_view,
    proposal_Update,
    proposal_delete,
)

from .StudentReport import (
    StudentReportsList,
    StudentReportsCreate,
    StudentReportsDetail,
    StudentReportsUpdate,
    StudentReportsDelete,
    StudentReportSkillsList,
    StudentReportSkillsCreate,
    StudentReportSkillsDetail,
    StudentReportSkillsUpdate,
    StudentReportSkillsDelete,
    StudentReportAchievementsList,
    StudentReportAchievementsCreate,
    StudentReportAchievementsDetail,
    StudentReportAchievementsUpdate,
    StudentReportAchievementsDelete,
)
from .UniversityFeedback import (
    UniversityFeedbackListView,
    UniversityFeedbackDetailsView,
)

from .UniversityTip import (
    UniversityTipsList,
    UniversityTipsCreate,
    UniversityTipsDetail,
    UniversityTipsUpdate,
    UniversityTipsDelete,
)
from .User import (
    StudentSignUpView,
    UniversitySignUpView,
    CompanySignUpView,
    StudentSignUpDetail,
    UniversitySignUpDetail,
    CompanySignUpDetail,
)

from .Token import TokenView
