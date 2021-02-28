single_task_role
=========

Role for testing my_own_module.

Role Variables
--------------
There are three vars that you can redefine:
```yaml
path: "/tmp/third_test" # Path to file which need to create
content: "Hello from role :))" # What you want to write to file
debug_mode: no # Whether run debug task or not
```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: all
  roles:
      - single_task_role
```

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
