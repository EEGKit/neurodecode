from __future__ import print_function, division

"""
Add Cybex events for patient 6.

* For patients 2 and 5, use mat2fif.py since the mat file structure is completely different.

Kyuhwa Lee
Swiss Federal Institute of Technology (EPFL)
"""

import os
import sys
import mne
import numpy as np
import neurodecode.utils.q_common as qc
import neurodecode.utils.pycnbi_utils as pu
from builtins import input
from IPython import embed
mne.set_log_level('ERROR')

def run(fif_file):
    print('Loading "%s"' % fif_file)
    raw, events = pu.load_raw(fif_file)
    print('Raw info: %s' % raw)
    print('Channels: %s' % ', '.join(raw.ch_names))
    if len(events) > 0:
        print('Events: %s' % set(events[:, 2]))
    print('Sampling freq: %.3f Hz' % raw.info['sfreq'])
    qc.print_c('\n>> Interactive mode start. Type quit or Ctrl+D to finish', 'g')
    qc.print_c('>> Variables: raw, events\n', 'g')
    embed()

# for batch scripts
def batch_run(fif_file):
    run(fif_file)

def main():
    """
    Invoked from console
    """
    if len(sys.argv) == 1:
        print('Usage: %s fif_file' % os.path.basename(__file__))
        return

    fif_file = sys.argv[1]
    batch_run(fif_file)


if __name__ == '__main__':
    main()
