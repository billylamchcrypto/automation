from infra.base import Base


class Passcode(Base):

    def __init__(self, driver):
        # super.__init__(driver)
        super().__init__(driver)
        self.driver = driver

# aos element
    _p9 = ('id', 'co.mona.android.staging:id/keyboard9Btn')
    _p8 = ('id', 'co.mona.android.staging:id/keyboard8Btn')
    _p7 = ('id', 'co.mona.android.staging:id/keyboard7Btn')
    _p6 = ('id', 'co.mona.android.staging:id/keyboard6Btn')
    _p5 = ('id', 'co.mona.android.staging:id/keyboard5Btn')
    _p4 = ('id', 'co.mona.android.staging:id/keyboard4Btn')

    _passcode_title = ('id', 'co.mona.android.staging:id/mainCaptionTextView')

    def passcode_enter(self):
        self.click(self._p9)
        self.click(self._p8)
        self.click(self._p7)
        self.click(self._p6)
        self.click(self._p5)
        self.click(self._p4)

    def passcode_here(self):
        self.wait_visible(self._passcode_title)




