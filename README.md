## MOSIP Authentication SDK Demo Files

Simple Python scripts to demonstrate the capabilities of MOSIP's Authentication SDK. More information on the SDK can be found [here](https://docs.mosip.io/1.2.0/id-lifecycle-management/identity-verification/id-authentication-services/mosip-authentication-sdk). The repository for the Authentication SDK can be found [here](https://github.com/mosip/ida-auth-sdk/tree/develop).


### Requirements

* Python 3
* Be onboarded as a MOSIP authentication partner and have the necessary certificates. More information on authentication partners can be found [here](https://docs.mosip.io/1.2.0/id-lifecycle-management/support-systems/partner-management-services/partners).
* A `config.toml` file containing the API URLs, partner ID, API key, MISP license key, and the locations of the required certificates. A sample config file can be found [here](https://github.com/mosip/ida-auth-sdk/blob/develop/examples/config.toml).

### Usage
It is recommended to create a Python virtual environment.
```bash
python -m venv env
source ./env/bin/activate
```

Install the requirements using `pip`:
```bash
pip install -r requirements.txt
```

Then run the desired script:
```bash
python yes_no_auth.py
```