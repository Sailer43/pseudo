Class Voters:
	
	def __init__(self,data):
		self.wallets.append(data.wallet_address)
		self.authenticator[data.wallet_address] = data.authenticator

	def generate_token(data):
		token = RANDOM_TOKEN_GENERATION()
		voter.token[data.wallet_address] = token
		return token

	def match_token(tokens,data):
		return authenticator[data.wallet_address] == token


def voters_match_tokens(voters,tokens,request_data):
	for v in voters:
		if v.match_token == False:
			return False
	return True