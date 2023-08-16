from SeleniumLibrary import SeleniumLibrary
from robot.api.deco import library
from robotlibcore import DynamicCore

from UserTeamsLibrary.keywords.browser import Browser
from UserTeamsLibrary.keywords.loginpage import LoginPage
from UserTeamsLibrary.keywords.openpage import OpenPage
from UserTeamsLibrary.keywords.selectteam import SelectTeam
from UserTeamsLibrary.keywords.teamdetails import TeamDetails
from UserTeamsLibrary.keywords.userteamseditor import UserTeamsEditor
from UserTeamsLibrary.keywords.assignagenttoteam import AssignAgenttoTeam
from UserTeamsLibrary.keywords.removeagenttoteam import RemoveAgenttoTeam


@library(scope='GLOBAL')
class UserTeamsLibrary(DynamicCore):
    
    def __init__(self): 
        ctx = SeleniumLibrary(timeout="30s", screenshot_root_directory="EMBED")
        components = [
            Browser(ctx=ctx),
            LoginPage(ctx=ctx),
            OpenPage(ctx=ctx),
            SelectTeam(ctx=ctx), 
            TeamDetails(ctx=ctx), 
            UserTeamsEditor(ctx=ctx),
            AssignAgenttoTeam(ctx=ctx),
            RemoveAgenttoTeam(ctx=ctx)

        ]
        DynamicCore.__init__(self,library_components=components)