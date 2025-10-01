import allure

from elements.base_element import BaseElement


class FileInput(BaseElement):
    @property
    def type_of(self)->str:
        return 'file'

    def set_input_files(self, file: str,  nth: int = 0, **kwargs):
        with allure.step(f'Setting {self.type_of} "{self.name}" to {file}'):
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file)
