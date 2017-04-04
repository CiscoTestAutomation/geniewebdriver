

from ats.topology import loader


tb = loader.load('testbed.yaml')

device = tb.devices['chrome']

device.connect(via='webdriver')

from login import S3_LoginPage


login = S3_LoginPage(device)

try:
    login.login('lol', 'jb')
except Exception as e:
    import traceback
    traceback.print_exc()
    import pdb; pdb.set_trace()
    print('done')



import code
code.interact(local=locals())