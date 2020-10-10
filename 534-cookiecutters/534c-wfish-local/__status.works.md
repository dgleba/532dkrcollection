
works.

just has simple model form with {{form}} render. nothing special, but thanks for the efforts. I appreciate it.



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@  
#@  notice: https not git:    --   cookiecutter https://github.com/wildfish/wildfish-django-starter.git
#@  
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   2020-10-05[Oct-Mon]21-08PM 


local not docker  on --- dg ubu398e-redek446

cookiecutter https://github.com/wildfish/wildfish-django-starter.git


albe@vamp398:/srv/dkr/532dkrcollection/534-cookiecutters/534c-wfish-local$ cookiecutter https://github.com/wildfish/wildfish-django-starter.git
/home/albe/.local/lib/python3.5/site-packages/arrow/arrow.py:28: DeprecationWarning: Arrow will drop support for Python 2.7 and 3.5 in the upcoming v1.0.0 release. Please upgrade to Python 3.6+ to continue receiving updates for Arrow.
  DeprecationWarning,
project_title [New Project]: wild01
project_name [newproject]: wild01
author_name [Your name]: dg
author_email [you@somewhere.com]: dgleba@gmail.com
domain_name [wildfish.com]: example.com
time_zone [Europe/London]: us/eastern
email_user []: dgleba
email_password []: a
sentry_dsn []:
app_name [things]:
model_name [Thing]:
model_name_lower [thing]:
albe@vamp398:/srv/dkr/532dkrcollection/534-cookiecutters/534c-wfish-local$



had to fix a few things, but it runs.


dc build

dc up


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@  
#@  
#@  
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   2020-10-05[Oct-Mon]21-12PM 



















=================================================

older


2020-09-13_Sun_22.13-PM

local not docker  on --- dg ubu398e-redek446


 1063  20-09-13 22:05:30 python3 --version
 1065  20-09-13 22:06:12 sudo apt install python3-pip
 1066  20-09-13 22:06:51 pip3 install cookiecutter
 1069  20-09-13 22:09:58 pip3 list
 1072  20-09-13 22:11:34 mkdir 534c-wfish-local
 1075  20-09-13 22:11:45 cookiecutter git@github.com:wildfish/wildfish-django-starter.git
albe@vamp398:/srv/dkr/532dkrcollection/534-cookiecutters/534c-wfish-local$



albe@vamp398:/srv/dkr/532dkrcollection/534-cookiecutters/534c-wfish-local$ cookiecutter git@github.com:wildfish/wildfish-django-starter.git
The authenticity of host 'github.com (140.82.114.3)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)? yes
Traceback (most recent call last):
  File "/home/albe/.local/bin/cookiecutter", line 11, in <module>
    sys.exit(main())
  File "/home/albe/.local/lib/python3.5/site-packages/click/core.py", line 829, in __call__
    return self.main(*args, **kwargs)
  File "/home/albe/.local/lib/python3.5/site-packages/click/core.py", line 782, in main
    rv = self.invoke(ctx)
  File "/home/albe/.local/lib/python3.5/site-packages/click/core.py", line 1066, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/home/albe/.local/lib/python3.5/site-packages/click/core.py", line 610, in invoke
    return callback(*args, **kwargs)
  File "/home/albe/.local/lib/python3.5/site-packages/cookiecutter/cli.py", line 152, in main
    skip_if_file_exists=skip_if_file_exists,
  File "/home/albe/.local/lib/python3.5/site-packages/cookiecutter/main.py", line 74, in cookiecutter
    directory=directory,
  File "/home/albe/.local/lib/python3.5/site-packages/cookiecutter/repository.py", line 114, in determine_repo_dir
    no_input=no_input,
  File "/home/albe/.local/lib/python3.5/site-packages/cookiecutter/vcs.py", line 104, in clone
    stderr=subprocess.STDOUT,
  File "/usr/lib/python3.5/subprocess.py", line 626, in check_output
    **kwargs).stdout
  File "/usr/lib/python3.5/subprocess.py", line 708, in run
    output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '['git', 'clone', 'git@github.com:wildfish/wildfish-django-starter.git']' returned non-zero exit status 128
albe@vamp398:/srv/dkr/532dkrcollection/534-cookiecutters/534c-wfish-local$


_____________



git clone git@github.com:wildfish/wildfish-django-starter.git

git clone https://github.com/wildfish/wildfish-django-starter.git


_____________

