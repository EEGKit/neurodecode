from __future__ import print_function, division

import neurodecode
import neurodecode.utils.nd_lsl as nd_lsl
import time

LSL_SERVER = 'RexController'
print('Connecting to %s server' % LSL_SERVER)
inlet = nd_lsl.start_client(LSL_SERVER)

while True:
    # pull_chunk
    if 0:
        data, ts = inlet.pull_chunk()
        if len(data) > 0:
            print('Recevied data', data)
        else:
            print('.', end='')
        time.sleep(0.1)

    # pull_sample
    if 1:
        data, ts = inlet.pull_sample()
        print('Recevied data type', type(data), 'value', data)
