import jinja2 as jinja

from core.defaults import *


## Jinja Environment
jin_temp_location = 'templates'
jin_env = jinja.Environment(loader=jinja.FileSystemLoader(jin_temp_location), lstrip_blocks=True)


## Authentication Headers from environment variables
auth_headers = {
    'ClientAccessKey': ClientAccessKey, 
    'Password': UKGPWD, 
    'UserAccessKey': UserAccessKey,
    'UserName': UKGUID,
}
