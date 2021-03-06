from .StudentAppResponse import (
    ApplicationResponseCreate,
    ApplicationResponseDelete,
    ApplicationResponseDetail,
    ApplicationResponseList,
    ApplicationResponseUpdate,
)

from .CompanyRating import (
    CompanyRatingCreate,
    CompanyRatingDelete,
    CompanyRatingDetail,
    CompanyRatingList,
    CompanyRatingUpdate,
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
    InternshipPostCreate,
    InternshipPostDetail,
    InternshipPostUpdate,
    InternshipPostDelete,
    InternshipPostsViewSets,
)


from .StudentApplication import (
    StudentApplicationList,
    StudentApplicationCreate,
    StudentApplicationDetail,
    StudentApplicationUpdate,
    StudentApplicationDelete,
    StudentApplicationResponseList,
    StudentApplicationResponseCreate,
    StudentApplicationResponseDetail,
    StudentApplicationResponseUpdate,
    StudentApplicationResponseDelete,
    # ApplicationsViewSets
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
    StudentReportTypesList,
    StudentReportTypesCreate,
    StudentReportTypesDetail,
    StudentReportTypesUpdate,
    StudentReportTypesDelete,
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
    StudentReportRemarksList,
    StudentReportRemarksCreate,
    StudentReportRemarksDetail,
    StudentReportRemarksUpdate,
    StudentReportRemarksDelete,
)
from .UniversityFeedback import (
    UniversityFeedbackList,
    UniversityFeedbackCreate,
    UniversityFeedbackDetail,
    UniversityFeedbackUpdate,
    UniversityFeedbackDelete,
)

from .UniversityTip import (
    UniversityTipsList,
    UniversityTipsCreate,
    UniversityTipsDetail,
    UniversityTipsUpdate,
    UniversityTipsDelete,
    UniversityTipTopicsList,
    UniversityTipTopicsCreate,
    UniversityTipTopicsDetail,
    UniversityTipTopicsUpdate,
    UniversityTipTopicsDelete,
)
from .User import (
    StudentSignUpView,
    UniversitySignUpView,
    CompanySignUpView,
    StudentSignUpDetail,
    UniversitySignUpDetail,
    CompanySignUpDetail,
)


from .Faculty import (
    FacultyListView,
    FacultyDetailsView,
)

from .SupervisedBy import (
    SupervisedByListView,
    SupervisedByDetailsView,
)

from .Cities import (
    CitiesCreate,
    CitiesDetail,
    CitiesList,
    CitiesUpdate,
    CitiesDelete,
)

from .UniproposalResponse import (
    UniResponse_create,
    UniResponse_delete,
    UniResponse_detail_view,
    UniResponse_List_View,
    UniResponse_Update,
)
from .Token import TokenView

from .Token import TokenView
from .logout import logout_view
