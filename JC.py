# -*- coding: utf-8 -*-
from lark import Lark, Transformer
import unittest
# ↓ グローバル変数としてここに書く！
classes = {}
current_class = None
call_count = {}
vars_array = {}  # ← これを追加！
# 文法定義
parser = Lark('''
    start: stat+

    stat: class_def
        | func_def
        | assign ";"?
        | expr ";"?

    class_def: "class" NAME "{" class_body "}"
    class_body: (assign ";"? | func_def)*

    func_def: "func" NAME "(" ")" "{" stat* "}"
    assign: NAME "=" expr

    # if文を追加
    if_stat: "if" "(" expr ")" "{" stat* "}"
           | "if" "(" expr ")" "{" stat* "}" "else" "{" stat* "}"

    expr: expr "+" expr        -> add
        | expr "-" expr        -> sub
        | expr "*" expr        -> mul
        | expr "==" expr       -> eq
        | expr "<" expr        -> lt
        | expr ">" expr        -> gt
        | NAME ("." NAME)+     -> method_call
        | NUMBER               -> number
        | NAME                 -> var

    NAME: /[a-zA-Z][a-zA-Z0-9_]*/
    NUMBER: /[0-9]+/
%import common.WS
%ignore WS
''', parser='earley')

# クラス情報を保存する辞書
classes = {}
current_class = None

class MyLang(Transformer):

# クラス定義
    def class_def(self, items):
        global current_class
        name = str(items[0])
        body = items[1]
    
        methods = {}
        vars = {}
    
        # Treeのまま来た時の処理！
        for item in body.children:
            if hasattr(item, 'data') and item.data == 'func_def':
                func_name = str(item.children[0])
                stats = list(item.children[1:])
                methods[func_name] = {"params": [], "body": stats}
            elif isinstance(item, dict) and "method" in item:
                methods.update(item["method"])
    
        classes[name] = {"vars": vars, "methods": methods, "children": {}}
        current_class = None

    # クラスの中身
def class_body(self, items):
    methods = {}
    vars = {}
    for item in items:
        # Treeのまま来た時の処理を追加！
        if hasattr(item, 'data') and item.data == 'func_def':
            name = str(item.children[0])
            stats = list(item.children[1:])
            methods[name] = {"params": [], "body": stats}
        elif isinstance(item, dict) and "method" in item:
            methods.update(item["method"])
        elif isinstance(item, dict) and "assign" in item:
            vars.update(item["assign"])
    return {"vars": vars, "methods": methods, "children": {}}


    def assign(self, items):
        return {"assign": {str(items[0]): items[1]}}

    def string(self, items):
        # "apple" → apple（クォートを外す）
        return str(items[0])[1:-1]

    def number(self, items):
        return int(items[0])

def if_stat(self, items):
    condition = items[0]
    if condition:
        for stat in items[1:]:
            if isinstance(stat, dict) and "assign" in stat:
                for var_name, value in stat["assign"].items():
                    if var_name not in vars_array:
                        vars_array[var_name] = []
                    vars_array[var_name].append(value)
                    # ↓ current_classを使って取得する！
                    classes[current_class]["vars"][var_name] = value
            else:
                print(stat)# ← printでいいのはここだけ！
    # メソッド呼び出し
    def method_call(self, items):
        names = [str(item) for item in items]
    
        method_name = names[-1]
        class_path = names[:-1]
    
        current = classes
        for i, name in enumerate(class_path):
            if i == 0:
                if name not in current:
                   raise Exception(f"クラス{name}が見つからない")
                current = current[name]
            else:
                if name not in current["children"]:
                    raise Exception(f"子クラス{name}が見つからない")
                current = current["children"][name]
    
        if method_name not in current["methods"]:
            raise Exception(f"メソッド{method_name}が見つからない")
    
        # bodyを取り出す！
        body = current["methods"][method_name].get("body", [])
    
        for stat in body:
            if isinstance(stat, dict) and "assign" in stat:
                for var_name, value in stat["assign"].items():
                    # vars_arrayにも追加！
                    if var_name not in vars_array:
                        vars_array[var_name] = []
                    vars_array[var_name].append(value)
                    current["vars"][var_name] = value
            else:
                print(stat)



    # 関数定義
    def func_def(self, items):
        name = str(items[0])
        stats = list(items[1:])
        # paramsとbodyを分けて返す！
        return {"method": {name: {"params": [], "body": stats}}}
    
    # 代入文
    def assign(self, items):
        return {"assign": {str(items[0]): items[1]}}

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

def add(self, items): return items[0] + items[1]
def sub(self, items): return items[0] - items[1]
def mul(self, items): return items[0] * items[1]
def number(self, items): return int(items[0])
#    def var(self, items): return str(items[0])
def var(self, items):
    name = str(items[0])
    if current_class and name in classes[current_class]["vars"]:
        return classes[current_class]["vars"][name]
    return name #追加した
def run_func(func_name, args=[], depth=0):
    if depth > 1000:
        raise Exception("再帰が深すぎる！")

    cls = classes[current_class]
    if func_name not in cls["methods"]:
        raise Exception(f"関数{func_name}が見つからない")    
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
    
    for stat in body:
        # Treeのままのstatとassignをここでさばく！
        for node in stat.children:
            if hasattr(node, 'data') and node.data == 'assign':
                var_name = str(node.children[0])
                # numberの処理
                value_node = node.children[1]
                if hasattr(value_node, 'data') and value_node.data == 'number':
                    value = int(value_node.children[0])
                else:
                    value = str(value_node)
                
                if var_name not in vars_array:
                    vars_array[var_name] = []
                vars_array[var_name].append(value)
                cls["vars"][var_name] = value
    
    call_count[method_name] += 1

#---

## テストコード
#```
code = '''
    class MyClass {
        func add() {
            x = 100;
        }
    }
    '''
tree = parser.parse(code)
MyLang().transform(tree)

# ここで確認！
print("classes:", classes)
# おそらく {} になってるはず
print(tree.pretty())
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
        func add() {
                x = 100;
            }
        }
        '''
        tree = parser.parse(code)
        print("tree:", tree.pretty())  # ← 追加！
        MyLang().transform(tree)
        print("classes:", classes)     # ← 追加！
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

#  こう呼ぶ！
if __name__ == "__main__":
    unittest.main()
