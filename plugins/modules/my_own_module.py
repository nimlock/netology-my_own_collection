#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_test

short_description: This is my test module

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
   path:
       description: This is the path for creating file.
       required: true
       type: str
   content:
       description: This is content of creating file.
       required: true
       type: str
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
   - my_namespace.my_collection.my_doc_fragment_name

author:
   - Zhilyaev Ivan (@nimlock)
'''

EXAMPLES = r'''
# Pass the module
- name: Test the module
 my_namespace.my_collection.my_test:
   path: /path/to/file
   content: "Hello, world!"
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
message:
   description: The output message that the test module generates.
   type: str
   returned: always
   sample: 'goodbye'
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
   # define available arguments/parameters a user can pass to the module
   module_args = dict(
       path=dict(type='str', required=True),
       content=dict(type='str', required=True)
   )

   # seed the result dict in the object
   # we primarily care about changed and state
   # changed is if this module effectively modified the target
   # state will include any data that you want your module to pass back
   # for consumption, for example, in a subsequent task
   result = dict(
       changed=False,
       message=''
   )
   current_content = ''

   # the AnsibleModule object will be our abstraction working with Ansible
   # this includes instantiation, a couple of common attr would be the
   # args/params passed to the execution, as well as if the module
   # supports check mode
   module = AnsibleModule(
       argument_spec=module_args,
       supports_check_mode=True
   )

   # if the user is working with this module in only check mode we do not
   # want to make any changes to the environment, just return the current
   # state with no modifications
   if module.check_mode:
       result['message'] = 'Run in checking mode, no changes.'
       module.exit_json(**result)

   # manipulate or modify the state as needed (this is going to be the
   # part where your module will do what it needs to do)
   try:
       with open(module.params['path'], 'r') as f:
           current_content = f.read()
   except FileNotFoundError:
       pass
   
   if current_content == module.params['content']:
       result['changed'] = False
       result['message'] = 'Target file {} already exists with given content.'.format(module.params['path'])
   else:
       try:
           with open(module.params['path'], 'w') as f:
               f.write(module.params['content'])
           result['message'] = 'Success with write file {} with given content.'.format(module.params['path'])
           result['changed'] = True
       except Exception:
           result['message'] = 'Something going wrong!'
           module.fail_json(msg='Your request finish with fail :(', **result)

   # in the event of a successful module execution, you will want to
   # simple AnsibleModule.exit_json(), passing the key/value results
   module.exit_json(**result)


def main():
   run_module()


if __name__ == '__main__':
   main()
