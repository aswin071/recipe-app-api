# recipe-app-api




Git Hub Actions :
Automation tools for continuously auto up[date changes

TDD with Django::
 Django test is built on top of Unit Testing library(pytthon)
 DJango adds features like:
    *Test-client dummy web browser--it allows to send test requests to the django backend
    *simulate authentication
    *Temporary Database'
 DRF:
    *Test APIClient -->its a class provided by the DRF
Common Test classes provided by DRF:
    -->SimpeTestCase=NO DB integration so that it will use for,if there is no DB actions required
    -->TestCase =  Allows DB integration

Mocking:
Override or change the behaviour of dependencies  for the purpose of testing.
Avoid unintended side effects
Isolate the code being tested

How to mock code :
*Use unittest.mock
   { Magicmock /Mock
    patch }
*Always start with test_ when writing a test

DB Race condition:
*Make Django "wait for db"
    -Check for database availability
    -Continue when database ready
*Create Custom Django command


Custom User Model
*AbstarctUserModel and PermmissionMixin


------------------API Documentation---------------------------
what to documet?
*Everything needed to use the API
*Available Endpoints (paths)
*SUpport methods
*Formate of playloads
    -parameter
    -Post on JSON format
*Formate of response
    -JSON
AUthentication Process

Options for documentation
*Manaul
    *Word doc
    *Markdown
*Automated
    -Use metadata from code (comments)
    -Generate documentation pages

AUtomated API documentation with DRF
*   Auto generate docs
    -drf-spectacular (library for use in auto-generate API)


Build User API:
*User Registration
*Creating auth token
*Viewing/updating profile
