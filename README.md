# Sugar 10 PRPackage Installer

## Installation

```shell script
python3 -m pip install -r requirements.txt
```
## Adding a new Environment in Environments.json file
- envi_url = "Give the url of the Environment"
- credentials = "Give the payload url with username and password"
- example : check it in "environments.json" file

## Running the Scripts

- Download and Place the PRPackage file in the root Directory.
-  For installing the scripts :
- `python3 deploy_install_pkg.py <environment_name> <prnumber>`
-  For uninstalling the scripts :
- `python3 deploy_uninstall_pkg.py <environment_name> <prnumber>`

For example:

```shell script
python3 deploy_install_pkg.py int 2312
python3 deploy_uninstall_pkg.py int 2312
```

## Todo

- Download the PRPackage Script automatically.
- Add config file to make the codebase dynamic.
- Add configs for all VMs.
