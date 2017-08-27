import unittest
from .solution import get_mimes


class ExtensionsTest(unittest.TestCase):
    def test_simple(self):
        extensions = [
            'html text/html',
            'png image/png',
            'gif image/gif'
        ]

        files = [
            'animated.gif',
            'portrait.png',
            'index.html'
        ]

        correct = [
            'image/gif',
            'image/png',
            'text/html'
        ]

        self.assertEqual(get_mimes(extensions, files), correct)

    def test_unknown(self):
        extensions = [
            'txt text/plain',
            'xml text/xml',
            'flv video/x-flv'
        ]

        files = [
            'image.png',
            'animated.gif',
            'script.js',
            'source.cpp'
        ]

        correct = [
            'UNKNOWN',
            'UNKNOWN',
            'UNKNOWN',
            'UNKNOWN'
        ]

        self.assertEqual(get_mimes(extensions, files), correct)

    def test_correct_division(self):
        extensions = [
            'wav audio/x-wav',
            'mp3 audio/mpeg',
            'pdf application/pdf'
        ]

        files = [
            'a',
            'a.wav',
            'b.wav.tmp',
            'test.vmp3',
            'pdf',
            '.pdf',
            'mp3',
            'report..pdf',
            'defaultwav',
            '.mp3.',
            'final.'
        ]

        correct = [
            'UNKNOWN',
            'audio/x-wav',
            'UNKNOWN',
            'UNKNOWN',
            'UNKNOWN',
            'application/pdf',
            'UNKNOWN',
            'application/pdf',
            'UNKNOWN',
            'UNKNOWN',
            'UNKNOWN'
        ]

        self.assertEqual(get_mimes(extensions, files), correct)

    def test_case_consideration(self):
        extensions = [
            'png image/png',
            'TIFF image/TIFF',
            'css text/css',
            'TXT text/plain'
        ]

        files = [
            'example.TXT',
            'referecnce.txt',
            'strangename.tiff',
            'resolv.CSS',
            'matrix.TiFF',
            'lanDsCape.Png',
            'extract.cSs'
        ]

        correct = [
            'text/plain',
            'text/plain',
            'image/TIFF',
            'text/css',
            'image/TIFF',
            'image/png',
            'text/css'
        ]

        self.assertEqual(get_mimes(extensions, files), correct)

if __name__ == '__main__':
    unittest.main()
