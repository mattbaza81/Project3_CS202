import unittest
from proj3 import *


class TestStudent(unittest.TestCase):

    def test_heapify_up(self):
        heap = MinHeap([
            Node(5, "a"),
            Node(8, "b"),
            Node(2, "c")
        ])

        new_heap = heapify_up(heap, 2)

        self.assertEqual(new_heap.data[0].freq, 2)
        self.assertEqual(len(new_heap.data), 3)

    def test_insert(self):
        heap = MinHeap([])
        heap = insert(heap, Node(4, "a"))
        heap = insert(heap, Node(1, "b"))

        self.assertEqual(heap.data[0].freq, 1)
        self.assertEqual(len(heap.data), 2)

    def test_extract_min(self):
        heap = MinHeap([])
        heap = insert(heap, Node(3, "a"))
        heap = insert(heap, Node(1, "b"))
        heap = insert(heap, Node(2, "c"))

        new_heap, minimum = extract_min(heap)

        self.assertEqual(minimum.freq, 1)
        self.assertEqual(len(new_heap.data), 2)
        self.assertEqual(new_heap.data[0].freq, 2)

    def test_build_tree_shape(self):
        freq = count_frequency("aab")
        heap = create_priority_queue(freq)
        root = build_tree_from_queue(heap)
        self.assertEqual(root.freq, 3)
        self.assertIsNotNone(root.left)
        self.assertIsNotNone(root.right)

    def test_encode_decode_repeated_characters(self):
        s = "aaabbc"
        encoded, decoded, codes = huffman_encoding(s)
        self.assertEqual(decoded, s)
        self.assertEqual(len(codes), 3)
        self.assertTrue(len(encoded) > 0)

    def test_single_character(self):
        s = "aaaa"

        encoded, decoded, codes = huffman_encoding(s)
        self.assertEqual(decoded, s)
        self.assertEqual(codes["a"], "0")
        self.assertEqual(encoded, "0000")

    def test_empty_string(self):
        encoded, decoded, codes = huffman_encoding("")
        self.assertEqual(encoded, "")
        self.assertEqual(decoded, "")
        self.assertEqual(codes, {})


if __name__ == "__main__":
    unittest.main()