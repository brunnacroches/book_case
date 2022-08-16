from src.models.book_repository import book_case_enrollment
from src.models.entities.book_case_class import BookCaseClass


class RegistryBookCaseController:
    def registry(self, book_case: str):
        try:
            book_case_count = book_case_enrollment.count_book_case()
            new_book_case_id = str(book_case_count + 1)

            new_book_case_id = BookCaseClass(new_book_case_id, book_case)
            book_case_enrollment.registry_book_case(new_book_case_id)

            return new_book_case_id
        except:
            return None
