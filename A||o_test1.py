class MyXpaths():
    locators = {
        'smartphones' : '//ul[@id="nav"]//a[@href="//allo.ua/ru/mobilnye-telefony-i-sredstva-svyazi/"]',
        'tv': '//ul[@id="nav"]//a[@href="//allo.ua/ru/televizory-i-mediapleery/"]',
        'naushniki' : '//ul[@id="nav"]//a[@href="//allo.ua/ru/naushniki-i-akustika/"]',
        'notebook' :   '//ul[@id="nav"]//a[@href="//allo.ua/ru/planshety-i-gadzhety/"]',
        'apple' : '//ul[@id="nav"]//a[@href = "//allo.ua/ru/aksessuary-apple/"]',
        'xiaomi': '//ul[@id="nav"]//a[@href="//allo.ua/ru/xiaomi-page/"]',
        'gadzhety' : '//ul[@id="nav"]//a[@href="//allo.ua/ru/gadzhety/"]',
        'tehnika' : '//ul[@id="nav"]//a[@href="//allo.ua/ru/bytovaya-tehnika/"]',
        'sport' : '//ul[@id="nav"]//a[@href="//allo.ua/ru/sport-i-zdorov-e/"]',
        'turizm' : '//ul[@id="nav"]//a[@href="//allo.ua/ru/turizm-i-rybalka/"]',
        'santehnika' : '//ul[@id="nav"]//a[@href="//allo.ua/ru/santehnika-i-remont/"]',
        'dom' : '//ul[@id="nav"]//a[@href="//allo.ua/ru/dom-sad-remont/"]',
        'detej' : '//ul[@id="nav"]//a[@href="//allo.ua/ru/tovary-dlja-detej/"]',
        'avtotovary' : '//ul[@id="nav"]//a[@href="//allo.ua/ru/avtotovary/"]',
        'ukrashenija' : '//ul[@id="nav"]//a[@href="//allo.ua/ru/chasy-i-ukrashenija/"]',
        'events': '//ul[@id="nav"]//a[@href="//allo.ua/ru/events-and-discounts/"]'

    }
    def smartphones_test(self):
        a= '//ul[@id="nav"]//a[@href="//allo.ua/ru/mobilnye-telefony-i-sredstva-svyazi/"]'
        a_1='smartphones'
        if self.locators.get(a_1) == a:
            print a_1, "link is correct"
        else:
            print a_1, "link is not correct"

    def tv_test(self):
        b= '//ul[@id="nav"]//a[@href="//allo.ua/ru/televizory-i-mediapleery/"]'
        b_1='tv'
        if self.locators.get(b_1) == b:
            print b_1, "link is correct"
        else:
            print b_1, "link is not correct"
    def naushniki_test(self):
        c = '//ul[@id="nav"]//a[@href="//allo.ua/ru/naushniki-i-akustika/"]'
        c_1 = 'naushniki'
        if self.locators.get(c_1) == c:
            print c_1, "link is correct"
        else:
            print c_1, "link is not correct"
    def notebook_test(self):
        d = '//ul[@id="nav"]//a[@href="//allo.ua/ru/planshety-i-gadzhety/"]'
        d_1 = 'notebook'
        if self.locators.get(d_1) == d:
            print d_1, "link is correct"
        else:
            print d_1, "link is not correct"
    def apple_test(self):
        e = '//ul[@id="nav"]//a[@href = "//allo.ua/ru/aksessuary-apple/"]'
        e_1 = 'apple'
        if self.locators.get(e_1) == e:
            print e_1, "link is correct"
        else:
            print e_1, "link is not correct"
    def xiaomi_test(self):
        f = '//ul[@id="nav"]//a[@href="//allo.ua/ru/xiaomi-page/"]'
        f_1 = 'xiaomi'
        if self.locators.get(f_1) == f:
            print f_1, "link is correct"
        else:
            print f_1, "link is not correct"
    def gadzhety_test(self):
        g = '//ul[@id="nav"]//a[@href="//allo.ua/ru/gadzhety/"]'
        g_1 = 'gadzhety'
        if self.locators.get(g_1) == g:
            print g_1, "link is correct"
        else:
            print g_1, "link is not correct"
    def tehnika_test(self):
        h = '//ul[@id="nav"]//a[@href="//allo.ua/ru/bytovaya-tehnika/"]'
        h_1 = 'tehnika'
        if self.locators.get(h_1) == h:
            print h_1, "link is correct"
        else:
            print h_1, "link is not correct"
    def sport_test(self):
        i = '//ul[@id="nav"]//a[@href="//allo.ua/ru/sport-i-zdorov-e/"]'
        i_1 = 'sport'
        if self.locators.get(i_1) == i:
            print i_1, "link is correct"
        else:
            print i_1, "link is not correct"
    def turizm_test(self):
        j = '//ul[@id="nav"]//a[@href="//allo.ua/ru/turizm-i-rybalka/"]'
        j_1 = 'turizm'
        if self.locators.get(j_1) == j:
            print j_1, "link is correct"
        else:
            print j_1, "link is not correct"
    def santehnika_test(self):
        k = '//ul[@id="nav"]//a[@href="//allo.ua/ru/santehnika-i-remont/"]'
        k_1 = 'santehnika'
        if self.locators.get(k_1) == k:
            print k_1, "link is correct"
        else:
            print k_1, "link is not correct"
    def dom_test(self):
        l = '//ul[@id="nav"]//a[@href="//allo.ua/ru/dom-sad-remont/"]'
        l_1 = 'dom'
        if self.locators.get(l_1) == l:
            print l_1, "link is correct"
        else:
            print l_1, "link is not correct"
    def detej_test(self):
        m = '//ul[@id="nav"]//a[@href="//allo.ua/ru/tovary-dlja-detej/"]'
        m_1 = 'detej'
        if self.locators.get(m_1) == m:
            print m_1, "link is correct"
        else:
            print m_1, "link is not correct"
    def avtotovary_test(self):
        n = '//ul[@id="nav"]//a[@href="//allo.ua/ru/avtotovary/"]'
        n_1 = 'avtotovary'
        if self.locators.get(n_1) == n:
            print n_1, "link is correct"
        else:
            print n_1, "link is not correct"
    def ukrashenija_test(self):
        o = '//ul[@id="nav"]//a[@href="//allo.ua/ru/chasy-i-ukrashenija/"]'
        o_1 = 'ukrashenija'
        if self.locators.get(o_1) == o:
            print o_1, "link is correct"
        else:
            print o_1, "link is not correct"
    def events_test(self):
        p = '//ul[@id="nav"]//a[@href="//allo.ua/ru/events-and-discounts/"]'
        p_1 = 'events'
        if self.locators.get(p_1) == p:
            print p_1, "link is correct"
        else:
            print p_1, "link is not correct"

test = MyXpaths()

test.smartphones_test()
test.tv_test()
test.naushniki_test()
test.notebook_test()
test.apple_test()
test.xiaomi_test()
test.gadzhety_test()
test.tehnika_test()
test.sport_test()
test.santehnika_test()
test.dom_test()
test.detej_test()
test.events_test()
