from infra.base import Base


class Passcode(Base):

    def __init__(self, driver):
        # super.__init__(driver)
        super().__init__(driver)
        self.driver = driver

# aos element
    _p9 = ('id', '3u7')
    _p8 = ('id', 'v3d')
    _p7 = ('id', '9t6')
    _p6 = ('id', '7u1')
    _p5 = ('id', 'ke8')
    _p4 = ('id', '331')

    def passcode_enter(self):
        self.click(self._p9)
        self.click(self._p8)
        self.click(self._p7)
        self.click(self._p6)
        self.click(self._p5)
        self.click(self._p4)

    def passcode_here(self):
        self.wait_visible(self._p9)




