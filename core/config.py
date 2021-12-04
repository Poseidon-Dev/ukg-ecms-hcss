import jinja2 as jinja

from core.defaults import *

## Jinja Environment
jin_env = jinja.Environment(loader=jinja.FileSystemLoader('templates'), lstrip_blocks=True)

## Authentication Headers from environment variables
auth_headers = {
    'ClientAccessKey': ClientAccessKey, 
    'Password': UKGPWD, 
    'UserAccessKey': UserAccessKey,
    'UserName': UKGUID,
}
