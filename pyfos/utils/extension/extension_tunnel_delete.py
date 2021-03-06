#!/usr/bin/env python3

# Copyright © 2018 Broadcom. All Rights Reserved. The term “Broadcom” refers to
# Broadcom Inc. and/or its subsidiaries.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may also obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""

:mod:`extension_tunnel_delete` - PyFOS util for deleting a tunnel.
*******************************************************************************
The :mod:`extension_tunnel_delete` util provides tunnel deletion functionality.

This module is a stand-alone script that can be used to delete an extension
tunnel.

extension_tunnel_delete.py: Usage

* Infrastructure Options:
    * -i,--ipaddr=IPADDR: The IP address of the FOS switch.
    * -L,--login=LOGIN: The login name.
    * -P,--password=PASSWORD: The password.
    * -f,--vfid=VFID: The VFID to which the request is directed.
    * -s,--secured=MODE: The HTTPS mode "self" or "CA" [Optional].
    * -v,--verbose: Verbose mode [Optional].

* Util Script Options:
    * -n,--name=NAME: Sets the name.

* Outputs:
    * Python dictionary content with RESTCONF response data.

.. function:: extension_tunnel_delete.delete_extension_tunnel(session, name)

    *Delete an Extension Tunnel*

        Example Usage of the Method::

            ret = extension_tunnel_delete.delete_extension_tunnel(session,
            name)
            print (ret)

        Details::

            tunnel = {
                            "name": name,
                       }
            result = extension_tunnel_delete._delete_extension_tunnel(session,
            tunnel)

        * Input:
            :param session: The session returned by the login.
            :param name: Sets the VE_Port name expressed as slot/port.

        * Output:
            :rtype: A dictionary of return status matching the REST response.

        *Use Cases*

         Delete an extension tunnel.
"""


import sys
from pyfos import pyfos_auth
from pyfos import pyfos_util
from pyfos.pyfos_brocade_extension_tunnel import extension_tunnel
from pyfos.utils import brcd_util

isHttps = "0"


def _delete_extension_tunnel(session, tnlobject):
    result = tnlobject.delete(session)
    return result


def delete_extension_tunnel(session, name):
    value_dict = {'name': name}
    tnlobject = extension_tunnel(value_dict)
    result = _delete_extension_tunnel(session, tnlobject)
    return result


def validate(tnlobject):
    if tnlobject.peek_name() is None:
        return 1
    return 0


def main(argv):
    # myinput = str("-i 10.17.3.70  -n 4/19 ")
    # argv = myinput.split()
    filters = ['name']
    inputs = brcd_util.parse(argv, extension_tunnel, filters, validate)
    tnlobject = inputs['utilobject']
    session = brcd_util.getsession(inputs)
    result = _delete_extension_tunnel(session, tnlobject)
    pyfos_util.response_print(result)
    pyfos_auth.logout(session)


if __name__ == "__main__":
    main(sys.argv[1:])
