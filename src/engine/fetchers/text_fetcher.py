class TextFetcher:
    def fetch_from_path(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            return ''.join(lines)