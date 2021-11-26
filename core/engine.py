from pathlib import Path


class DisplayablePath(object):
    display_filename_prefix_middle = '├──'
    display_filename_prefix_last = '└──'
    display_parent_prefix_middle = '    '
    display_parent_prefix_last = '│   '

    def __init__(self, path, parent_path, is_last):
        self.path = Path(str(path))
        self.parent = parent_path
        self.is_last = is_last
        self.depth = self.parent.depth + 1 if self.parent else 0
        self.json_info = {
            'name': self.path.name,
            'full_path': str(path),
            'type': self.file_type,
            'size': self.file_size,
            'items': list(),
        }

    @classmethod
    def make_tree(cls, root, parent=None, is_last=False, criteria=None):
        root = Path(str(root))
        criteria = criteria or cls._default_criteria

        displayable_root = cls(root, parent, is_last)
        yield displayable_root
        try:
            children = sorted(
                [path for path in root.iterdir() if criteria],
                key=lambda s: str(s).lower(),
            )

            for count, path in enumerate(children, start=1):
                is_last = count == len(children)
                if path.is_dir():
                    yield from cls.make_tree(path,
                                             parent=displayable_root,
                                             is_last=is_last,
                                             criteria=criteria)
                else:
                    yield cls(path, displayable_root, is_last)
        except FileNotFoundError:
            print(f'Path {root} not found.')

    @classmethod
    def _default_criteria(cls, path):
        return True

    @property
    def display_name(self):
        if self.path.is_dir():
            return self.path.name + '/'
        return self.path.name

    @property
    def file_type(self):
        if self.path.is_dir():
            return 'folder'
        return self.path.suffix

    @property
    def file_size(self):
        return self.path.stat().st_size

    def displayable(self):
        if self.parent is None:
            return self.display_name

        _filename_prefix = (self.display_filename_prefix_last
                            if self.is_last
                            else self.display_filename_prefix_middle)

        parts = ['{!s} {!s}'.format(_filename_prefix,
                                    self.display_name)]

        parent = self.parent
        while parent and parent.parent is not None:
            parts.append(self.display_parent_prefix_middle
                         if parent.is_last
                         else self.display_parent_prefix_last)
            parent = parent.parent

        return ''.join(reversed(parts))

    def json_data(self):
        return self.json_info

    def append_item(self, item):
        self.json_info['items'].append(item.json_data())
