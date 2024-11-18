import unittest
from list_counter import ListCounter

class TestListCounter(unittest.TestCase):
    def setUp(self):
        self.parser = ListCounter()

    def test_empty_html(self):
        self.parser.feed('')
        self.assertEqual(self.parser.max_list_count, 0)

    def test_single_list(self):
        html = """
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
        </ul>
        """
        self.parser.feed(html)
        self.assertEqual(self.parser.max_list_count, 3)

    def test_nested_lists(self):
        html = """
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <ul>
                <li>Nested 1</li>
                <li>Nested 2</li>
            </ul>
            <li>Item 3</li>
        </ul>
        """
        self.parser.feed(html)
        self.assertEqual(self.parser.max_list_count, 3)  # Should only count top-level items

    def test_multiple_lists(self):
        html = """
        <ul>
            <li>List1 Item1</li>
            <li>List1 Item2</li>
        </ul>
        <p>Some text</p>
        <ul>
            <li>List2 Item1</li>
            <li>List2 Item2</li>
            <li>List2 Item3</li>
        </ul>
        """
        self.parser.feed(html)
        self.assertEqual(self.parser.max_list_count, 3)

    def test_reset_between_feeds(self):
        html1 = "<ul><li>Item1</li><li>Item2</li></ul>"
        html2 = "<ul><li>Item1</li><li>Item2</li><li>Item3</li></ul>"
        
        self.parser.feed(html1)
        self.assertEqual(self.parser.max_list_count, 2)
        
        self.parser = ListCounter()  # Reset parser
        self.parser.feed(html2)
        self.assertEqual(self.parser.max_list_count, 3)


if __name__ == '__main__':
    unittest.main()