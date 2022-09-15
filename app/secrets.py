import oci
import base64
import sys

# Retrieve secret
def read_secret_value(secret_ocid):

    # Replace secret_id value below with the ocid of your secret
    secret_id = secret_ocid

    # By default this will hit the auth service in the region the instance is running.
    signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()

    # In the base case, configuration does not need to be provided as the region and tenancy are obtained from the InstancePrincipalsSecurityTokenSigner
    identity_client = oci.identity.IdentityClient(config={}, signer=signer)

    # Get instance principal context
    secret_client = oci.secrets.SecretsClient(config={}, signer=signer)

    response = secret_client.get_secret_bundle(secret_id)
    base64_Secret_content = response.data.secret_bundle_content.content
    base64_secret_bytes = base64_Secret_content.encode('ascii')
    base64_message_bytes = base64.b64decode(base64_secret_bytes)
    secret_content = base64_message_bytes.decode('ascii')
    return format(secret_content)
