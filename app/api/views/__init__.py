from .ComapnyRating import (
    ComapnyRatingList,
    ComapnyRatingCreate,
    ComapnyRatingDetail,
    ComapnyRatingUpdate,
    ComapnyRatingDelete,
)
from .comp_uni_feedback import CompUniFeedbackListView, CompUniFeedbackDetailsView

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


from .StudentApplications import (
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
from .StudentGoals import (
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

from .StudentReports import (
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
from .uni_stu_feedback import UniStuFeedbackListView, UniStuFeedbackDetailsView

from .UniversityTips import (
    UniversityTipsList,
    UniversityTipsCreate,
    UniversityTipsDetail,
    UniversityTipsUpdate,
    UniversityTipsDelete,
)
from .Users import (
    StudentSignUpView,
    UniversitySignUpView,
    CompanySignUpView,
    StudentSignUpDetail,
    UniversitySignUpDetail,
    CompanySignUpDetail,
)
