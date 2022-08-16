from src.views.registry_book_view import RegistryBookViews
from src.controllers.registry_book_controller import RegistryBookController


def registry_book_process() -> None:
    registry_book_view = RegistryBookViews()
    registry_book_controller = RegistryBookController()

    # qual o  sentido de fazer estas chamadas aqui?
    book_informations = registry_book_view.registry_book_view()
    response = registry_book_controller.registry(book_informations)

    if response["success"]:
        registry_book_view.registry_book_success(response["book_registry"])
    else:
        registry_book_view.registry_book_fail(response["error"])
