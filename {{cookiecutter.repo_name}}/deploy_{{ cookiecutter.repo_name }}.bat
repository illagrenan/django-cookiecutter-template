@echo off

SET project_name={{ cookiecutter.repo_name }}
SET jenkins_url=http://127.0.0.1:8888/job/

echo Deploying %project_name%
http %jenkins_url%%project_name%/build
echo %project_name% will be deployed.

pause