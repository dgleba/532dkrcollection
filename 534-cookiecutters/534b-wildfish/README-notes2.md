
# One


https://github.com/wildfish/wildfish-django-starter/


docker-compose run --rm djdev cookiecutter git@github.com:wildfish/wildfish-django-starter.git


albe@vamp398:/srv/dkr/532dkrcollection/534-cookiecutters/534b-wildfish$ docker-compose run --rm djdev cookiecutter git@github.com:wildfish/wildfish-django-starter.git

The authenticity of host 'github.com (140.82.114.3)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)? yes
Traceback (most recent call last):
  File "/usr/local/bin/cookiecutter", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.7/site-packages/click/core.py", line 829, in __call__
    return self.main(*args, **kwargs)
  File "/usr/local/lib/python3.7/site-packages/click/core.py", line 782, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.7/site-packages/click/core.py", line 1066, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.7/site-packages/click/core.py", line 610, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.7/site-packages/cookiecutter/cli.py", line 152, in main
    skip_if_file_exists=skip_if_file_exists,
  File "/usr/local/lib/python3.7/site-packages/cookiecutter/main.py", line 74, in cookiecutter
    directory=directory,
  File "/usr/local/lib/python3.7/site-packages/cookiecutter/repository.py", line 114, in determine_repo_dir
    no_input=no_input,
  File "/usr/local/lib/python3.7/site-packages/cookiecutter/vcs.py", line 104, in clone
    stderr=subprocess.STDOUT,
  File "/usr/local/lib/python3.7/subprocess.py", line 411, in check_output
    **kwargs).stdout
  File "/usr/local/lib/python3.7/subprocess.py", line 512, in run
    output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '['git', 'clone', 'git@github.com:wildfish/wildfish-django-starter.git']' returned non-zero exit status 128.
albe@vamp398:/srv/dkr/532dkrcollection/534-cookiecutters/534b-wildfish$



