# Generated from arithmetic.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("C\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4#\n\4\f\4\16\4&\13\4")
        buf.write("\3\4\5\4)\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4")
        buf.write("\64\n\4\f\4\16\4\67\13\4\3\5\3\5\5\5;\n\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\b\2\3\6\t\2\4\6\b\n\f\16\2\5\3\2\7\b\3")
        buf.write("\2\t\n\3\2\13\r\2B\2\23\3\2\2\2\4\30\3\2\2\2\6(\3\2\2")
        buf.write("\2\b:\3\2\2\2\n<\3\2\2\2\f>\3\2\2\2\16@\3\2\2\2\20\22")
        buf.write("\5\4\3\2\21\20\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2\23")
        buf.write("\24\3\2\2\2\24\26\3\2\2\2\25\23\3\2\2\2\26\27\7\2\2\3")
        buf.write("\27\3\3\2\2\2\30\31\5\6\4\2\31\32\5\16\b\2\32\33\5\6\4")
        buf.write("\2\33\5\3\2\2\2\34\35\b\4\1\2\35\36\7\5\2\2\36\37\5\6")
        buf.write("\4\2\37 \7\6\2\2 )\3\2\2\2!#\t\2\2\2\"!\3\2\2\2#&\3\2")
        buf.write("\2\2$\"\3\2\2\2$%\3\2\2\2%\'\3\2\2\2&$\3\2\2\2\')\5\b")
        buf.write("\5\2(\34\3\2\2\2($\3\2\2\2)\65\3\2\2\2*+\f\7\2\2+,\7\17")
        buf.write("\2\2,\64\5\6\4\b-.\f\6\2\2./\t\3\2\2/\64\5\6\4\7\60\61")
        buf.write("\f\5\2\2\61\62\t\2\2\2\62\64\5\6\4\6\63*\3\2\2\2\63-\3")
        buf.write("\2\2\2\63\60\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2\65\66")
        buf.write("\3\2\2\2\66\7\3\2\2\2\67\65\3\2\2\28;\5\n\6\29;\5\f\7")
        buf.write("\2:8\3\2\2\2:9\3\2\2\2;\t\3\2\2\2<=\7\4\2\2=\13\3\2\2")
        buf.write("\2>?\7\3\2\2?\r\3\2\2\2@A\t\4\2\2A\17\3\2\2\2\b\23$(\63")
        buf.write("\65:")
        return buf.getvalue()


class arithmeticParser ( Parser ):

    grammarFileName = "arithmetic.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'='", "'.'", 
                     "'^'" ]

    symbolicNames = [ "<INVALID>", "VARIABLE", "SCIENTIFIC_NUMBER", "LPAREN", 
                      "RPAREN", "PLUS", "MINUS", "TIMES", "DIV", "GT", "LT", 
                      "EQ", "POINT", "POW", "WS" ]

    RULE_file = 0
    RULE_equation = 1
    RULE_expression = 2
    RULE_atom = 3
    RULE_scientific = 4
    RULE_variable = 5
    RULE_relop = 6

    ruleNames =  [ "file", "equation", "expression", "atom", "scientific", 
                   "variable", "relop" ]

    EOF = Token.EOF
    VARIABLE=1
    SCIENTIFIC_NUMBER=2
    LPAREN=3
    RPAREN=4
    PLUS=5
    MINUS=6
    TIMES=7
    DIV=8
    GT=9
    LT=10
    EQ=11
    POINT=12
    POW=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(arithmeticParser.EOF, 0)

        def equation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(arithmeticParser.EquationContext)
            else:
                return self.getTypedRuleContext(arithmeticParser.EquationContext,i)


        def getRuleIndex(self):
            return arithmeticParser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)




    def file(self):

        localctx = arithmeticParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << arithmeticParser.VARIABLE) | (1 << arithmeticParser.SCIENTIFIC_NUMBER) | (1 << arithmeticParser.LPAREN) | (1 << arithmeticParser.PLUS) | (1 << arithmeticParser.MINUS))) != 0):
                self.state = 14
                self.equation()
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(arithmeticParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EquationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(arithmeticParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(arithmeticParser.ExpressionContext,i)


        def relop(self):
            return self.getTypedRuleContext(arithmeticParser.RelopContext,0)


        def getRuleIndex(self):
            return arithmeticParser.RULE_equation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquation" ):
                listener.enterEquation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquation" ):
                listener.exitEquation(self)




    def equation(self):

        localctx = arithmeticParser.EquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_equation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.expression(0)
            self.state = 23
            self.relop()
            self.state = 24
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(arithmeticParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(arithmeticParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(arithmeticParser.ExpressionContext,i)


        def RPAREN(self):
            return self.getToken(arithmeticParser.RPAREN, 0)

        def atom(self):
            return self.getTypedRuleContext(arithmeticParser.AtomContext,0)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(arithmeticParser.PLUS)
            else:
                return self.getToken(arithmeticParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(arithmeticParser.MINUS)
            else:
                return self.getToken(arithmeticParser.MINUS, i)

        def POW(self):
            return self.getToken(arithmeticParser.POW, 0)

        def TIMES(self):
            return self.getToken(arithmeticParser.TIMES, 0)

        def DIV(self):
            return self.getToken(arithmeticParser.DIV, 0)

        def getRuleIndex(self):
            return arithmeticParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = arithmeticParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [arithmeticParser.LPAREN]:
                self.state = 27
                self.match(arithmeticParser.LPAREN)
                self.state = 28
                self.expression(0)
                self.state = 29
                self.match(arithmeticParser.RPAREN)
                pass
            elif token in [arithmeticParser.VARIABLE, arithmeticParser.SCIENTIFIC_NUMBER, arithmeticParser.PLUS, arithmeticParser.MINUS]:
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==arithmeticParser.PLUS or _la==arithmeticParser.MINUS:
                    self.state = 31
                    _la = self._input.LA(1)
                    if not(_la==arithmeticParser.PLUS or _la==arithmeticParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 36
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 37
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 51
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 49
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = arithmeticParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 40
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 41
                        self.match(arithmeticParser.POW)
                        self.state = 42
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = arithmeticParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 43
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 44
                        _la = self._input.LA(1)
                        if not(_la==arithmeticParser.TIMES or _la==arithmeticParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 45
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = arithmeticParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 46
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 47
                        _la = self._input.LA(1)
                        if not(_la==arithmeticParser.PLUS or _la==arithmeticParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 48
                        self.expression(4)
                        pass

             
                self.state = 53
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scientific(self):
            return self.getTypedRuleContext(arithmeticParser.ScientificContext,0)


        def variable(self):
            return self.getTypedRuleContext(arithmeticParser.VariableContext,0)


        def getRuleIndex(self):
            return arithmeticParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = arithmeticParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_atom)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [arithmeticParser.SCIENTIFIC_NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.scientific()
                pass
            elif token in [arithmeticParser.VARIABLE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.variable()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScientificContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCIENTIFIC_NUMBER(self):
            return self.getToken(arithmeticParser.SCIENTIFIC_NUMBER, 0)

        def getRuleIndex(self):
            return arithmeticParser.RULE_scientific

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScientific" ):
                listener.enterScientific(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScientific" ):
                listener.exitScientific(self)




    def scientific(self):

        localctx = arithmeticParser.ScientificContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_scientific)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(arithmeticParser.SCIENTIFIC_NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(arithmeticParser.VARIABLE, 0)

        def getRuleIndex(self):
            return arithmeticParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = arithmeticParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(arithmeticParser.VARIABLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelopContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(arithmeticParser.EQ, 0)

        def GT(self):
            return self.getToken(arithmeticParser.GT, 0)

        def LT(self):
            return self.getToken(arithmeticParser.LT, 0)

        def getRuleIndex(self):
            return arithmeticParser.RULE_relop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelop" ):
                listener.enterRelop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelop" ):
                listener.exitRelop(self)




    def relop(self):

        localctx = arithmeticParser.RelopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_relop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << arithmeticParser.GT) | (1 << arithmeticParser.LT) | (1 << arithmeticParser.EQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




