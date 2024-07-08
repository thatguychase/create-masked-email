This code is designed to run as a Function on DigitalOcean's Serverless service.

## Deploying
Before deploying on DigitalOcean, edit the following parameters in the 'project.yml' file:
- Edit *'FM_USERNAME'* parameter to whatever your FastMail username is.
- Add your FastMail API token to the *'FM_TOKEN'* parameter.
- Generate a randomized secret and add it to the *'webSecure'* parameter. This secret will be required when making requests to the function.

To deploy, follow DigitalOcean's deployment guide [here](https://docs.digitalocean.com/products/functions/how-to/develop-functions/).

## Acknowledgement
This code relies heavily on the work of Hudson Bailey and his [fastmask](https://github.com/hdb/fastmask) FastMail Masked Email library.
