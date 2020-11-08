from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

# ARRANGE
URL = 'https://www.ecosia.org/'
query_string = "'yashaka selene'"
# користувач завантажує сторінку в браузері: https://www.ecosia.org/
# browser.config.hold_browser_open = True
browser.open(URL)

# ACTS
# користувач в поле пошуку вводить текст 'yashaka selene'
# користувач натискає Enter
s('[placeholder="Search the web to plant trees..."]').type(query_string).press_enter()

# користувач переходить по першому посиланню серед знайдених результатів
s('[class="result-snippet-link"]').click()

# ASSERT
# користувач перевіряє що на відкритій сторінці
# є три локальні посилання на https://github.com/yashaka/selene
print(ss('[href="/yashaka/selene"]'))
ss('[href="/yashaka/selene"]').should(have.size(3))

browser.quit()