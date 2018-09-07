class Token:
    def __init__(self, type, text):
        self.type = type
        self.text = text

class Lex:
    number = "number"
    operator = "operator"
    identifier = "identifier"
    def __init__(self):
        self.initialized = False

lex = Lex()

# Autogenerated with DRAKON Editor 1.31

def add_char(data, c):
    #item 47
    data.current.append(c)


def array_to_string(chars):
    #item 159
    result = ""
    for char in chars:
        #item 160
        result += char
    #item 161
    return result


def create_identifier(data):
    #item 53
    create_token(data, Lex.identifier)


def create_number(data):
    #item 69
    create_token(data, Lex.number)


def create_operator(data):
    #item 75
    create_token(data, Lex.operator)


def create_token(data, type):
    #item 59
    if len(data.current) == 0:
        pass
    else:
        #item 62
        text = data.current
        data.current = []
        #item 63
        token = token_create(type, text)
        data.tokens.append(token)


def define_op_char(text):
    #item 177
    lex.op_chars[text] = True


def define_space(text):
    #item 184
    lex.whitespace[text] = True


def is_long_op(first, second):
    #item 200
    op = first + second
    #item 111
    return op in lex.long_ops


def is_operator(c):
    #item 333
    return c in lex.op_chars


def is_space(c):
    #item 334
    return c in lex.whitespace


def lex_init():
    #item 117
    if lex.initialized:
        pass
    else:
        #item 116
        lex.op_chars = {}
        lex.long_ops = ["==", "!=", "<=", ">="]
        lex.initialized = True
        lex.whitespace = {}
        #item 140
        define_space(" ")
        define_space("\t")
        define_space("\r")
        define_space("\n")
        #item 119
        define_op_char("!")
        define_op_char("=")
        define_op_char("<")
        define_op_char(">")
        define_op_char("-")
        define_op_char("+")
        define_op_char("/")
        define_op_char("\\")
        define_op_char("*")
        define_op_char("%")
        define_op_char("(")
        define_op_char(")")
        define_op_char("(")
        define_op_char(")")
        define_op_char("{")
        define_op_char("}")
        define_op_char(":")
        define_op_char(".")
        define_op_char("#")
        define_op_char(",")
        define_op_char("^")
        define_op_char("|")
        define_op_char("&")
        define_op_char("'")
        define_op_char("\"")


def main():
    #item 331
    lex_init()
    #item 327
    text = "foo.Bar(34 / 4-(18+m * 3)) ==800"
    tokens = tokenize(text)
    #item 330
    print("  Text:\n" + text)
    print("  Tokens:")
    for token in tokens:
        #item 329
        token_print(token)
    #item 10
    frog = baby_frog()
    #item 11
    print("The baby frog says.")
    print(frog.state + "/sleep")
    print(frog.sleep(0))
    print(frog.state + "/food")
    print(frog.food(0))
    print(frog.state + "/food")
    print(frog.food(0))
    print(frog.state + "/sleep")
    print(frog.sleep(0))


def make_lexer():
    #item 325
    machine = Lexer_machine()
    machine.tokens = []
    machine.current = []
    #item 326
    return machine


def token_create(type, chars):
    #item 191
    text = array_to_string(chars)
    #item 192
    return Token(type, text)


def token_print(token):
    #item 198
    message = token.type + ": " + token.text
    #item 199
    print(message)


def tokenize(text):
    #item 302
    lexer = make_lexer()
    for c in text:
        #item 306
        if is_space(c):
            #item 319
            lexer.whitespace(c)
        else:
            #item 308
            if c.isdigit():
                #item 315
                lexer.digit(c)
            else:
                #item 312
                if is_operator(c):
                    #item 316
                    lexer.operator(c)
                else:
                    #item 311
                    lexer.letter(c)
    #item 320
    lexer.whitespace(" ")
    #item 305
    return lexer.tokens


def try_make_long_op(data, c):
    #item 81
    previous = data.current[0]
    #item 82
    if is_long_op(previous, c):
        #item 85
        data.current = []
        text = [ previous, c ]
        token = token_create(Lex.operator, text)
        data.tokens.append(token)
        #item 86
        return True
    else:
        #item 87
        return False


class baby_frog:
    def __init__(self):
        self.state = "Hungry"

    def food(self, msg):
        _state_ = self.state
        if _state_ == "Hungry":
            return self.Hungry_food(msg)
        elif _state_ == "Sleepy":
            return self.Sleepy_food(msg)
        return None

    def sleep(self, msg):
        _state_ = self.state
        if _state_ == "Hungry":
            return self.Hungry_sleep(msg)
        elif _state_ == "Sleepy":
            return self.Sleepy_sleep(msg)
        return None


    def Hungry_food(self, msg):
        #item 20
        self.state = "Sleepy"
        return "yam-yam"


    def Hungry_sleep(self, msg):
        #item 29
        self.state = "Hungry"
        return "I am hungry"


    def Sleepy_food(self, msg):
        #item 31
        self.state = "Sleepy"
        return "na..."


    def Sleepy_sleep(self, msg):
        #item 35
        self.state = "Hungry"
        return "z-z-z..."



class Lexer_machine:
    def __init__(self):
        self.state = "idle"

    def digit(self, c):
        _state_ = self.state
        if _state_ == "idle":
            return self.idle_digit(c)
        elif _state_ == "identifier":
            return self.identifier_digit(c)
        elif _state_ == "number":
            return self.number_digit(c)
        elif _state_ == "operator":
            return self.operator_digit(c)
        return None

    def dummy(self, c):
        _state_ = self.state
        if _state_ == "idle":
            return self.idle_default(c)
        elif _state_ == "number":
            return self.number_dummy(c)
        return None

    def letter(self, c):
        _state_ = self.state
        if _state_ == "idle":
            return self.idle_letter(c)
        elif _state_ == "identifier":
            return self.identifier_letter(c)
        elif _state_ == "number":
            return self.number_letter(c)
        elif _state_ == "operator":
            return self.operator_letter(c)
        return None

    def operator(self, c):
        _state_ = self.state
        if _state_ == "idle":
            return self.idle_operator(c)
        elif _state_ == "identifier":
            return self.identifier_operator(c)
        elif _state_ == "number":
            return self.number_operator(c)
        elif _state_ == "operator":
            return self.operator_operator(c)
        return None

    def whitespace(self, c):
        _state_ = self.state
        if _state_ == "idle":
            return self.idle_default(c)
        elif _state_ == "identifier":
            return self.identifier_whitespace(c)
        elif _state_ == "number":
            return self.number_whitespace(c)
        elif _state_ == "operator":
            return self.operator_whitespace(c)
        return None


    def idle_letter(self, c):
        #item 230
        add_char(self, c)
        #item 233
        self.state = "identifier"


    def idle_digit(self, c):
        #item 231
        add_char(self, c)
        #item 234
        self.state = "number"


    def idle_operator(self, c):
        #item 232
        add_char(self, c)
        #item 235
        self.state = "operator"


    def idle_default(self, c):
        #item 209
        self.state = "idle"


    def identifier_whitespace(self, c):
        #item 251
        create_identifier(self)
        #item 217
        self.state = "idle"


    def identifier_letter(self, c):
        #item 245
        add_char(self, c)
        #item 248
        self.state = "identifier"


    def identifier_digit(self, c):
        #item 246
        add_char(self, c)
        #item 249
        self.state = "identifier"


    def identifier_operator(self, c):
        #item 292
        create_identifier(self)
        #item 247
        add_char(self, c)
        #item 250
        self.state = "operator"


    def number_whitespace(self, c):
        #item 267
        create_number(self)
        #item 220
        self.state = "idle"


    def number_letter(self, c):
        #item 261
        add_char(self, c)
        #item 264
        self.state = "number"


    def number_digit(self, c):
        #item 262
        add_char(self, c)
        #item 265
        self.state = "number"


    def number_operator(self, c):
        #item 268
        create_number(self)
        #item 263
        add_char(self, c)
        #item 266
        self.state = "operator"


    def number_dummy(self, c):
        #item 266
        self.state = "operator"


    def operator_whitespace(self, c):
        #item 284
        create_operator(self)
        #item 212
        self.state = "idle"


    def operator_letter(self, c):
        #item 285
        create_operator(self)
        #item 278
        add_char(self, c)
        #item 281
        self.state = "identifier"


    def operator_digit(self, c):
        #item 286
        create_operator(self)
        #item 279
        add_char(self, c)
        #item 282
        self.state = "number"


    def operator_operator(self, c):
        #item 287
        if try_make_long_op(self, c):
            #item 290
            self.state = "idle"
        else:
            #item 291
            create_operator(self)
            #item 280
            add_char(self, c)
            #item 283
            self.state = "operator"


main()
