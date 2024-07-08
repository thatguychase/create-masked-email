from masked_mail import MaskedMailClient
from os import environ as env

def main(args):
    client = MaskedMailClient(username=env.get("FM_USERNAME"),
                              token=env.get("FM_TOKEN"))
    
    response = client.new(url=args.get("url"),
                          description=args.get("description"),
                          domain=env.get("DOMAIN"),
                          state="enabled")
    
    try:
        result = [v for k,v in response[1]["created"].items()][0]
        
        return {
            'body': {
                'status_code': 200,
                'message': result['email']
            }
        }
        
    except Exception as e:
        return {
            'body': {
                'status_code': 500,
                'message': e,
            }
        }
