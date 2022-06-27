from .users_views import (
    StudentSignUpView,
    UniversitySignUpView,
    CompanySignUpView,
    StudentSignUpDetail,
    UniversitySignUpDetail,
    CompanySignUpDetail,
)
from .uni_stu_feedback import UniStuFeedbackListView, UniStuFeedbackDetailsView
from .comp_uni_feedback import CompUniFeedbackListView, CompUniFeedbackDetailsView

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
from .StudentProfile import (
    StudentProfileList,
    StudentProfileCreate,
    StudentProfileDetail,
    StudentProfileUpdate,
    StudentProfileDelete,
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
from .StudentExperience import (
    StudentExperienceCreate,
    StudentExperienceDelete,
    StudentExperienceDetail,
    StudentExperienceList,
    StudentExperienceUpdate,
)

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


from .StudentApplications import (
    StudentApplicationsList,
    StudentApplicationsRetrieveUpdateDestroy,
    ApplicationsViewSets,
)
