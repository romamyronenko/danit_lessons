def test_library_remove_book(library):
    library.remove_book("a")
    assert len(library._books) == 2
    assert not library.find_by_title("a")
