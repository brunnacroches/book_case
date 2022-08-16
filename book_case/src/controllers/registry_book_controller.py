from typing import Dict
from src.models.book_repository import book_enrollment
from src.models.entities.book import book

class RegistrybookController:
    
    def registry(self, book_informations: Dict):
        try:
            class_registry = self.__get_book_class(book_informations["book_id"])
            new_book_id = self.__get_new_book_id()

            new_book = book(
                new_book_id,
                book_informations["book"],
                book_case_registry
            )
            book_enrollment.registry_book(new_book)

            return { "success": True, "book_registry": new_book }
        except Exception as exception:
            return { "success": False, "error": str(exception) }

        def __get_book_class(self, book_id: str) -> any:
            book_count = book_enrollment.count_bookren()
            new_book_id = str(book_count + 1)
            return new_book_id
