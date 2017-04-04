

from ats.topology import loader


tb = loader.load('testbed.yaml')

device = tb.devices['chrome']

device.connect(via='webdriver')

import pdb

pdb.set_trace()

