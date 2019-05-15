<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-sys_audit.svg)](https://github.com/while-true-do/ansible-role-sys_audit/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-sys_audit.svg)](https://github.com/while-true-do/ansible-role-sys_audit/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-sys_audit.svg)](https://github.com/while-true-do/ansible-role-sys_audit/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-sys_audit.svg)](https://github.com/while-true-do/ansible-role-sys_audit/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-sys_audit.svg)](https://travis-ci.com/while-true-do/ansible-role-sys_audit)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_audit%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_audit)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_audit%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_audit)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-sys_audit%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/sys_audit)

# Ansible Role: sys_audit

An Ansible Role to install and configure audit.

## Motivation

[Audit](http://people.redhat.com/sgrubb/audit/) is a very common tool for
auditing systems and changes in RedHat('ish) Linux Environments.

## Description

This role installs and configures audit.

-   install audit
-   configure to local log
-   configure to receive logs
-   configure to send logs

## Requirements

Used Modules:

-   [Ansible Package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible Service Module](https://docs.ansible.com/ansible/latest/modules/service_module.html)
-   [Ansible Template Module](https://docs.ansible.com/ansible/latest/modules/template_module.html)


## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/sys_audit)
```
ansible-galaxy install while_true_do.sys_audit
```

Install from [Github](https://github.com/while-true-do/ansible-role-sys_audit)
```
git clone https://github.com/while-true-do/ansible-role-sys_audit.git while_true_do.sys_audit
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.srv_audit

# Package Management
wtd_sys_audit_package: "audit"
# State can be present|latest|absent
wtd_sys_audit_package_state: "present"

# Service Management
wtd_sys_audit_service: "auditd"
# State can be started|stopped
wtd_sys_audit_service_state: "started"
wtd_sys_audit_service_enabled: true

# Configuration Management
# Consult 'man audit.conf' for detailed information
wtd_sys_audit_conf:
  local_events: "yes"
  # write_logs: "yes"
  # log_file: "/var/log/audit/audit.log"
  # log_group: "root"
  # log_format: "ENRICHED"
  # flush: "INCREMENTAL_ASYNC"
  # freq: "50"
  # max_log_file: "8"
  # num_logs: "5"
  # priority_boost: "4"
  # name_format: "NONE"
  # name: "mydomain"
  # max_log_file_action: "ROTATE"
  # space_left: "75"
  # space_left_action: "SYSLOG"
  # verify_email: "yes"
  # action_mail_acct: "root"
  # admin_space_left: "50"
  # admin_space_left_action: "SUSPEND"
  # disk_full_action: "SUSPEND"
  # disk_error_action: "SUSPEND"
  # use_libwrap: "yes"
  # tcp_listen_port: "60"
  # tcp_listen_queue: "5"
  # tcp_max_per_addr: "1"
  # tcp_client_ports: "1024-65535"
  # tcp_client_max_idle: "0"
  # transport: "TCP"
  # krb5_principal: "auditd"
  # krb5_key_file: "/etc/audit/audit.key"
  # distribute_network: "no"
  # q_depth: "400"
  # overflow_action: "SYSLOG"
  # max_restarts: "10"
  # plugin_dir: "/etc/audit/plugins.d"

# Consult 'man audit.rules' for detailed information
wtd_sys_audit_rules:
  - rule
  - rule
  - rule
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.sys_audit
```

## Known Issues

None.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-sys_audit/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-sys_audit/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
