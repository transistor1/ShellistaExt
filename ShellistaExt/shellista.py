import os
from setuptools import setup
import sys

SHELLISTA_EXT = "https://github.com/transistor1/ShellistaExt/archive/master.tar.gz"

import contextlib
@contextlib.contextmanager
def _save_context():
    sys._argv = sys.argv[:]
    sys._path = sys.path[:]
    yield
    sys.argv = sys._argv
    sys.path = sys._path

def _run_setup():
    with _save_context():
        version_string = '0.0.2'

        setup_kwargs = {
            'name': 'ShellistaExt-Bootstrap',
            'description': 'A Python shell for iOS and Pythonista',
            'keywords': 'shellista ShellistaExt',
            'version': version_string,
            'url': 'https://github.com/transistor1/ShellistaExt',
            'license': 'MIT',
            'author': "briarfox@github",
            'author_email': 'noreply@github',
            'long_description': """
            ShellistaExt is a modular version of shellista, the shell for Pythonista on iOS.
            """,
            'packages': [],
            'install_requires': [
            # PyPI
            'gittle==0.3.0',
            'dulwich==0.9.7',

            # Non PyPI
            'funky',
            'mimer',
            'pipista',
            ],
            'dependency_links': [
                'https://github.com/FriendCode/funky/tarball/e89cb2ce4374bf2069c7f669e52e046f63757241#egg=funky-0.0.1',
                'https://github.com/FriendCode/mimer/tarball/a812e5f631b9b5c969df5a2ea84b635490a96ced#egg=mimer-0.0.1',
                'https://gist.githubusercontent.com/transistor1/0ea245e666189b3e675a/raw/23a23e229d6c279be3bc380c18c22fc2de24ef17/pipista.py#egg=pipista-23a23',

            ],
        }

        print "Setting up..."

        #cwd = os.getcwd()
        #sys.argv = [sys.argv[0], 'install', '--home={0}/site-packages'.format(cwd)]
        #sys.path.extend([cwd,os.path.join(cwd, 'site-packages')])
        #os.environ['PYTHONPATH'] = os.pathsep.join(sys.path)

        import urllib2, tarfile

        #Hackishness to download the ShellistaExt module
        tgz = urllib2.urlopen(SHELLISTA_EXT)
        tgz_file_name = 'shellistaext.tar.gz'
        with open(tgz_file_name,'wb') as output:
            output.write(tgz.read())

        with tarfile.open(tgz_file_name, 'r:gz') as tfile:
            tfile.extractall('.')

        os.unlink(tgz_file_name)
        os.rename('ShellistaExt-master/ShellistaExt', 'ShellistaExt')

        sys.argv = [sys.argv[0], 'install', '--user']

        setup(**setup_kwargs)
        os.mkdir('.shellista')
        print "** Installation complete. Please re-run shellista.py."

if __name__=="__main__":
    if os.path.exists('.shellista'):
        import site
        sys.path.append(site.USER_SITE)
        sys.path.append(os.path.join(os.getcwd(),'ShellistaExt'))
        os.chdir(os.path.join(os.getcwd(),'ShellistaExt'))
        from ShellistaExt import Shellista
        shell = Shellista()
        shell.cmdloop()
    else:
        _run_setup()



