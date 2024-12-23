'''
Carolina Pacheco da Silva
Matheus Antunes Monteiro
Matheus Beilfuss
'''

PARSING_TABLE = {('S', '$'): ['MAIN'],
 ('S', 'def'): ['MAIN'],
 ('S', '{'): ['MAIN'],
 ('S', 'int'): ['MAIN'],
 ('S', 'id'): ['MAIN'],
 ('S', ';'): ['MAIN'],
 ('S', 'print'): ['MAIN'],
 ('S', 'return'): ['MAIN'],
 ('S', 'if'): ['MAIN'],
 ('MAIN', '$'): [],
 ('MAIN', 'def'): ['FLIST'],
 ('MAIN', '{'): ['STMT'],
 ('MAIN', 'int'): ['STMT'],
 ('MAIN', 'id'): ['STMT'],
 ('MAIN', ';'): ['STMT'],
 ('MAIN', 'print'): ['STMT'],
 ('MAIN', 'return'): ['STMT'],
 ('MAIN', 'if'): ['STMT'],
 ('FLIST', 'def'): ['FDEF', 'FLIST’'],
 ('FLIST’', '$'): [],
 ('FLIST’', 'def'): ['FLIST'],
 ('FDEF', 'def'): ['def', 'id(', 'PARLIST', ')', '{', 'STMTLIST', '}'],
 ('PARLIST', ')'): [],
 ('PARLIST', 'int'): ['int', 'id', 'PARLIST’'],
 ('PARLIST’', ')'): [],
 ('PARLIST’', ','): [',', 'PARLIST'],
 ('VARLIST', 'id'): ['id', 'VARLIST’'],
 ('VARLIST’', ','): [',', 'VARLIST'],
 ('VARLIST’', ';'): [],
 ('STMT', '{'): ['{', 'STMTLIST', '}'],
 ('STMT', 'int'): ['int', 'VARLIST', ';'],
 ('STMT', 'id'): ['ATRIBST', ';'],
 ('STMT', ';'): [';'],
 ('STMT', 'print'): ['PRINTST', ';'],
 ('STMT', 'return'): ['RETURNST', ';'],
 ('STMT', 'if'): ['IFSTMT'],
 ('ATRIBST', 'id'): ['id', ':=', 'ATRIBST’'],
 ('ATRIBST’', 'id('): ['FCALL'],
 ('ATRIBST’', 'id'): ['EXPR'],
 ('ATRIBST’', '('): ['EXPR'],
 ('ATRIBST’', 'num'): ['EXPR'],
 ('FCALL', 'id('): ['id(', 'PARLISTCALL', ')'],
 ('PARLISTCALL', ')'): [],
 ('PARLISTCALL', 'id'): ['id', 'PARLISTCALL’'],
 ('PARLISTCALL’', ')'): [],
 ('PARLISTCALL’', ','): [',', 'PARLISTCALL'],
 ('PRINTST', 'print'): ['print', 'EXPR'],
 ('RETURNST', 'return'): ['return', 'RETURNST’'],
 ('RETURNST’', 'id'): ['id'],
 ('RETURNST’', ';'): [],
 ('IFSTMT', 'if'): ['if', '(', 'EXPR', ')', '{', 'STMTLIST', '}', 'ELSEPART'],
 ('ELSEPART', '$'): [],
 ('ELSEPART', '{'): [],
 ('ELSEPART', '}'): [],
 ('ELSEPART', 'int'): [],
 ('ELSEPART', 'id'): [],
 ('ELSEPART', ';'): [],
 ('ELSEPART', 'print'): [],
 ('ELSEPART', 'return'): [],
 ('ELSEPART', 'if'): [],
 ('ELSEPART', 'else'): ['else', '{','STMTLIST', '}'],
 ('STMTLIST', '{'): ['STMT', 'STMTLIST’'],
 ('STMTLIST', 'int'): ['STMT', 'STMTLIST’'],
 ('STMTLIST', 'id'): ['STMT', 'STMTLIST’'],
 ('STMTLIST', ';'): ['STMT', 'STMTLIST’'],
 ('STMTLIST', 'print'): ['STMT', 'STMTLIST’'],
 ('STMTLIST', 'return'): ['STMT', 'STMTLIST’'],
 ('STMTLIST', 'if'): ['STMT', 'STMTLIST’'],
 ('STMTLIST’', '{'): ['STMTLIST'],
 ('STMTLIST’', '}'): [],
 ('STMTLIST’', 'int'): ['STMTLIST'],
 ('STMTLIST’', 'id'): ['STMTLIST'],
 ('STMTLIST’', ';'): ['STMTLIST'],
 ('STMTLIST’', 'print'): ['STMTLIST'],
 ('STMTLIST’', 'return'): ['STMTLIST'],
 ('STMTLIST’', 'if'): ['STMTLIST'],
 ('EXPR', 'id'): ['NUMEXPR', 'EXPR’'],
 ('EXPR', '('): ['NUMEXPR', 'EXPR’'],
 ('EXPR', 'num'): ['NUMEXPR', 'EXPR’'],
 ('EXPR’', ')'): [],
 ('EXPR’', ';'): [],
 ('EXPR’', '<'): ['<', 'NUMEXPR'],
 ('EXPR’', '<='): ['<=', 'NUMEXPR'],
 ('EXPR’', '>'): ['>', 'NUMEXPR'],
 ('EXPR’', '>='): ['>=', 'NUMEXPR'],
 ('EXPR’', '=='): ['==', 'NUMEXPR'],
 ('EXPR’', '<>'): ['<>', 'NUMEXPR'],
 ('NUMEXPR', 'id'): ['TERM', 'NUMEXPR′'],
 ('NUMEXPR', '('): ['TERM', 'NUMEXPR′'],
 ('NUMEXPR', 'num'): ['TERM', 'NUMEXPR′'],
 ('NUMEXPR′', ')'): [],
 ('NUMEXPR′', ';'): [],
 ('NUMEXPR′', '<'): [],
 ('NUMEXPR′', '<='): [],
 ('NUMEXPR′', '>'): [],
 ('NUMEXPR′', '>='): [],
 ('NUMEXPR′', '=='): [],
 ('NUMEXPR′', '<>'): [],
 ('NUMEXPR′', '+'): ['+', 'TERM', 'NUMEXPR′'],
 ('NUMEXPR′', '-'): ['-', 'TERM', 'NUMEXPR′'],
 ('TERM', 'id'): ['FACTOR', 'TERM′'],
 ('TERM', '('): ['FACTOR', 'TERM′'],
 ('TERM', 'num'): ['FACTOR', 'TERM′'],
 ('TERM′', ')'): [],
 ('TERM′', ';'): [],
 ('TERM′', '<'): [],
 ('TERM′', '<='): [],
 ('TERM′', '>'): [],
 ('TERM′', '>='): [],
 ('TERM′', '=='): [],
 ('TERM′', '<>'): [],
 ('TERM′', '+'): [],
 ('TERM′', '-'): [],
 ('TERM′', '*'): ['*', 'FACTOR', 'TERM′'],
 ('TERM′', '/'): ['/', 'FACTOR', 'TERM′'],
 ('FACTOR', 'id'): ['id'],
 ('FACTOR', '('): ['(', 'NUMEXPR', ')'],
 ('FACTOR', 'num'): ['num']}