from __future__ import with_statement
from fabric.api import *

import uuid

env.roledefs = {
    'production': ['agile@10.0.125.7'],
}

@roles('production')
def deploy():
    code_dir = '/usr/local/django/answebsite/'
    virtualenv_dir = '/usr/local/django/virtualenvs/answebsite/'
    python = virtualenv_dir + 'bin/python'
    pip = virtualenv_dir + 'bin/pip'
    django_admin = python + ' manage.py'

    with settings(sudo_user='answebsite'):
        with cd(code_dir):
            sudo("git pull")
            sudo(pip + " install -r requirements.txt")
            sudo(django_admin + " migrate --noinput --settings=ans.settings.production")
            sudo(django_admin + " collectstatic --noinput --settings=ans.settings.production")
            sudo(django_admin + " compress --force --settings=ans.settings.production")

    sudo("systemctl restart answebsite")


@roles('production')
def fetch_data():
    file_name = 'answebsite_%s.sql' % uuid.uuid4()
    dumps_dir = '/home/answebsite/dumps/'

    with settings(sudo_user='answebsite'):
        sudo("pg_dump -cO -f %s answebsite" % (dumps_dir + file_name))
        sudo("gzip %s" % (dumps_dir + file_name))
        get("%s.gz" % (dumps_dir + file_name), "/tmp/%s.gz" % file_name)
        sudo("rm %s.gz" % (dumps_dir + file_name))

    local("gunzip /tmp/%s.gz" % file_name)
    local("dropdb answebsite")
    local("createdb answebsite")
    local("psql answebsite -f /tmp/%s" % file_name)
    local("rm /tmp/%s" % file_name)


@roles('production')
def fetch_media():
    media_dir = '/usr/local/django/answebsite/media/'

    local('rsync -avz %s:%s /vagrant/media/' % (env['host_string'], media_dir))
