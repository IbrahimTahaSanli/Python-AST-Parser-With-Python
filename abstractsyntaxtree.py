import re

class examples:
    ex1 = """def printNumber(start , end):
    asd = "done"
    for i in range(start, end, 1):
        print(i)

    print(done)
"""
    ex2 = """
    """

class Node:
    type = -1
    baseType = -1

class Statement(Node):
    def __init__(self) -> None:
        self.body = []
        self.indent = 0
        self.baseType = 0

    def __str__(self) -> str:
        return "Statement"

    def returnChildCount(self):
        return 1 + sum(i.returnChildCount() for i in self.body)

    def diffWithOtherNode(self, other):
        count = 0



class RootNode(Statement):
    def __init__(self):
        super().__init__()

        self.type = "RootNode"

    def __str__(self) -> str:
        return "RootNode"        

class Loop(Statement):
    def __init__(self) -> None:
        super().__init__()

        self.condition = None
        self.list = None
    
    def __str__(self) -> str:
        return "Loop"

    def returnChildCount(self):
        return super().returnChildCount() + self.condition.returnChildCount()

    ForLoop = (70, "^for( )( )*")
    WhileLoop = (71, "^while( )*\(")

class Library(Statement):
    def __init__(self) -> None:
        super().__init__()

        self.library = None
        self.functions = None
    
    def __str__(self) -> str:
        return "Library"

    def returnChildCount(self):
        return super().returnChildCount() + self.library.returnChildCount()

    Import = ( 68 , "^import( )( )*" )
    From = ( 69 , "^from( )( )*" )

class Function(Statement):
    def __init__(self) -> None:
        super().__init__()

        self.type = None
        self.name = None
        self.parameters = None

    def __str__(self) -> str:
        return "Function"

    def returnChildCount(self):
        return super().returnChildCount() + self.type.returnChildCount() + self.parameters.returnChildCount() + 1 #for name is string 

    Definition = (65,"^def( )( )*")
    Call = (66,"^[a-zA-Z_][a-zA-Z0-9_]*\(")
    LambdaDefinition = (67,"^lambda( )( )*")

class If(Statement):
    def __init__(self) -> None:
        super().__init__()

        self.condition = None
    
    def __str__(self) -> str:
        return "IfElifElse"

    def returnChildCount(self):
        return super().returnChildCount() + self.condition.returnChildCount()

    If = (62,"^if( )*\(( )*")
    Elif = (63, "^elif( )*\(( )*")
    Else = (64,"^else( )*:")

class Expression(Node):  
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.type = None
        self.baseType = 1

    def __str__(self) -> str:
        return "Expression"
        
    def returnChildCount(self):
        return self.left.returnChildCount() + self.right.returnChildCount() + 1 # type is string 

class AssigmentOper(Expression):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "AssigmentOper"

    def returnChildCount(self):
        return super().returnChildCount()

    LeftShiftAssigment = (50, "^<<=( )*")
    RightShiftAsigment = (51,"^>>=( )*( )*")
    FloorDivisionAssigment = (52, "^//=( )*")
    PowerAssigment = (53,"^\*\*=( )*")
    AdditionAssigment = (54,"^\+=( )*")
    SubtractAssigment = (55,"^-=( )*")
    MultiplyAssigment = (56,"^\*=( )*")
    DivisionAssigment = (57,"^/=( )*")
    ModuloAssigment = (58,"^%=( )*")
    AndAssigment = (59,"^&=( )*")
    OrAssigment = (60,"^\|=( )*")
    XorAssigment = (61,"^\^=( )*")
    Assigment = (81, "^( )*=( )*")

class ArithmaticOper(Expression):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "ArithmaticOper"

    def returnChildCount(self):
        return super().returnChildCount()

    FloorDiv = (43, "^//( )*")
    Power = (44,"^\*\*( )*")
    Modulo = (45,"^%( )*")
    Division = (46,"^/( )*")
    Multiplication = (47,"^\*( )*")
    Subtraction = (48,"^[-]( )*")
    Addition = (49,"^\+( )*")

class BitwiseOper(Expression):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "BitwiseOper"

    def returnChildCount(self):
        return super().returnChildCount()

    LeftShift = (37, "^<<( )*")
    RightShift = (38,"^>>( )*")
    And = (39,"^&( )*")
    Or = (40,"^\|( )*")
    Not = (41,"^~( )*")
    Xor = (42,"^\^( )*")

class ComprasionOper(Expression):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "ComprasionOper"

    def returnChildCount(self):
        return super().returnChildCount()

    Equal = (31,"^==( )*")
    NotEqual = (32,"^!=( )*")
    LessOrEqual = (33,"^<=( )*")
    MoreOrEqual = (34,"^>=( )*")
    Less = (35,"^<( )*")
    More = (36,"^>( )*")


class LogicalOper(Expression):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "LogicalOper"

    def returnChildCount(self):
        return super().returnChildCount()

    And = (26,"^and ( )*")
    Or = (27,"^or ( )*")
    Not = (28,"^not ( )*")
    Is = (29,"^is ( )*")
    In = (30,"^( )*in ( )*")

class Conevtions(Expression):
    def __init__(self) -> None:
        super().__init__()
    
    def __str__(self) -> str:
        return "Conevtions"

    def returnChildCount(self):
        return super().returnChildCount()

    As = (25, "^as ")

class SyncOper(Statement):
    def __init__(self) -> None:
        super().__init__()

    def __str__(self) -> str:
        return "SyncOper"

    def returnChildCount(self):
        return super().returnChildCount()

    Async = (23,"^async ")
    Await = (24,"^await ")

class LoopControls(Statement):
    def __init__(self) -> None:
        super().__init__()
    
    def __str__(self) -> str:
        return "LoopControls"

    def returnChildCount(self):
        return super().returnChildCount()

    Break = (21,"^break( )*(\n)")
    Continue = (22,"^continue( )*(\n)")

class Class(Statement):
    def __init__(self) -> None:
        super().__init__()

        self.name = None
        self.Parents = None
    
    def __str__(self) -> str:
        return "Class"

    def returnChildCount(self):
        return super().returnChildCount() + self.Parents.returnChildCount() + 1 # name is string  
    
    Class = (20, "^class ")

class FunctionRet(Statement):
    def __init__(self) -> None:
        super().__init__()

        self.returns = None

    def __str__(self) -> str:
        return "FunctionRet"

    def returnChildCount(self):
        return super().returnChildCount() + self.returns.returnChildCount()

    Pass = (17, "^pass( )*(\n)")
    Return = (18,"^return( )( )*")
    Yield = (19,"^yield( )( )*")
    Indent = (80, "^( )*\:( )*\n")

class Del(Statement):
    def __init__(self) -> None:
        super().__init__()

        self.value = None

    def __str__(self) -> str:
        return "Del"

    def returnChildCount(self):
        return super().returnChildCount() + self.value.returnChildCount()

    Del = (16 , "^del( )( )*")

class ErrorHandling(Statement):
    def __init__(self) -> None:
        super().__init__()
        
        self.exceptionType = None

    def __str__(self) -> str:
        return "ErrorHandling"

    def returnChildCount(self):
        return super().returnChildCount() + self.exceptionType.returnChildCount()

    Try = (11,"^try( )*:")
    Except = (12,"^except( )( )*")
    Finnaly = (13,"^finnaly( )*:")
    Raise = (14,"^raise( )( )*")
    Assert = (15,"^assert( )( )*")

class ScopeDefinition(Statement):
    def __init__(self) -> None:
        super().__init__()
        
        self.variables = None

    def __str__(self) -> str:
        return "ScopeDefinition"

    def returnChildCount(self):
        return super().returnChildCount() + self.variables.returnChildCount()

    Global = (8,"^global( )( )*")
    Nonlocal = (9,"^nonlocal( )( )*")
    With = (10,"^with( )( )*")

class Const(Node):
    def __init__(self) -> None:
        self.value = None
        self.baseType = 2

    def __str__(self) -> str:
        return "Const"

    def returnChildCount(self):
        return 2

    FalseConst = ( 1, "^False( )( )*" )
    TrueConst = ( 2, "^True( )( )*" ) 
    NoneConst = ( 3, "^None( )( )*" ) 
    StringConst = ( 4 , "^\".*\"( )*" )
    SpaceConst = ( 5 , "^( )*" )
    NewLineConst = ( 6 , "^( )*(\n)(\n)*" )
    NumberConst = ( 7, "^[0-9][0-9]*([.][0-9]*)?" )


class Variable(Node):
    def __init__(self) -> None:
        self.name = ""
        self.array = None

        self.baseType = 3

    def __str__(self) -> str:
        return "Variable"

    def returnChildCount(self):
        return 3

    ArrayVariable = (82, "^[a-zA-Z_][a-zA-Z0-9_]*( )*\[")
    Variable = (0,"^[a-zA-Z_][a-zA-Z0-9_]*( )*")


class Tuple(Node):
    def __init__(self) -> None:
        self.items = []
        self.baseType = 4

    def __str__(self) -> str:
        return "Tuple"

    def returnChildCount(self):
        return 1 + sum(i.returnChildCount() for i in self.items)

    TupleStart = (72, "^( )*\(( )*" )
    TupleEnd = (73, "^( )*\)")
    Array = (74, "^( )*\[( )*" )
    ArraySep = (75,"^( )*,( )*")
    ArrayEnd = (76, "^( )*\]")
    DictionaryStart = (77, "^( )*\{( )*")
    DictionaryLink = (78, "^( )*:( )*")
    DictionaryEnd = (79, "^( )*\}")


class ast:
    Order = [
        ErrorHandling.Try,
        ErrorHandling.Except,
        ErrorHandling.Finnaly,
        ErrorHandling.Raise,
        ErrorHandling.Assert,

        SyncOper.Async, 
        SyncOper.Await,

        ScopeDefinition.Global,
        ScopeDefinition.Nonlocal,
        ScopeDefinition.With,
    
        LoopControls.Break,
        LoopControls.Continue,

        Class.Class,

        FunctionRet.Pass,
        FunctionRet.Return,
        FunctionRet.Yield,
        FunctionRet.Indent,

        Library.Import,
        Library.From,

        If.If,
        If.Elif,
        If.Else,

        Function.Definition,
        Function.Call,
        Function.LambdaDefinition,

        Const.FalseConst,
        Const.NoneConst,
        Const.TrueConst,

        Loop.WhileLoop,
        Loop.ForLoop,

        LogicalOper.And,
        LogicalOper.Or,
        LogicalOper.Not,
        LogicalOper.Is,
        LogicalOper.In,

        Conevtions.As,

        AssigmentOper.LeftShiftAssigment,
        AssigmentOper.RightShiftAsigment,
        AssigmentOper.FloorDivisionAssigment,
        AssigmentOper.PowerAssigment,
        AssigmentOper.AdditionAssigment,
        AssigmentOper.SubtractAssigment,
        AssigmentOper.MultiplyAssigment,
        AssigmentOper.DivisionAssigment,
        AssigmentOper.ModuloAssigment,
        AssigmentOper.AndAssigment,
        AssigmentOper.OrAssigment,
        AssigmentOper.XorAssigment,
        AssigmentOper.Assigment,

        ArithmaticOper.FloorDiv,
        ArithmaticOper.Power,
        ArithmaticOper.Modulo,
        ArithmaticOper.Division,
        ArithmaticOper.Multiplication,
        ArithmaticOper.Subtraction,
        ArithmaticOper.Addition,

        Const.NewLineConst,

        BitwiseOper.LeftShift,
        BitwiseOper.RightShift,
        BitwiseOper.And,
        BitwiseOper.Or,
        BitwiseOper.Xor,
        BitwiseOper.Not,

        ComprasionOper.Equal,
        ComprasionOper.NotEqual,
        ComprasionOper.LessOrEqual,
        ComprasionOper.MoreOrEqual,
        ComprasionOper.Less,
        ComprasionOper.More,

        Tuple.TupleStart,
        Tuple.TupleEnd,
        Tuple.Array,
        Tuple.ArrayEnd,
        Tuple.DictionaryStart,
        Tuple.ArraySep,

        Const.StringConst,

        Const.NumberConst,

        Variable.ArrayVariable,
        Variable.Variable,
    ]

    def __init__(self, code) -> None:
        self.rootNode = RootNode()
        self.nodePath = [(self.rootNode,0)]
        self.code = code.replace("\t", " "*4)
        self.lastIndex = 0

    def parse(self, startIndex):
        for node in self.Order:
            res = re.search(node[1], self.code[startIndex:]) 
            if(res != None):
                return (node,res)
        return None

    def parseFor(self, startIndex, node):
        return re.search(node[1], self.code[startIndex:])

    def start(self):
        while(self.code[self.lastIndex:] != ""):
            node = self.RegexCheck(self.lastIndex)
            if(node.o != )
            self.rootNode.body.append( node )

        return self

    def RegexCheck(self, startIndex)->int:
        parsed = self.parse(startIndex)
        if(parsed == None):
            return None
        match parsed[0][0]:
            case 0:
                node = Variable()
                node.name = parsed[1].group()
                self.lastIndex += parsed[1].span()[1]
                return node

            case 1|2|3:
                node = Const()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]

                return node

            case 4:
                node = Const()
                node.type = parsed[0][0]
                node.value = parsed[1].group()
                self.lastIndex += parsed[1].span()[1]

                return node

            case 5|6:
                node = Const()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]

                return node

            case 7:
                node = Const()
                node.type = parsed[0][0]
                node.value = parsed[1].group()
                self.lastIndex += parsed[1].span()[1]

                return node

            case 8|9:
                node = ScopeDefinition()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                node.variables = self.parseList(self.lastIndex)
                return node

            case 10:
                node = ScopeDefinition()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                node.variables = self.RegexCheck(self.lastIndex)
                return node

            case 11:
                node = ErrorHandling()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                node.body = self.RegexCheck(self.lastIndex)
                currentIndent = self.parseFor(self.lastIndex, Const.SpaceConst)
                for i in range(0, len(self.nodePath),1):
                    if(self.nodePath[i][1] == currentIndent):
                        self.nodePath = self.nodePath[:i+1]
                return node
            
            case 12:
                node = ErrorHandling()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                node.exceptionType = self.RegexCheck(self.lastIndex)
                node.body = self.RegexCheck(self.lastIndex)
                currentIndent = self.parseFor(self.lastIndex, Const.SpaceConst)
                for i in range(0, len(self.nodePath),1):
                    if(self.nodePath[i][1] == currentIndent):
                        self.nodePath = self.nodePath[:i+1]
                return node

            case 13:
                node = ErrorHandling()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                node.body = self.RegexCheck(self.lastIndex)
                currentIndent = self.parseFor(self.lastIndex, Const.SpaceConst)
                for i in range(0, len(self.nodePath),1):
                    if(self.nodePath[i][1] == currentIndent):
                        self.nodePath = self.nodePath[:i+1]
                return node

            case 14|15:
                node = ErrorHandling()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                node.exceptionType = self.RegexCheck(self.lastIndex)
                return node
            
            case 16:
                node = Del()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                node.value = self.RegexCheck(self.lastIndex)
                return node
            
            case 17:
                node = FunctionRet()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                return node

            case 18|19:
                node = FunctionRet()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                node.returns = self.RegexCheck(self.lastIndex)
                return node

            case 20:
                node = Class()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                node.name = self.RegexCheck(self.lastIndex)
                node.Parents = self.RegexCheck(self.lastIndex)()
                node.body = self.RegexCheck(self.lastIndex)
                currentIndent = self.parseFor(self.lastIndex, Const.SpaceConst)
                for i in range(0, len(self.nodePath),1):
                    if(self.nodePath[i][1] == currentIndent):
                        self.nodePath = self.nodePath[:i+1]
                return node
            
            case 21|22:
                node = LoopControls()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                return node

            case 23 | 24:
                node = SyncOper()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                node.body = self.RegexCheck(self.lastIndex)
                currentIndent = self.parseFor(self.lastIndex, Const.SpaceConst)
                for i in range(0, len(self.nodePath),1):
                    if(self.nodePath[i][1] == currentIndent):
                        self.nodePath = self.nodePath[:i+1]
                return node

            case 25:
                node = SyncOper()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                if(self.nodePath[-1] is []):
                    node.left = self.nodePath.pop()
#                self.nodePath.append(node)
                node.right = self.RegexCheck(self.lastIndex)
                return node

            case 26|27|29|30:
                node = LogicalOper()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                if(self.nodePath[-1] is []):
                    node.left = self.nodePath.pop()
#                self.nodePath.append(node)
                node.right = self.RegexCheck(self.lastIndex)
                return node
            
            case 28:
                node = LogicalOper()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                node.right = self.RegexCheck(self.lastIndex)
                return node

            case 31|32|33|34|35|36:
                node = ComprasionOper()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                if(self.nodePath[-1] is []):
                    node.left = self.nodePath.pop()
#                self.nodePath.append(node)
                node.right = self.RegexCheck(self.lastIndex)
                return node

            case 37|38|39|40|41|42:
                node = BitwiseOper()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                if(self.nodePath[-1] is []):
                    node.left = self.nodePath.pop()
#                self.nodePath.append(node)
                node.right = self.RegexCheck(self.lastIndex)
                return node
                
            case 43|44|45|46|47|48|49:
                node = ArithmaticOper()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                if(self.nodePath[-1] is []):
                    node.left = self.nodePath.pop()
#                self.nodePath.append(node)
                node.right = self.RegexCheck(self.lastIndex)
                return node

            case 50|51|52|53|54|55|56|57|58|59|60|61|81:
                node = AssigmentOper()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                if(self.nodePath[-1] is []):
                    node.left = self.nodePath.pop()
#                self.nodePath.append(node)
                node.right = self.RegexCheck(self.lastIndex)
                return node

            case 62|63:
                node = If()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].group().rindex("(")
                node.condition = self.RegexCheck(self.lastIndex)
                node.body = self.RegexCheck(self.lastIndex)
                currentIndent = self.parseFor(self.lastIndex, Const.SpaceConst)
                for i in range(len(self.nodePath) - 1 , 0 ,-1):
                    if(self.nodePath[i][1] == currentIndent):
                        self.nodePath = self.nodePath[:i+1]
                return node

            case 64:
                node = If()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                node.body = self.RegexCheck()
                currentIndent = self.parseFor(self.lastIndex, Const.SpaceConst)
                for i in range(0, len(self.nodePath),1):
                    if(self.nodePath[i][1] == currentIndent):
                        self.nodePath = self.nodePath[:i+1]
                return node

            case 65:
                node = Function()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                node.name = self.parseFor(self.lastIndex, Variable.Variable)
                
                self.lastIndex += len(node.name.group())
                node.name = node.name.group()

                tupleInd = self.parse(self.lastIndex)
                if(tupleInd[0][0] != 72):
                    raise UnsupportedSyntax()
                node.parameters = self.RegexCheck(self.lastIndex)
                node.body = self.RegexCheck(self.lastIndex)
                currentIndent = self.parseFor(self.lastIndex, Const.SpaceConst)
                for i in range(0, len(self.nodePath),1):
                    if(self.nodePath[i][1] == currentIndent):
                        self.nodePath = self.nodePath[:i+1]
                return node

            case 66:
                node = Function()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]-1
                node.name = parsed[1].group()[:-1]
                node.parameters = self.RegexCheck(self.lastIndex)
                return node
            
            case 67:
                node = Function()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                raise TBIL("TBIL", "Lambda Expression")

            case 68:
                node = Library()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                node.library = self.RegexCheck(self.lastIndex)
                return node

            case 69:
                raise TBIL("TBIL", "From")

            case 70:
                node = Loop()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                node.condition = self.RegexCheck(self.lastIndex)
                self.nodePath.append(node.condition)
                In = self.parseFor(self.lastIndex, LogicalOper.In )
                if(In == None):
                    raise UnsupportedSyntax("",self.lastIndex)
                node.condition = self.RegexCheck(self.lastIndex)
                node.body = self.RegexCheck(self.lastIndex)
                currentIndent = self.parseFor(self.lastIndex, Const.SpaceConst)
                for i in range(0, len(self.nodePath),1):
                    if(self.nodePath[i][1] == currentIndent.span()[1]):
                        self.nodePath = self.nodePath[:i+1]
                        break
                return node

            case 71:
                node = Loop()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]
                node.condition = self.RegexCheck(self.lastIndex)
                node.body = self.RegexCheck(self.lastIndex)
                currentIndent = self.parseFor(self.lastIndex, Const.SpaceConst)
                for i in range(0, len(self.nodePath),1):
                    if(self.nodePath[i][1] == currentIndent):
                        self.nodePath = self.nodePath[:i+1]
                return node
            
            case 72:
                node = Tuple()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]

                next = parsed
                while(next[0][0] != 73):
                    node.items.append( self.RegexCheck(self.lastIndex))
                    next = self.parse(self.lastIndex)
                    while(next[0][0] != 75 and next[0][0] != 73 ):
                        self.nodePath.append(node.items.pop(-1))
                        node.items.append(self.RegexCheck(self.lastIndex))
                        next = self.parse(self.lastIndex)
                            
                    self.lastIndex += next[1].span()[1]

                return node

            case 74:
                node = Tuple()
                node.type = parsed[0][0]
                self.lastIndex += parsed[1].span()[1]

                next = parsed 
                while(next[0][0] != 76):
                    node.items.append( self.RegexCheck(self.lastIndex))
                    next = self.parse(self.lastIndex)
                    while(next[0][0] != 75 and next[0][0] != 76 ):
                        self.nodePath.append(node.items.pop(-1))
                        node.items.append(self.RegexCheck(self.lastIndex))
                        next = self.parse(self.lastIndex)
                    self.lastIndex += next[1].span()[1]

                return node

            case 77:
                raise TBIL("", "Dictionary")


            case 80:
                node = []
                self.lastIndex += parsed[1].span()[1]

                indent = self.parseFor(self.lastIndex, Const.SpaceConst)
                if(indent == None):
                    raise UnsupportedSyntax

                indent = indent.span()[1]

                self.nodePath.append( ( node, indent ) )
                line = Const()
                while(line != None):
                    currentIndent = self.parseFor(self.lastIndex, Const.SpaceConst)
                    if(currentIndent.span()[1] != indent):
                        return node

                    self.lastIndex += currentIndent.span()[1]

                    while( line != None and line.type != 6 ):
                        line = self.RegexCheck(self.lastIndex)
                        self.nodePath.append(line)
                    line = Const()
                    self.nodePath.pop()
                    node.append(self.nodePath.pop())
                    
                return node

            case 82:
                node = Variable()
                node.name = parsed[1].group()[:parsed[1].group().rindex("[")]
                self.lastIndex += parsed[1].group().rindex("[") 
                node.array = self.RegexCheck(self.lastIndex)
                return node

            case _:
                raise SomethingWrong(self.lastIndex)

        return None

class UnsupportedSyntax(Exception):
    def __init__(self, msg = "Syntax wrong at: Anywhere in code") -> None:
        self.msg = msg

    def __init__(self, msg , char) -> None:
        self.msg = "Syntax wrong at: " + str(char) 
    def __str__(self) -> str:
        return str(self.msg)

class TBIL(Exception):
    def __init__(self, msg = "TBIL") -> None:
        self.msg = msg

    def __init__(self, msg , char) -> None:
        self.msg = "TBIL" + str(char) 
    def __str__(self) -> str:
        return str(self.msg)


class SomethingWrong(Exception):
    def __init__(self, msg = "Something Wrong At: ") -> None:
        self.msg = msg

    def __init__(self, msg , char) -> None:
        self.msg = "Something Wrong At: " + str(char) 
    def __str__(self) -> str:
        return str(self.msg)


if(__name__ == "__main__"):
    a = ast(examples.ex2)
    a.start()
    print("sadldsajlksad")
