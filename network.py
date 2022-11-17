# step 2 -> 3
def process_request_auth(request):
	if not verify_checksum(request, request.checksum):
		return "ACTION.REJECT"
	
	if not verify_ip(request.physical_address, request.network.source):
		return "ACTION.REJECT"
	
	previous_unique_token = fetch_previous_unique_token(request.wallet)
	if request.action.previous_token.unique_token != previous_unique_token \
			or previous_unique_token != algorithm(request):
		return "ACTION.REJECT"

	current_time = datetime.now()
	if current_time < request.action.previous_token.timestamp:
		return "ACTION.REJECT"
	
	if current_time < request.action.previous_token.expiration:
		return "ACTION.3a" # Approve the request directly
	else:
		authenticator = fetch_authenticator(request.wallet)
		return "ACTION.3b" # Request the network to select 10 registered voters
	
# step 3b -> 4
def generate_and_send_secret_token(request):
