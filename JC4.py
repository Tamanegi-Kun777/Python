# -*- coding: utf-8 -*-
from lark import Lark, Transformer, Tree, Token
import unittest
# ↓ グローバル変数としてここに書く！
classes = {}
current_class = None
call_count = {}
vars_array = {}  # ← これを追加！
# 文法定義

# -*- coding: utf-8 -*-
from lark import Lark, Transformer, Tree, Token
import unittest
# ↓ グローバル変数としてここに書く！
current_class = None
call_count = {}
vars_array = {}  # ← これを追加！
# 文法定義

parser = Lark('''


    start: stat+

    stat: class_def
        | func_def
        | var_decl
        | func_body

    class_def: "class" NAME "{" class_body "}"
    class_body: (assign ";"? | func_def | var_decl)*
    var_decl: NAME ";"
    func_def: "func" NAME "(" params ")" "{" func_body* "}"
    params: (NAME ("," NAME)*)?
              
    // func_bodyを追加
    func_body: assign ";"?
             | if_stat
             | return_stat ";"?
             | expr ";"?

    assign: NAME "=" expr
    if_stat: "if" expr "{" func_body* "}" ("elif" expr "{" func_body* "}")* ("else" "{" func_body* "}")?
    return_stat: "return" expr

    expr: expr "+" term   -> add
        | expr "-" term   -> sub
        | expr "==" term  -> eq
        | expr "<" term   -> lt
        | expr ">" term   -> gt
        | term

    term: term "*" atom   -> mul
        | atom

    atom: NAME "(" (expr ("," expr)*)? ")" -> func_call
        | NUMBER          -> number
        | NAME            -> var
        | "(" expr ")"    -> paren

    NAME: /(?!(if|elif|else|return)\b)[a-zA-Z][a-zA-Z0-9_]*/
    NUMBER: /[0-9]+/
%import common.WS
%ignore WS
''', parser='lalr')

# クラス情報を保存する辞書
classes = {}
current_class = None






def eval_expr(tree):
    if isinstance(tree, int):
        return tree
    
    if isinstance(tree, str):
        if current_class and tree in classes[current_class]["vars"]:
            return classes[current_class]["vars"][tree]
        if tree in vars_array:
            return vars_array[tree][-1]
        raise Exception(f"変数{tree}が見つからない")
    
    if not hasattr(tree, 'data'):
        return tree
    
    if tree.data == 'number':
        return int(tree.children[0])
    elif tree.data == 'var':
        name = str(tree.children[0])
        if current_class and name in classes[current_class]["vars"]:
            return classes[current_class]["vars"][name]
        if name in vars_array:
            return vars_array[name][-1]
        raise Exception(f"変数{name}が見つからない")
    elif tree.data == 'add':
        return eval_expr(tree.children[0]) + eval_expr(tree.children[1])
    elif tree.data == 'sub':
        return eval_expr(tree.children[0]) - eval_expr(tree.children[1])
    elif tree.data == 'mul':
        return eval_expr(tree.children[0]) * eval_expr(tree.children[1])
    elif tree.data == 'eq':
        return eval_expr(tree.children[0]) == eval_expr(tree.children[1])
    elif tree.data == 'lt':
        return eval_expr(tree.children[0]) < eval_expr(tree.children[1])
    elif tree.data == 'gt':
        return eval_expr(tree.children[0]) > eval_expr(tree.children[1])
    
    # func_callを追加！
    elif tree.data == 'func_call':
        func_name = str(tree.children[0])
        args = [eval_expr(arg) for arg in tree.children[1:]]
        return run_func(func_name, args, depth=0)
    
    elif tree.data in ('expr', 'term', 'atom'):
        return eval_expr(tree.children[0])

class MyLang(Transformer):

# クラス定義
    def params(self, items):
        print("params items:", items)
        return items  # ← [Token('NAME', 'n')]が返るはず！
    def class_def(self, items):
        global current_class
        name = str(items[0])
        body = items[1]
        methods = {}
        vars = {}
        
        # ? bodyがdictの時だけでOK！
        if isinstance(body, dict):
            methods = body.get("methods", {})
            vars = body.get("vars", {})
        
        classes[name] = {"vars": vars, "methods": methods, "children": {}}
        current_class = None
        # Treeのまま来た時の処理！
        #for item in body.children:
        #    if hasattr(item, 'data') and item.data == 'func_def':
        #        func_name = str(item.children[0])
        #        stats = list(item.children[1:])
        #        methods[func_name] = {"params": [], "body": stats}
        #    elif isinstance(item, dict) and "method" in item:
        #        methods.update(item["method"])
        #
        
        
        # クラスの中身
    def class_body(self, items):
        print("class_body 呼ばれた！")
        methods = {}
        vars = {}
        for item in items:
            # Treeのまま来た時の処理を追加！
            if hasattr(item, 'data') and item.data == 'func_def':
                name = str(item.children[0])      # → 'add'や'fib'
                params = item.children[1]         # → paramsのTree！
                body = list(item.children[2:])    # → bodyだけ！
                param_list = [str(p) for p in params] if isinstance(params, list) else []
                methods[name] = {"params": param_list, "body": body}
            elif isinstance(item, dict) and "method" in item:
                methods.update(item["method"])
            elif isinstance(item, dict) and "assign" in item:
                vars.update(item["assign"])
        return {"vars": vars, "methods": methods, "children": {}}
    def assign(self, items):
        return {"assign": {str(items[0]): eval_expr(items[1])}}
#                                     ↑ eval_exprを追加！

    def string(self, items):
        # "apple" → apple（クォートを外す）
        return str(items[0])[1:-1]

    def number(self, items):
        return int(items[0])

    def if_stat(self, items):
    # Treeのまま返すだけ！
        return Tree(Token('RULE', 'if_stat'), items)
        # メソッド呼び出し
    # return_statを追加して！
    def return_stat(self, items):
        print("return_stat items:", items)
        return Tree(Token('RULE', 'return_stat'), items)
    # ↑ Treeのまま返す！
    # run_funcで処理するよ！
    def func_body(self, items):
        return Tree(Token('RULE', 'func_body'), items)
    def func_def(self, items):
        print("func_def items:", items)  # ← fibのitemsを確認！
        name = str(items[0])
        params = items[1]
        body = list(items[2:])  # ← ここを確認！
        print("func_def body:", body)  # ← 追加して！
    
        # paramsの中身を文字列のリストに変換！
        param_list = [str(p) for p in params] if isinstance(params, list) else []
        #print("func_def name:", name)
        #print("func_def params:", param_list)
    
        return {"method": {name: {"params": param_list, "body": body}}}
    

    # 変数.番号でアクセス
    def indexed_var(self, items):
        global vars_array  # ← これも追加！
        var_name = str(items[0])
        index = int(items[1])

        if var_name not in vars_array:
            raise Exception(f"変数{var_name}が見つからない")
        if index >= len(vars_array[var_name]):
            raise Exception(f"{var_name}.{index}が見つからない")

        return vars_array[var_name][index]

    def number(self, items): return int(items[0])
#    def var(self, items): return str(items[0])
    def var(self, items):
        name = str(items[0])
        return name  # ← 文字列のまま返すだけ！
def run_if_stat(children):
    i = 0
    while i < len(children):
        child = children[i]
        if hasattr(child, 'data') and child.data == 'func_body':
            # elseのfunc_bodyの時！
            for inner in child.children:
                if not hasattr(inner, 'data'):
                    continue
                if inner.data == 'return_stat':
                    return eval_expr(inner.children[0])
                elif inner.data == 'assign':
                    var_name = str(inner.children[0])
                    value = eval_expr(inner.children[1])
                    if var_name not in vars_array:
                        vars_array[var_name] = []
                    vars_array[var_name].append(value)
                elif inner.data == 'if_stat':
                    # ネストしたifを再帰的に処理！
                    result = run_if_stat(inner.children)
                    if result is not None:
                        return result
            i += 1

        elif i + 1 < len(children) and hasattr(children[i+1], 'data') and children[i+1].data == 'func_body':
            # 条件 + func_bodyのペアの時！
            condition = eval_expr(child)
            if condition:
                for inner in children[i+1].children:
                    if not hasattr(inner, 'data'):
                        continue
                    if inner.data == 'return_stat':
                        return eval_expr(inner.children[0])
                    elif inner.data == 'assign':
                        var_name = str(inner.children[0])
                        value = eval_expr(inner.children[1])
                        if var_name not in vars_array:
                            vars_array[var_name] = []
                        vars_array[var_name].append(value)
                    elif inner.data == 'if_stat':
                        # ネストしたifを再帰的に処理！
                        result = run_if_stat(inner.children)

                if result is not None:
                            return result
                i += 2
            else:
                i += 1
    return None
      
def run_method(class_name, method_name):
    global current_class
    current_class = class_name
    cls = classes[class_name]

    if method_name not in cls["methods"]:
        print(f"メソッド{method_name}が見つからない")
        return

    if method_name not in call_count:
        call_count[method_name] = 0

    body = cls["methods"][method_name].get("body", [])
    print("body:", body)  # ← bodyの全体を確認！
    for stat in body:
        print("stat:", stat)    # ← statの中身は？

        # func_bodyの中を処理！
        if hasattr(stat, 'data') and stat.data == 'func_body':
            for node in stat.children:
                # dictで来た時！
                if not hasattr(node, 'data'):
                    continue
                # Treeで来た時！
                if node.data == 'assign':
                    var_name = str(node.children[0])
                    value = eval_expr(node.children[1])
                    if var_name not in vars_array:
                        vars_array[var_name] = []
                    vars_array[var_name].append(value)
                    cls["vars"][var_name] = value
                elif node.data == 'return_stat':
                    return eval_expr(node.children[0])
                elif node.data == 'if_stat':
                    result = run_if_stat(node.children)
                    if result is not None:
                        return result








def run_func(func_name, args=[], depth=0):
    if depth > 1000:
        raise Exception("再帰が深すぎる！")

    # 全classesから探す！
    cls = None
    for class_name, class_data in classes.items():
        if func_name in class_data["methods"]:
            cls = class_data
            break

    if cls is None:
        raise Exception(f"関数{func_name}が見つからない")

    method = cls["methods"][func_name]
    params = method.get("params", [])
    body = method.get("body", [])

    print("func_name:", func_name)
    print("params:", params)
    print("args:", args)
    print("body:", body)

    # 引数をvars_arrayに追加！
    for param, arg in zip(params, args):
        if param not in vars_array:
            vars_array[param] = []
        vars_array[param].append(arg)
    # paramsの中身を表示して確認！
    print("vars_array:", vars_array)
    # bodyを実行！
    result = None
    for stat in body:
        if isinstance(stat, list):  # ← 先にチェック！
            continue
        if isinstance(stat, dict) and "assign" in stat:
            for var_name, value in stat["assign"].items():
                if var_name not in vars_array:
                    vars_array[var_name] = []
                vars_array[var_name].append(value)
        elif not hasattr(stat, 'data'):#stat の中に data という名前の変数や部屋があるか？」を調べます。
            continue
        elif hasattr(stat, 'data') and stat.data == 'func_body':  # ← func_bodyの処理！
            print("func_body.children:", stat.children)  # ← 追加！
            for node in stat.children:
                print("node:", node)  # ← 追加！
                print("node type:", type(node))  # ← 追加！
                if node is None:
                    print("nodeがNoneだよ！")  # ← 追加！
                    continue
                if isinstance(node,dict) and 'assign' in node:
                    for var_name, value in node["assign"].items():
                        if var_name not in vars_array:
                            vars_array[var_name] = []
                        vars_array[var_name].append(value)
                elif not hasattr(node, 'data'):
                    continue
                elif node.data == 'return_stat':
                    return eval_expr(node.children[0])
                elif node.data == 'assign':
                    var_name = str(node.children[0])
                    value = eval_expr(node.children[1])
                    if var_name not in vars_array:
                        vars_array[var_name] = []
                    vars_array[var_name].append(value)
                elif node.data == 'if_stat':
                    children = node.children
                    i = 0
                    while i < len(children):
                        child = children[i]
                        if hasattr(child,'data') and child.data == 'func_body':
                    #elif node.data == 'if_stat':
                            condition = eval_expr(child)
                            if condition:
                                for inner in child.children:
                                    if not hasattr(inner, 'data'):
                                        continue
                                    if inner.data == 'return_stat':
                                        return eval_expr(inner.children[0])
                                    elif inner.data == 'assign':
                                        var_name = str(inner.children[0])
                                        value = eval_expr(inner.children[1])
                                        if var_name not in vars_array:
                                            vars_array[var_name] = []
                                        vars_array[var_name].append(value)
                            i += 1


## テストコード
#```
code = '''
    class MyClass {
        func add() {
            x = 100;
        }
        func fib(n){
            if n==1{
                return 0
            }
            elif n==2{
                return 1
            }
            else{
                return fib(n-1)+fib(n-2)
            }
        }
    }
    '''
tree = parser.parse(code)
result = MyLang().transform(tree)

# ここで確認！
#print("classes:", classes)
# おそらく {} になってるはず
#print(tree.pretty())
a=30

class TestMyLang(unittest.TestCase):
    def setUp(self):
        global vars_array, classes, call_count
        vars_array = {}
        classes = {}
        call_count = {}
    def test_call_count(self):
        code = '''
        class MyClass {
            x;
            func add() {
                x = 100;
            }
            func fib(n){
                if (n==1) {
                    return 0
                }
                elif (n==2) {
                    return 1
                }
                else {
                    return fib(n-1)+fib(n-2)
                }
            }
        }
        '''
        tree = parser.parse(code)
        print("tree:", tree.pretty())  # ← 追加！
        result = MyLang().transform(tree)
        #print("classes:", classes)     # ← 追加！
        print("methods:", classes["MyClass"]["methods"].keys())
    # 3回呼んでるか確認！
        print("1回目")
        run_method("MyClass", "add")
        print("2回目")
        run_method("MyClass", "add")
        print("3回目")
        run_method("MyClass", "add")
    
        print("vars_array:", vars_array)
        self.assertEqual(vars_array["x"], [100, 100, 100])
    
    # 実行後も確認！
        print("vars_array after:", vars_array)
    
        self.assertEqual(vars_array["x"], [100, 100, 100])
        # Pythonのfib()じゃなくてrun_funcで呼ぶ！
        global current_class
        current_class = "MyClass"
        result = run_func("fib", [10], 0)
        print("fib(10):", result)
#  こう呼ぶ！
if __name__ == "__main__":
    unittest.main()

