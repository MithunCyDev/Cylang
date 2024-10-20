import re

def lexer(code):
    token_specification = [
        ('KEYWORD', r'\b(int|return)\b'),  # Keywords like int, return
        ('NUMBER', r'\d+'),                # Integer numbers
        ('IDENTIFIER', r'[A-Za-z_][A-Za-z_0-9]*'),  # Variable names
        ('OPERATOR', r'[=+*/-]'),          # Arithmetic operators
        ('PAREN', r'[(){}]'),              # Parentheses and braces
        ('SEMICOLON', r';'),               # Statement terminator
        ('SKIP', r'[ \t]+'),               # Ignore spaces and tabs
    ]
    tok_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    get_token = re.compile(tok_regex).match
    pos = 0
    tokens = []
    while pos < len(code):
        mo = get_token(code, pos)
        if not mo:
            raise SyntaxError(f"Unexpected character at position {pos}")
        pos = mo.end()
        if mo.lastgroup != 'SKIP':
            tokens.append((mo.lastgroup, mo.group(mo.lastgroup)))
    return tokens

code = "int a = 5; return a;"
print(lexer(code))
