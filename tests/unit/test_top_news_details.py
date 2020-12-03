import top_news_details

def test_top_news_details_datatype():
    top_news_details.top_news_details()
    assert isinstance(top_news_details.notifications_list, list)

def test_top_news_details_returnedlength():
    top_news_details.top_news_details()
    assert len(top_news_details.notifications_list) > 0

def test_top_news_details_dismissedlist():
    top_news_details.top_news_details()
    assert len(top_news_details.dismissed_notifications) == 0
