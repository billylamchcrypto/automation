from infra.base import Base


class Home(Base):

    def __init__(self, driver):
        # super.__init__(driver)
        super().__init__(driver)
        self.driver = driver

# aos element
    _lion_logo = ('id', '')

    def home_here(self):
        self.wait_visible(self._lion_logo)
