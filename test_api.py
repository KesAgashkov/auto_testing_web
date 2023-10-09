import yaml
import testpage



with open('testdata.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def test_search_old_article_by_title():
    result = testpage.get_full_articles().json()['data']
    result_title = [i['title'] for i in result]
    assert data["old_title_api"] in result_title, 'search old article FAIL'

def test_search_new_articles_by_description():
    add_art = testpage.append_new_article()
    full_art = testpage.get_full_articles().json()["data"]
    full_art = [i['description'] for i in full_art]
    assert (add_art.status_code == 200 and add_art.json()["description"] in full_art), \
        "Статья не найдена в списке статей"
