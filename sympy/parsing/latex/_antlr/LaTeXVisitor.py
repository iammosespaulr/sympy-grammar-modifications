# Generated from LaTeX.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LaTeXParser import LaTeXParser
else:
    from LaTeXParser import LaTeXParser

# This class defines a complete generic visitor for a parse tree produced by LaTeXParser.

class LaTeXVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LaTeXParser#prog.
    def visitProg(self, ctx:LaTeXParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#trig_functions_.
    def visitTrig_functions_(self, ctx:LaTeXParser.Trig_functions_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#frac_.
    def visitFrac_(self, ctx:LaTeXParser.Frac_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#common_functions_.
    def visitCommon_functions_(self, ctx:LaTeXParser.Common_functions_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#aaaa.
    def visitAaaa(self, ctx:LaTeXParser.AaaaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#add_sub.
    def visitAdd_sub(self, ctx:LaTeXParser.Add_subContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#begin_eq_.
    def visitBegin_eq_(self, ctx:LaTeXParser.Begin_eq_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#l_paren_.
    def visitL_paren_(self, ctx:LaTeXParser.L_paren_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#sss.
    def visitSss(self, ctx:LaTeXParser.SssContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#being_eqnarray.
    def visitBeing_eqnarray(self, ctx:LaTeXParser.Being_eqnarrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#number_.
    def visitNumber_(self, ctx:LaTeXParser.Number_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#underscore_.
    def visitUnderscore_(self, ctx:LaTeXParser.Underscore_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#array.
    def visitArray(self, ctx:LaTeXParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#relation_operators_.
    def visitRelation_operators_(self, ctx:LaTeXParser.Relation_operators_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#symbols_.
    def visitSymbols_(self, ctx:LaTeXParser.Symbols_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#sssss.
    def visitSssss(self, ctx:LaTeXParser.SssssContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#vector.
    def visitVector(self, ctx:LaTeXParser.VectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#mul_div.
    def visitMul_div(self, ctx:LaTeXParser.Mul_divContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#begin_split_.
    def visitBegin_split_(self, ctx:LaTeXParser.Begin_split_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#exponent.
    def visitExponent(self, ctx:LaTeXParser.ExponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#array_1_d.
    def visitArray_1_d(self, ctx:LaTeXParser.Array_1_dContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#maybe_common.
    def visitMaybe_common(self, ctx:LaTeXParser.Maybe_commonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#common_functions.
    def visitCommon_functions(self, ctx:LaTeXParser.Common_functionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#frac.
    def visitFrac(self, ctx:LaTeXParser.FracContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#integer.
    def visitInteger(self, ctx:LaTeXParser.IntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#float.
    def visitFloat(self, ctx:LaTeXParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#prime.
    def visitPrime(self, ctx:LaTeXParser.PrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#relation_operators.
    def visitRelation_operators(self, ctx:LaTeXParser.Relation_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#maybe_remove.
    def visitMaybe_remove(self, ctx:LaTeXParser.Maybe_removeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaTeXParser#symbols.
    def visitSymbols(self, ctx:LaTeXParser.SymbolsContext):
        return self.visitChildren(ctx)



del LaTeXParser