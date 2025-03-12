from mosip_auth_sdk import MOSIPAuthenticator
from mosip_auth_sdk.models import DemographicsModel
from dynaconf import Dynaconf

config = Dynaconf(settings_files=["./config.toml"], environments=False)
authenticator = MOSIPAuthenticator(config=config)

# yes/no auth
demographics_data = DemographicsModel(dob="1992/04/29")
print(f"Demographics data: {demographics_data.model_dump()}")

# try using this to authenticate using the name
# demographics_data = DemographicsModel(name=[{"language": "eng", "value": "James Rodrigious"}])

response = authenticator.auth(
    individual_id="2047631038",
    individual_id_type="UIN",
    demographic_data=demographics_data,
    consent=True,
)
response_body = response.json()
print(f"RESPONSE: {response_body}")
