class MockDB:
    class Model:
        pass

    class Column:
        def __init__(self, *args, **kwargs):
            pass

    class Integer:
        def __init__(self, *args, **kwargs):
            pass

    class String:
        def __init__(self, *args, **kwargs):
            pass

    class ForeignKey:
        def __init__(self, *args, **kwargs):
            pass

    class relationship:
        def __init__(self, *args, **kwargs):
            pass

    class backref:
        def __init__(self, *args, **kwargs):
            pass

    def session_add(self, obj):
        pass

    def session_commit(self):
        pass

db = MockDB()
