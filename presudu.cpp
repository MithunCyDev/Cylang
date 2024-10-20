function parseProgram(tokens):
    while not endOfTokens():
        if nextToken() == "int":
            parseVariableDeclaration()
        elif nextToken() == "return":
            parseReturnStatement()

function parseVariableDeclaration():
    expect("int")
    identifier = nextToken()
    expect("=")
    value = nextToken()
    expect(";")

function parseReturnStatement():
    expect("return")
    value = nextToken()
    expect(";")




function generateLLVM(astNode):
    if astNode is Function:
        emit "define i32 @main() {"
        for each statement in astNode.body:
            generateLLVM(statement)
        emit "}"
    elif astNode is Declaration:
        emit "  %a = alloca i32"
        emit "  store i32 5, i32* %a"
    elif astNode is Return:
        emit "  %1 = load i32, i32* %a"
        emit "  ret i32 %1"
