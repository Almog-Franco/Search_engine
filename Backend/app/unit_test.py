from search_entity import SearchEntity


def test_class():
    test = SearchEntity("Word",3)
    assert test is not None


def test_search_word():
    data_lst = []
    test = SearchEntity("Test",3)
    res = test.search_word()
    assert len(res["data"]) > 0

def test_search_pic():
    data_lst = []
    test = SearchEntity("Test",3)
    res = test.search_pic()
    assert len(res["data"]) > 0

def test_search_video():
    data_lst = []
    test = SearchEntity("Test",3)
    res = test.search_videos()
    assert len(res["data"]) > 0
