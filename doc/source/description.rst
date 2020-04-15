Description
--------------------------------------------------------------

Ansible role to add apt repositories to the apt sources.

This role performs the following actions:

- Ensure the requirements are installed.

- Ensure the current user can obtain administrative (root) permissions.

- If the **repositories** variable is defined, add to the apt sources the
  repositories listed on it.

- If the **configuration** variable is defined, add to the apt sources the
  repositories listed on it.