import unittest


def split_names(names):
    male, female = [], []
    for name in names:
        if isinstance(name, str):
            if name[-1] == 'a':
                female.append(name)
            else:
                male.append(name)
    return {"male": male, "female": female}


class SplitNamesTest(unittest.TestCase):
    def testMale(self):
        self.assertEqual(split_names(["Jan", "Andrzej", "Piotr"]),
                         {"male": ["Jan", "Andrzej", "Piotr"], "female": []})

    def testFemale(self):
        self.assertEqual(split_names(["Zofia", "Ania"]),
                         {"male": [], "female": ["Zofia", "Ania"]})

    def testInFemale(self):
        self.assertIn("Karolina", split_names(
            ["Zofia", "Ania", "Karolina"])["female"])

    def testMixed(self):
        self.assertEqual(split_names(["Jan", "Ania"]),
                         {"male": ["Jan"], "female": ["Ania"]})

    def testMaleNotInFemale(self):
        self.assertNotIn("Jan", split_names(
            ["Zofia", "Ania", "Zofia", "Andrzej", "Piotr"])["female"])


if __name__ == '__main__':
    unittest.main()
