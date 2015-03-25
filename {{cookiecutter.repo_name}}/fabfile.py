# -*- encoding: utf-8 -*-

from fabric.context_managers import cd
from fabric.contrib.console import confirm
from fabric.operations import prompt
from fabric.state import env

from fabric.utils import abort
from fabric.contrib.files import exists


# Import fabric settings
from project.fabutils.utils import GitControl, ConsolePrinter, LinuxServer, PythonEnv

try:
    from project.settings.fabric import *
except IOError, e:
    abort('Unable to import settings')


###############
# Set fabric environment
###############

def prod_env():
    env.host_string = PROD_HOST
    env.port = PROD_SSH_PORT

    # your user on that system
    env.user = PROD_SSH_USER


def dev_env():
    env.host_string = DEV_HOST
    env.port = DEV_SSH_PORT

    # your user on that system
    env.user = DEV_SSH_USER

# Assumes that your *.pem key is in the same directory as your fabfile.py
env.key_filename = CERTIFICATE_FILE

env.use_ssh_config = True


###############
# End of Settings
###############

git = GitControl()
printer = ConsolePrinter()
server = LinuxServer()
virtualenv = PythonEnv()

##############################
# Internal functions
##############################

from fabric.operations import run


def _update_django_project(project_root_dir, upgrade_requirements):
    """ Updates the remote django project.
    """

    # Přejdeme do root složky projektu (obsahuje requirements.txt, materiály apod.)
    with cd(project_root_dir):
        git.pull()
        printer.succcess("Git repository updated")

        virtualenv.install_pip_requirements(upgrade_requirements)
        printer.succcess("Requirements installed")

        if exists(project_root_dir + '/cron'):
            printer.notice('Fixing cron permissions')
            run('chmod 775 cron/')
            printer.succcess("Permission fixed")

        printer.notice('Deleting pyc files')
        server.delete_pyc_files()
        printer.succcess("PYC files deleted")

        # Přejdeme do django složky projektu, která obsahuje manage.py
        with cd(project_root_dir + "/project"):
            virtualenv.update_database()

            printer.succcess("Database updated")

            virtualenv.run_command_in_virtualenv(
                'python manage.py collectstatic --noinput')
            # virtualenv.run_command_in_virtualenv(
            #    'python manage.py clear_cache')
            virtualenv.run_command_in_virtualenv(
                'python manage.py cleanup')

            printer.notice('Fixing static and media permissions')
            run('chmod 777 static/')
            run('chmod 777 media/')

            printer.succcess("Static and media permissions fixed")

        with cd(project_root_dir + u"/project/project"):
            server.touch_wsgi()
            printer.succcess("WSGI touched")


def _run_deployment_guide(no_questions=False):
    """
    Deploy Django Project.
    """

    if no_questions:
        printer.notice(u'Welcome in automatic deployment guide')
        update_requirements = False
    else:
        printer.notice(u'Welcome in deployment guide')

        if confirm(u'Commit and push GIT?', default=False):
            printer.notice(u'Building GIT commit')
            commit()

        update_requirements = confirm(u'Update PIP requirements?', default=False)

    printer.notice(u'Updating Django project')
    _update_django_project(env.project_root_dir, update_requirements)
    printer.notice(u'Finished updating')

    printer.many_blank_lines()
    printer.succcess(u'Success')


def _confirm_production_server():
    printer.warn(u'Production server warning')

    if confirm(u'Are you sure you want to work on *PRODUCTION* server?', default=False) is False:
        abort(u'User canceled deployment.')


##############################
# End of Internal functions
##############################

def dev():
    """
    Deploy to development version.
    """
    env.project_root_dir = DEV_SERVER_PATH
    env.virtualenv = DEV_VIRTUALENV_NAME

    dev_env()

    _run_deployment_guide()


def production():
    _confirm_production_server()

    env.project_root_dir = PROD_SERVER_PATH
    env.virtualenv = PROD_VIRTUALENV_NAME

    prod_env()

    _run_deployment_guide()


def all_automatic():
    _confirm_production_server()

    # Update DEV
    env.project_root_dir = DEV_SERVER_PATH
    env.virtualenv = DEV_VIRTUALENV_NAME

    dev_env()

    _run_deployment_guide(no_questions=True)

    # Update PRODUCTION
    env.project_root_dir = PROD_SERVER_PATH
    env.virtualenv = PROD_VIRTUALENV_NAME

    prod_env()

    _run_deployment_guide(no_questions=True)


def commit():
    """
    Add all, comit and push.
    """
    # validate=r'^\w+$'
    commit_message = prompt("Commit message: ", default='No commit message specified')
    git.build_commit(commit_message)


def test_console():
    printer.notice("This is notice")
    printer.warn("Warning, be careful")
    printer.error("Fatal error! Terminating!")
    printer.succcess("Django applicatioin deployed")
