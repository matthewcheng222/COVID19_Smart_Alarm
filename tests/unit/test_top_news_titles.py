import top_news_titles

def test_top_news_titles_outputtype():
    assert isinstance(top_news_titles.top_news_titles(), str)

def test_top_news_titles_outputlength():
    assert len(top_news_titles.top_news_titles()) > 0

def test_top_news_titles_outputuppercase():
    assert top_news_titles.top_news_titles()[0].isupper()

def test_top_news_titles_outputword():
    assert top_news_titles.top_news_titles()[0:12] == "Here are the"
