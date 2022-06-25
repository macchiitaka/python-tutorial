import json
import math
import sys
import time
from functools import wraps
from operator import itemgetter
from typing import Any, Callable, Dict, FrozenSet, Generator, List, Set, Tuple, Union

from package_bar import foo as _foo
from package_bar import print_foo

obj: Dict[str, Union[str, int]] = {"foo": "a", "bar": "b", "baz": 1}

# オブジェクトの属性を表示
print(dir(obj))

# オブジェクトの説明を表示
# help(json)

# 特定メソッドの説明を表示（コードジャンプで事足りる？）
# help(json.load)

# 辞書に in を使うとキーの有無を実行する
print("foo" in obj)

odd_numbers: List[int] = [2, 4, 6]
for num in odd_numbers:
    if num % 2 == 1:
        break
# else 句は for 文の最後に実行される
# ただし break した場合は通らない
# つまり奇数が含まれている場合は実行されない
else:
    print("奇数を含めてください")

while True:
    break
# for else と同じく最後に実行されるが break で抜けた場合は通らない
else:
    print("break せずに while 文を抜けた")  # unreachable code


def get_book(index: int) -> str:
    res: str = ""
    items: List[str] = ["note", "notebook", "sketchbook"]
    try:
        res = items[index]
    # 個別に定義する場合
    except IndexError:
        raise  # raise でエラーを投げる
    except TypeError:
        pass
    # except (IndexError, TypeError) as e:
    #     # () as でエラーをまとめられる
    #     print(f"{e}")
    else:
        # エラーがない場合のみ実行される
        print("該当する書籍があった")
    finally:
        # エラーの有無にかからず必ず実行される
        # クリーンアップ e.g. close() するケースなどで利用
        return res


def walrus_operator(index: int) -> str:
    # book = get_book(index)
    # if book:
    #     return book
    # else:
    #     return "Not Found"

    # 上記と同じ
    if book := get_book(index):
        return book
    else:
        return "Not Found"


# float の最大値/最小値確認
print(sys.float_info)

# 少数誤差を考慮した等価比較
print(0.1 + 0.1 + 0.1 == 0.3)  # False
print(math.isclose(0.1 + 0.1 + 0.1, 0.3))  # True

# () で文字列を囲むとひとつの文字列として解釈される
print(("a" "b" "c"))  # abc

# 文字列の繰り返し
print("a" * 4)  # aaaa

# 文字列をループすると一文字ずつ取り出せる
for char in "abcd👪":
    print(char)

# 文字列を含むか判定
print("cd" in "abcd👪")  # True

title: str = "Python"
# 変数名=
print(f"{title=}")  # title='Python'

# 配列の結合
print([1, 2] + [3, 4])  # [1, 2, 3, 4]

t1: Tuple[int, int, int] = (1, 2, 3)
t2: Tuple[int, int, int] = t1[:]  # タプルをスライス

# 辞書のキーには文字列、数値、タプルなど不変なオブジェクトを利用できる
d: Dict[Union[str, int, Tuple[int, int, int]], int] = {
    "a": 1,
    1: 2,
    (1, 2, 3): 3,
}

# 集合のリテラル表現
set_literal: Set[int] = {1, 2, 3}

# 不変な集合
frozen_set: FrozenSet[int] = frozenset({1, 2, 3})

# リスト内包表記は変数スコープを作成
nums: List[int] = [x for x in range(10)]
# NameError: name 'x' is not defined
# print(x)

# リスト内包表記のネスト
nums2: List[Tuple[int, int]] = [(x, y) for x in range(3) for y in range(3)]
print(nums2)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# 配列のフィルター
nums3_0: List[int] = [x for x in range(3) if x % 2 == 0]
print(nums3_0)  # [0, 2]

# 上記と同義
nums3_1: List[int] = list(filter(lambda x: x % 2 == 0, range(3)))
print(nums3_1)  # [0, 2]

# 集合のリスト内包表記
frozen_set1: FrozenSet[int] = frozenset({x for x in range(10)})

# ジェネレーターのリスト内包表記
gen: Generator[int, Any, None] = (i for i in range(10))


def func() -> str:
    return "func is called"


def func2(func: Callable[[], str]) -> str:
    return func()


print(func2(func))


# 配列引数の展開
def print_books(a: str, b: str, c: str) -> None:
    print(a)
    print(b)
    print(c)


books: List[str] = ["a", "b", "c"]
print_books(*books)

# キーワード引数の展開
books1 = {"a": "1", "b": "2", "c": "3"}
print_books(*books1)
print_books(a=books1["a"], b=books1["b"], c=books1["c"])

# 無名関数
print_book: Callable[[str], None] = lambda x: print(x)

# 型情報は __annotations__ に格納されている
print(print_books.__annotations__)


# クラス
class Foo:
    # _ 始まりは private
    _name: str
    _class_variable: str = "class variable"

    def __init__(self, name: str):
        self._name = name

    # getter
    @property
    def name_property(self) -> str:
        return self._name

    @classmethod
    def print_class_variable(cls) -> None:
        print(cls._class_variable)

    # ただの関数と同じ
    @staticmethod
    def greet() -> None:
        print("Hello")


foo_instance: Foo = Foo("John")
print(isinstance(foo_instance, Foo))  # True

# デコレーターで getter 表現ができる
print(foo_instance.name_property)  # John

# クラス変数
print(Foo._class_variable)

# クラスメソッド
Foo.print_class_variable()
foo_instance.print_class_variable()  # インスタンスからもアクセス可能

# スタティックメソッド
Foo.greet()

# モジュールをスクリプトとして利用したい場合に記述するPythonのイディオム
if __name__ == "__main__":
    print("script")

_foo.print_foo()
print_foo()

print(sys.path)

# グローバル変数一覧
print(globals())


# 変数スコープ
def f1() -> None:
    x: int = 1

    def g():
        # nonlocal 宣言でスコープ外の変数 x を書き換える
        nonlocal x
        x = 2

    g()
    print(x)


def f2() -> None:
    x: int = 1

    def g():
        # f2 の変数 x とは別スコープ
        x: int = 2

    g()
    print(x)


f1()
f2()


# クロージャー
def closure() -> Callable[[], int]:
    i: int = 0

    def increment():
        nonlocal i
        i += 1
        return i

    return increment


increment: Callable[[], int] = closure()
print(increment())  # 1
print(increment())  # 2
print(increment())  # 3

d = {}
print(isinstance(d, dict))  # True
print(issubclass(dict, object))  # True

print(callable(d))  # False
print(callable(closure))  # True
print(callable(closure()))  # True

group_length: int = 4
element_length: int = 3

print(
    list(
        zip(
            *[
                range(i * group_length + 1, (i + 1) * group_length + 1)
                for i in range(element_length)
            ]
        )
    )
)

# 上記と同じ処理
# arr: List[range] = []
# for i in range(element_length):
#     start = i * group_length + 1
#     end = start + group_length
#     arr.append(range(i * group_length + 1, (i + 1) * group_length + 1))
# print(list(zip(*arr)))


numbers = [3, 4, 1, 2]
print(sorted(numbers))  # [1, 2, 3, 4]
print(numbers)  # [3, 4, 1, 2]
print(list(filter(lambda x: x > 2, numbers)))  # [3, 4]
print(list(map(lambda x: x**2, sorted(numbers))))  # [1, 4, 9, 16]

# sorted と itemgetter の組み合わせで辞書の値で並び替えができる
counts: List[Dict[str, Union[int, str]],] = [
    {"word": "python", "count": 3},
    {"word": "practice", "count": 1},
    {"word": "book", "count": 2},
    {"word": "book", "count": 1},
]

print(sorted(counts, key=lambda x: x["count"]))

# 上記と同じ
print(sorted(counts, key=itemgetter("count")))

# count のあとに word で並び替える
print(sorted(counts, key=itemgetter("count", "word")))

print(all([0, 1, 2, 3]))
print(all([1, 2, 3]))
print(all([0]))

print(any([0, 1, 2, 3]))
print(any([1, 2, 3]))
print(any([0]))


def gen_function(n: int):
    while n >= 0:
        yield n
        n -= 1


gen_f = gen_function(2)
print(next(gen_f))  # 2
print(next(gen_f))  # 1
print(next(gen_f))  # 0
# print(next(gen_f))  # StopIteration Error

# ジェネレーターのループ
for i in gen_function(2):
    print(i)


nums = [1, 2, 3]

# 配列
arr: List[int] = [i for i in nums]

# ジェネレーター
gen1: Generator[int, Any, None] = (i for i in nums)
arr1: List[int] = list(gen1)


# デコレーター実装サンプル
def elapsed_time(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        v = f(*args, **kwargs)
        print(f"{f.__name__}: {time.time() - start}")
        return v

    return wrapper


class DecoratorSample:
    name: str

    def __init__(self, name: str):
        self.name = name

    @elapsed_time
    def getName(self) -> str:
        return self.name


decoratorSample = DecoratorSample("John")
decoratorSample.getName()
