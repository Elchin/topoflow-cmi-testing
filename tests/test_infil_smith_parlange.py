#!/usr/bin/env python

import os
from cmt.components import InfilSmithParlange as Component
from . import example_dir


cfg_file = os.path.join(example_dir, 'June_20_67_infil_smith_parlange.cfg')


def test_irf():
    component = Component()
    component.initialize(cfg_file)
    component.update(1.0)
    component.finalize()
