import json

def retrieve_credentials() -> dict:
    """
    Retrieves credentials to authenticate in Reddit.

    Params
    ------
        None

    Returns
    -------
        dict
            A dict containing user, password, client-id, client-secret and user agent. All this data is specific for each user.
    """
    credentials: dict = {}
    cred_filepath: str = "app_credentials.json"
    
    with open(cred_filepath, "rb") as cred_file:
        credentials = json.load(cred_file)

    return credentials
