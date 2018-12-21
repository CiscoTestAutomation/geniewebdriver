'''

Run this job file using"

    easypy job.py -testbed_file etc/testbed.yaml

'''

import os

from ats.easypy import run

SCRIPT_DIR = os.path.dirname(os.path.dirname(__file__))


def main():

    run(testscript = os.path.join(SCRIPT_DIR, 'script.py'),
        browser = 'firefox',
        base_url = 'http://www.google.com/')
