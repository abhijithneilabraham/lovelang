# Generated from pythongrammar.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .pythongrammarParser import pythongrammarParser
else:
    from pythongrammarParser import pythongrammarParser

# This class defines a complete listener for a parse tree produced by pythongrammarParser.
class pythongrammarListener(ParseTreeListener):

    # Enter a parse tree produced by pythongrammarParser#single_input.
    def enterSingle_input(self, ctx:pythongrammarParser.Single_inputContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#single_input.
    def exitSingle_input(self, ctx:pythongrammarParser.Single_inputContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#file_input.
    def enterFile_input(self, ctx:pythongrammarParser.File_inputContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#file_input.
    def exitFile_input(self, ctx:pythongrammarParser.File_inputContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#eval_input.
    def enterEval_input(self, ctx:pythongrammarParser.Eval_inputContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#eval_input.
    def exitEval_input(self, ctx:pythongrammarParser.Eval_inputContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#decorator.
    def enterDecorator(self, ctx:pythongrammarParser.DecoratorContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#decorator.
    def exitDecorator(self, ctx:pythongrammarParser.DecoratorContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#decorators.
    def enterDecorators(self, ctx:pythongrammarParser.DecoratorsContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#decorators.
    def exitDecorators(self, ctx:pythongrammarParser.DecoratorsContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#decorated.
    def enterDecorated(self, ctx:pythongrammarParser.DecoratedContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#decorated.
    def exitDecorated(self, ctx:pythongrammarParser.DecoratedContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#async_funcdef.
    def enterAsync_funcdef(self, ctx:pythongrammarParser.Async_funcdefContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#async_funcdef.
    def exitAsync_funcdef(self, ctx:pythongrammarParser.Async_funcdefContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#funcdef.
    def enterFuncdef(self, ctx:pythongrammarParser.FuncdefContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#funcdef.
    def exitFuncdef(self, ctx:pythongrammarParser.FuncdefContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#parameters.
    def enterParameters(self, ctx:pythongrammarParser.ParametersContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#parameters.
    def exitParameters(self, ctx:pythongrammarParser.ParametersContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#typedargslist.
    def enterTypedargslist(self, ctx:pythongrammarParser.TypedargslistContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#typedargslist.
    def exitTypedargslist(self, ctx:pythongrammarParser.TypedargslistContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#tfpdef.
    def enterTfpdef(self, ctx:pythongrammarParser.TfpdefContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#tfpdef.
    def exitTfpdef(self, ctx:pythongrammarParser.TfpdefContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#varargslist.
    def enterVarargslist(self, ctx:pythongrammarParser.VarargslistContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#varargslist.
    def exitVarargslist(self, ctx:pythongrammarParser.VarargslistContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#vfpdef.
    def enterVfpdef(self, ctx:pythongrammarParser.VfpdefContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#vfpdef.
    def exitVfpdef(self, ctx:pythongrammarParser.VfpdefContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#stmt.
    def enterStmt(self, ctx:pythongrammarParser.StmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#stmt.
    def exitStmt(self, ctx:pythongrammarParser.StmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#simple_stmt.
    def enterSimple_stmt(self, ctx:pythongrammarParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#simple_stmt.
    def exitSimple_stmt(self, ctx:pythongrammarParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#small_stmt.
    def enterSmall_stmt(self, ctx:pythongrammarParser.Small_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#small_stmt.
    def exitSmall_stmt(self, ctx:pythongrammarParser.Small_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#expr_stmt.
    def enterExpr_stmt(self, ctx:pythongrammarParser.Expr_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#expr_stmt.
    def exitExpr_stmt(self, ctx:pythongrammarParser.Expr_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#annassign.
    def enterAnnassign(self, ctx:pythongrammarParser.AnnassignContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#annassign.
    def exitAnnassign(self, ctx:pythongrammarParser.AnnassignContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#testlist_star_expr.
    def enterTestlist_star_expr(self, ctx:pythongrammarParser.Testlist_star_exprContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#testlist_star_expr.
    def exitTestlist_star_expr(self, ctx:pythongrammarParser.Testlist_star_exprContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#augassign.
    def enterAugassign(self, ctx:pythongrammarParser.AugassignContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#augassign.
    def exitAugassign(self, ctx:pythongrammarParser.AugassignContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#del_stmt.
    def enterDel_stmt(self, ctx:pythongrammarParser.Del_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#del_stmt.
    def exitDel_stmt(self, ctx:pythongrammarParser.Del_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#pass_stmt.
    def enterPass_stmt(self, ctx:pythongrammarParser.Pass_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#pass_stmt.
    def exitPass_stmt(self, ctx:pythongrammarParser.Pass_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#flow_stmt.
    def enterFlow_stmt(self, ctx:pythongrammarParser.Flow_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#flow_stmt.
    def exitFlow_stmt(self, ctx:pythongrammarParser.Flow_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#break_stmt.
    def enterBreak_stmt(self, ctx:pythongrammarParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#break_stmt.
    def exitBreak_stmt(self, ctx:pythongrammarParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#continue_stmt.
    def enterContinue_stmt(self, ctx:pythongrammarParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#continue_stmt.
    def exitContinue_stmt(self, ctx:pythongrammarParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#return_stmt.
    def enterReturn_stmt(self, ctx:pythongrammarParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#return_stmt.
    def exitReturn_stmt(self, ctx:pythongrammarParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#yield_stmt.
    def enterYield_stmt(self, ctx:pythongrammarParser.Yield_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#yield_stmt.
    def exitYield_stmt(self, ctx:pythongrammarParser.Yield_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#raise_stmt.
    def enterRaise_stmt(self, ctx:pythongrammarParser.Raise_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#raise_stmt.
    def exitRaise_stmt(self, ctx:pythongrammarParser.Raise_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#import_stmt.
    def enterImport_stmt(self, ctx:pythongrammarParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#import_stmt.
    def exitImport_stmt(self, ctx:pythongrammarParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#import_name.
    def enterImport_name(self, ctx:pythongrammarParser.Import_nameContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#import_name.
    def exitImport_name(self, ctx:pythongrammarParser.Import_nameContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#import_from.
    def enterImport_from(self, ctx:pythongrammarParser.Import_fromContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#import_from.
    def exitImport_from(self, ctx:pythongrammarParser.Import_fromContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#import_as_name.
    def enterImport_as_name(self, ctx:pythongrammarParser.Import_as_nameContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#import_as_name.
    def exitImport_as_name(self, ctx:pythongrammarParser.Import_as_nameContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#dotted_as_name.
    def enterDotted_as_name(self, ctx:pythongrammarParser.Dotted_as_nameContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#dotted_as_name.
    def exitDotted_as_name(self, ctx:pythongrammarParser.Dotted_as_nameContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#import_as_names.
    def enterImport_as_names(self, ctx:pythongrammarParser.Import_as_namesContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#import_as_names.
    def exitImport_as_names(self, ctx:pythongrammarParser.Import_as_namesContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#dotted_as_names.
    def enterDotted_as_names(self, ctx:pythongrammarParser.Dotted_as_namesContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#dotted_as_names.
    def exitDotted_as_names(self, ctx:pythongrammarParser.Dotted_as_namesContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#dotted_name.
    def enterDotted_name(self, ctx:pythongrammarParser.Dotted_nameContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#dotted_name.
    def exitDotted_name(self, ctx:pythongrammarParser.Dotted_nameContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#global_stmt.
    def enterGlobal_stmt(self, ctx:pythongrammarParser.Global_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#global_stmt.
    def exitGlobal_stmt(self, ctx:pythongrammarParser.Global_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#nonlocal_stmt.
    def enterNonlocal_stmt(self, ctx:pythongrammarParser.Nonlocal_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#nonlocal_stmt.
    def exitNonlocal_stmt(self, ctx:pythongrammarParser.Nonlocal_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#assert_stmt.
    def enterAssert_stmt(self, ctx:pythongrammarParser.Assert_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#assert_stmt.
    def exitAssert_stmt(self, ctx:pythongrammarParser.Assert_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#compound_stmt.
    def enterCompound_stmt(self, ctx:pythongrammarParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#compound_stmt.
    def exitCompound_stmt(self, ctx:pythongrammarParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#async_stmt.
    def enterAsync_stmt(self, ctx:pythongrammarParser.Async_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#async_stmt.
    def exitAsync_stmt(self, ctx:pythongrammarParser.Async_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#if_stmt.
    def enterIf_stmt(self, ctx:pythongrammarParser.If_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#if_stmt.
    def exitIf_stmt(self, ctx:pythongrammarParser.If_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#while_stmt.
    def enterWhile_stmt(self, ctx:pythongrammarParser.While_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#while_stmt.
    def exitWhile_stmt(self, ctx:pythongrammarParser.While_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#for_stmt.
    def enterFor_stmt(self, ctx:pythongrammarParser.For_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#for_stmt.
    def exitFor_stmt(self, ctx:pythongrammarParser.For_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#try_stmt.
    def enterTry_stmt(self, ctx:pythongrammarParser.Try_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#try_stmt.
    def exitTry_stmt(self, ctx:pythongrammarParser.Try_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#with_stmt.
    def enterWith_stmt(self, ctx:pythongrammarParser.With_stmtContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#with_stmt.
    def exitWith_stmt(self, ctx:pythongrammarParser.With_stmtContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#with_item.
    def enterWith_item(self, ctx:pythongrammarParser.With_itemContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#with_item.
    def exitWith_item(self, ctx:pythongrammarParser.With_itemContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#except_clause.
    def enterExcept_clause(self, ctx:pythongrammarParser.Except_clauseContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#except_clause.
    def exitExcept_clause(self, ctx:pythongrammarParser.Except_clauseContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#suite.
    def enterSuite(self, ctx:pythongrammarParser.SuiteContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#suite.
    def exitSuite(self, ctx:pythongrammarParser.SuiteContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#test.
    def enterTest(self, ctx:pythongrammarParser.TestContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#test.
    def exitTest(self, ctx:pythongrammarParser.TestContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#test_nocond.
    def enterTest_nocond(self, ctx:pythongrammarParser.Test_nocondContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#test_nocond.
    def exitTest_nocond(self, ctx:pythongrammarParser.Test_nocondContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#lambdef.
    def enterLambdef(self, ctx:pythongrammarParser.LambdefContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#lambdef.
    def exitLambdef(self, ctx:pythongrammarParser.LambdefContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#lambdef_nocond.
    def enterLambdef_nocond(self, ctx:pythongrammarParser.Lambdef_nocondContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#lambdef_nocond.
    def exitLambdef_nocond(self, ctx:pythongrammarParser.Lambdef_nocondContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#or_test.
    def enterOr_test(self, ctx:pythongrammarParser.Or_testContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#or_test.
    def exitOr_test(self, ctx:pythongrammarParser.Or_testContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#and_test.
    def enterAnd_test(self, ctx:pythongrammarParser.And_testContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#and_test.
    def exitAnd_test(self, ctx:pythongrammarParser.And_testContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#not_test.
    def enterNot_test(self, ctx:pythongrammarParser.Not_testContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#not_test.
    def exitNot_test(self, ctx:pythongrammarParser.Not_testContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#comparison.
    def enterComparison(self, ctx:pythongrammarParser.ComparisonContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#comparison.
    def exitComparison(self, ctx:pythongrammarParser.ComparisonContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#comp_op.
    def enterComp_op(self, ctx:pythongrammarParser.Comp_opContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#comp_op.
    def exitComp_op(self, ctx:pythongrammarParser.Comp_opContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#star_expr.
    def enterStar_expr(self, ctx:pythongrammarParser.Star_exprContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#star_expr.
    def exitStar_expr(self, ctx:pythongrammarParser.Star_exprContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#expr.
    def enterExpr(self, ctx:pythongrammarParser.ExprContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#expr.
    def exitExpr(self, ctx:pythongrammarParser.ExprContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#xor_expr.
    def enterXor_expr(self, ctx:pythongrammarParser.Xor_exprContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#xor_expr.
    def exitXor_expr(self, ctx:pythongrammarParser.Xor_exprContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#and_expr.
    def enterAnd_expr(self, ctx:pythongrammarParser.And_exprContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#and_expr.
    def exitAnd_expr(self, ctx:pythongrammarParser.And_exprContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#shift_expr.
    def enterShift_expr(self, ctx:pythongrammarParser.Shift_exprContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#shift_expr.
    def exitShift_expr(self, ctx:pythongrammarParser.Shift_exprContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#arith_expr.
    def enterArith_expr(self, ctx:pythongrammarParser.Arith_exprContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#arith_expr.
    def exitArith_expr(self, ctx:pythongrammarParser.Arith_exprContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#term.
    def enterTerm(self, ctx:pythongrammarParser.TermContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#term.
    def exitTerm(self, ctx:pythongrammarParser.TermContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#factor.
    def enterFactor(self, ctx:pythongrammarParser.FactorContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#factor.
    def exitFactor(self, ctx:pythongrammarParser.FactorContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#power.
    def enterPower(self, ctx:pythongrammarParser.PowerContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#power.
    def exitPower(self, ctx:pythongrammarParser.PowerContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#atom_expr.
    def enterAtom_expr(self, ctx:pythongrammarParser.Atom_exprContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#atom_expr.
    def exitAtom_expr(self, ctx:pythongrammarParser.Atom_exprContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#atom.
    def enterAtom(self, ctx:pythongrammarParser.AtomContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#atom.
    def exitAtom(self, ctx:pythongrammarParser.AtomContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#testlist_comp.
    def enterTestlist_comp(self, ctx:pythongrammarParser.Testlist_compContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#testlist_comp.
    def exitTestlist_comp(self, ctx:pythongrammarParser.Testlist_compContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#trailer.
    def enterTrailer(self, ctx:pythongrammarParser.TrailerContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#trailer.
    def exitTrailer(self, ctx:pythongrammarParser.TrailerContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#subscriptlist.
    def enterSubscriptlist(self, ctx:pythongrammarParser.SubscriptlistContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#subscriptlist.
    def exitSubscriptlist(self, ctx:pythongrammarParser.SubscriptlistContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#subscript.
    def enterSubscript(self, ctx:pythongrammarParser.SubscriptContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#subscript.
    def exitSubscript(self, ctx:pythongrammarParser.SubscriptContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#sliceop.
    def enterSliceop(self, ctx:pythongrammarParser.SliceopContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#sliceop.
    def exitSliceop(self, ctx:pythongrammarParser.SliceopContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#exprlist.
    def enterExprlist(self, ctx:pythongrammarParser.ExprlistContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#exprlist.
    def exitExprlist(self, ctx:pythongrammarParser.ExprlistContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#testlist.
    def enterTestlist(self, ctx:pythongrammarParser.TestlistContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#testlist.
    def exitTestlist(self, ctx:pythongrammarParser.TestlistContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#dictorsetmaker.
    def enterDictorsetmaker(self, ctx:pythongrammarParser.DictorsetmakerContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#dictorsetmaker.
    def exitDictorsetmaker(self, ctx:pythongrammarParser.DictorsetmakerContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#classdef.
    def enterClassdef(self, ctx:pythongrammarParser.ClassdefContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#classdef.
    def exitClassdef(self, ctx:pythongrammarParser.ClassdefContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#arglist.
    def enterArglist(self, ctx:pythongrammarParser.ArglistContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#arglist.
    def exitArglist(self, ctx:pythongrammarParser.ArglistContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#argument.
    def enterArgument(self, ctx:pythongrammarParser.ArgumentContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#argument.
    def exitArgument(self, ctx:pythongrammarParser.ArgumentContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#comp_iter.
    def enterComp_iter(self, ctx:pythongrammarParser.Comp_iterContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#comp_iter.
    def exitComp_iter(self, ctx:pythongrammarParser.Comp_iterContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#comp_for.
    def enterComp_for(self, ctx:pythongrammarParser.Comp_forContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#comp_for.
    def exitComp_for(self, ctx:pythongrammarParser.Comp_forContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#comp_if.
    def enterComp_if(self, ctx:pythongrammarParser.Comp_ifContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#comp_if.
    def exitComp_if(self, ctx:pythongrammarParser.Comp_ifContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#encoding_decl.
    def enterEncoding_decl(self, ctx:pythongrammarParser.Encoding_declContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#encoding_decl.
    def exitEncoding_decl(self, ctx:pythongrammarParser.Encoding_declContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#yield_expr.
    def enterYield_expr(self, ctx:pythongrammarParser.Yield_exprContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#yield_expr.
    def exitYield_expr(self, ctx:pythongrammarParser.Yield_exprContext):
        pass


    # Enter a parse tree produced by pythongrammarParser#yield_arg.
    def enterYield_arg(self, ctx:pythongrammarParser.Yield_argContext):
        pass

    # Exit a parse tree produced by pythongrammarParser#yield_arg.
    def exitYield_arg(self, ctx:pythongrammarParser.Yield_argContext):
        pass


