# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (c) 2020 Intel Corporation
#                    Wojtek Porczyk <woju@invisiblethingslab.com>
#

from . import Exec

# pylint: disable=invalid-name

class HelloWorld:
    # pylint: disable=no-self-use

    helloworld = Exec('helloworld', manifest_template='basic.manifest.template')
    setup = helloworld.setup

    def time_gramine_nosgx(self):
        self.helloworld.run_in_gramine(sgx=False)

    def time_gramine_sgx(self):
        self.helloworld.run_in_gramine(sgx=True)

class WritePages:
    # pylint: disable=no-self-use

    write_pages = Exec('write_pages', manifest_template='basic.manifest.template')
    params = [10000, 100000, 1000000, 10000000]
    param_names = ['pagecount']
    setup = write_pages.setup

    def time_gramine_nosgx(self, pagecount):
        self.write_pages.run_in_gramine(str(pagecount), sgx=False)

    def time_gramine_sgx(self, pagecount):
        self.write_pages.run_in_gramine(str(pagecount), sgx=True)
