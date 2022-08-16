from src.views.registry_book_case_process_view import RegistryBookCaseViews
from src.controllers.registry_book_case_process_controller import (
    RegistryBookCaseController,
)


def registry_book_case_process() -> None:
    registry_book_case_process_view = RegistryBookCaseViews()
    registry_book_case_process_controller = RegistryBookCaseController()

    book_case = registry_book_case_process_view.registry_book_case()
    new_book_case = registry_book_case_process_controller.registry(book_case)

    if new_book_case is not None:
        registry_book_case_process_view.resgistry_book_case_success(new_book_case)
    else:
        registry_book_case_process_controller.registry_book_case_fail()
