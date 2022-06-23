from utils import inRange
import unittest


class InRangeTestCase(unittest.TestCase):
    """
    慣例的に Test を含んだクラス名
    """

    max: int
    min: int

    def setUp(self) -> None:
        """
        テスト実行前のセットアップ関数
        """
        self.min = 2
        self.max = 4

    def test_min(self) -> None:
        """
        関数名が test_ で始まるメソッドは自動実行される
        """
        self.assertEqual(inRange(1, self.min, self.max), 2)

    def test_max(self) -> None:
        self.assertEqual(inRange(10, self.min, self.max), 4)

    def test_in_range(self) -> None:
        self.assertEqual(inRange(3, self.min, self.max), 3)


if __name__ == "__main__":
    unittest.main()
