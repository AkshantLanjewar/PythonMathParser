
class MathParser(object):

	def __init__(self, expression):
		self.expression = expression
		self.index = 0
		
		self.tokens = []
		self.splitTokens = []

		#standard positions
		self.variable_header = 0


	def parse(self):
		self.splitString()
		self.crawl_var()

	def splitString(self):
		unsplitString = self.expression
		self.splitTokens = list(unsplitString)
	def crawl_var(self):
		char_iter = iter(self.splitTokens)
		tmp_string_reg = ""

		for token in char_iter:
			if token.isdigit() == False and token != "+" and token != "-" and token != "/" and token != "*" and token != "=":
				if token == " ":
					if tmp_string_reg != "":
						if self.variable_header < len(self.tokens):
							self.tokens[0].append(tmp_string_reg)
						else:
							append_lst = ["variable_header", tmp_string_reg]
							self.tokens.insert(0, append_lst)

					tmp_string_reg = ""
				else:
					tmp_string_reg = tmp_string_reg + token
		print(self.tokens)


parser = MathParser("xs * 2 = 4")
parser.parse()