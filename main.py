import json
from random import randint
from typing import Dict, Final, List, Tuple, Union

from utils import inRange

# アスタリスクですべてインポート
# from utils import *

# 名前空有感 utils にすべての関数をインポート
# import utils

# テンプレートリテラル
foo: str = "foo"
bar: str = "bar"
print(f"{foo} {bar}")  # foo bar

# 連続代入
x, y, z = 0, 0, 0

# 定数（慣例）
MAX_CONNECTION: Final[int] = 10

# 数値区切り
unix_time: int = 1_000_000

# -1 で配列の後ろからアクセス
numbers: List[int] = [1, 2, 3, 4]
print(numbers[-1])  # 3

# array.pop は引数で位置を指定できる
# 指定しなければ最後の要素を取り出す
first_item: int = numbers.pop(0)
print(numbers)  # [2, 3, 3.5, 4]
print(first_item)  # 1

# array.remove は値を指定して要素を削除できる
# 同一値が複数あるは最初に発見した値のみ削除する
numbers.remove(4)
print(numbers)  # [2, 3, 3.5]

numbers.append(4)
numbers.append(4)
print(numbers)  # [2, 3, 3.5, 4, 4]
numbers.remove(4)
print(numbers)  # [2, 3, 3.5, 4]

# array.sort で並び替え
numbers = [1, 2, 3]
numbers.sort()
print(numbers)  # [1, 2, 3]

# reverse オプションで逆順に並び替え
numbers.sort(reverse=True)
print(numbers)  # [3, 2, 1]

# sorted 関数で非破壊的に並び替えできる
print(sorted(numbers))  # [1, 2, 3]
print(numbers)  # [3, 2, 1]

# reverse メソッドで配列を逆順に並び替える
numbers.reverse()

# 配列長
len(numbers)

# 配列をループ
for number in numbers:
    print(number)

# 数値の連番
for i in range(1, 5):
    print(i)  # 5 は出力されない

# range から配列を生成
print(list(range(1, 5)))  # [1, 2, 3, 4]

# range の第三引数で連番の間隔を指定できる
even_numbers: List[int] = list(range(2, 11, 2))
print(even_numbers)  # [2, 4, 6, 8, 10]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 省略表現
squares: List[int] = []
for i in range(1, 11):
    squares.append(i**2)

squares = [i**2 for i in range(1, 11)]

# 配列の slice
numbers = list(range(1, 11))
print(numbers[0:10])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:8])  # [4, 5, 6, 7, 8]

# 省略可
print(numbers[:8])  # [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[3:])  # [4, 5, 6, 7, 8, 9, 10]

# 負の数を指定すると後ろから指定できる
print(numbers[-3:])  # [8, 9, 10]

# 範囲外を指定してもエラーにならない
print(numbers[1000:])  # []
print(numbers[0:1000])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 配列のコピー
print(numbers[:])

# タプルは定数的に利用する
tuple: Tuple[int, int, int] = (1, 2, 3)
# tuple[0] = 1 # タプルは変更不可
tuple = (1, 2, 3)  # ただしタプルを格納した変数への再代入は可能

# 配列に含む
numbers = [1, 2, 3]
print(1 in numbers)
print(1 not in numbers)

# 空配列は Falsy
print(bool([]))


# 辞書（オブジェクト）
dict: Dict[str, Union[str, int]] = {"color": "red"}
print(dict)
print(dict["color"])
dict["size"] = 100

# get メソッドでアクセスすると第二引数にデフォルト値を設定できる
print(dict.get("color", "color is undefined."))  # red
print(dict.get("colr", "color is undefined."))  # color is undefined.

# JavaScript の Object.entries 相当
dict = {foo: 1, bar: 2}
print(dict.items())  # dict_items([('foo', 1), ('bar', 2)])
for key, value in dict.items():
    print(f"{key}={value}")

# 辞書をそのままループするとキーを取得できる
for key in dict:
    print(key)

# 上記と同等
for key in dict.keys():
    print(key)

print(dict.values())

# セット（集合）
arr: List[int] = [
    1,
    2,
    3,
    3,
    4,
    4,
    5,
]
print(set(arr))  # {1, 2, 3, 4, 5}

# セットから配列に変換
print(list(set(arr)))  # [1, 2, 3, 4, 5]

# 配列の比較
print([1] == [1])  # True
print([{foo: 1}] == [{foo: 1}])  # True

# 辞書の比較
print({foo: 1} == {foo: 1})  # True

# キャスト
print(str(21))
print(int("21"))
print(float("21"))

# 配列を空にする
arr = [1, 2, 3, 4, 5]
print(arr)
arr.clear()
print(arr)


# 関数定義
def greet(username: str = "NO NAME") -> None:
    """
    gree
    t"""
    print(f"Hello, {username}!!")


greet("World")

# キーワード引数
# 順序に依存しない + 可読性が上がる
greet(username="World")


def break_array(arr: List[int]) -> List[int]:
    arr.pop()
    return arr


# 配列の破壊を防ぐためにコピーを渡す
arr = [1, 2, 3]
break_array(arr[:])


def sample(foo: str, *args: int) -> None:  # 慣例的に args を利用する
    """
    可変長引数
    """
    print(foo)
    print(args)  # (1, 2, 3)


sample("foo", 1, 2, 3)


def foo1(_: str, **kwargs: int) -> None:  # 慣例的に kwargs を利用する
    """
    可変長キーワード引数
    """
    print(_)
    print(kwargs)  # (1, 2, 3)


foo1(_="_", foo=1, bar=2, baz=3)

print(inRange(1, 2, 3))  # 2


class Dog:
    """
    Class のサンプル
    """

    name: str
    is_sitting: bool

    def __init__(self, name: str) -> None:
        self.name = name
        self.is_sitting = False

    def bark(self) -> None:
        print(f"{self.name} said barked")

    def standUp(self) -> None:
        if self.is_sitting:
            print(f"{self.name} is already standing")
        else:
            self.is_sitting = False
            print(f"{self.name} is standing")

    def sit(self) -> None:
        self.is_sitting = True
        print(f"{self.name} is sitting down")


dog = Dog("John")
dog.sit()
dog.standUp()
dog.bark()


class Corgi(Dog):
    """
    継承
    """

    def __init__(self, name: str):
        super().__init__(name=name)


corgi = Corgi("Michel")

# 1 or 2 をランダムで表示する
print(randint(1, 2))

filename: str = "text.txt"
# ファイルの読み込み

with open(filename) as file_object:  # with 文を利用することで自動でオブジェクトを解放する
    contents: str = file_object.read()
print(contents.strip())

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

with open(filename) as file_object:
    lines: List[str] = [line.strip() for line in file_object.readlines()]

# 配列を結合
print("_".join(lines))

# ファイル書き込み
filename = "programming.txt"
# open の第二引数で読み込みモードを指定する
with open(filename, "w") as file_object:
    # ファイルは自動生成される
    file_object.write("I love programming.")

try:
    result = 5 / 0
    print(result)
except ZeroDivisionError:
    print("ZeroDivisionError occurred")
else:
    # try ブロックが成功した場合に else 句を通る
    print(result)

try:
    # ファイルエンコード指定
    with open("invalid_filename.txt", encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print("invalid_filename.txt not found.")

# 文字列分割. split の引数を未指定の場合は whitespace で分割
print("foo bar bar".split())

try:
    result = 5 / 0
    print(result)
except ZeroDivisionError:
    # pass 文を指定するとブロック内で何もしない
    # エラーを握り潰す
    pass
else:
    print(result)

# JSON 書き込み
numbers1: List[int] = list(range(1, 11))
with open("numbers.json", mode="w", encoding="utf-8") as f:
    json.dump(numbers, f)

# JSON 読み込み
with open("numbers.json", encoding="utf-8") as f:
    numbers2 = json.load(f)
print(numbers2)
