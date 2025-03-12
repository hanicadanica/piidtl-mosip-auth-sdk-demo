from mosip_auth_sdk import MOSIPAuthenticator
from mosip_auth_sdk.models import DemographicsModel
from dynaconf import Dynaconf

config = Dynaconf(settings_files=["./config.toml"], environments=False)
authenticator = MOSIPAuthenticator(config=config)

# kyc auth
demographics_data = DemographicsModel(
    name=[{"language": "eng", "value": "James Rodrigious"}],
)
print(f"Demographics data: {demographics_data.model_dump()}")

response = authenticator.kyc(
    individual_id="2047631038",
    individual_id_type="UIN",
    demographic_data=demographics_data,
    consent=True,
)
response_body = response.json()
# print(f"RESPONSE: {response_body}")

decrypted_response = authenticator.decrypt_response(response_body)
print(f"DECRYPTED RESPONSE: {decrypted_response}")
