from typing import Dict
from src.models.book_repository import book_enrollment


class ShowBookController:
    def show(self, book_name: str):
        try:
            book_registry = self.__search_book_registry(book_name)
            registry = self.__format_registry_info(book_registry)
            return {"success": True, "registry": registry}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __search_book_registry(self, book_name: str) -> any:
        book_registry = book_enrollment.get_book(book_name)
        if book_registry is None:
            raise Exception("Livro não encontrado!")

        return book_registry

    def __format_registry_info(self, book_registry: any):
        return {
            "id": book_registry.id,
            "name": book_registry.name,
        }
