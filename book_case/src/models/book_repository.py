class __BookEnrollment:
    def __init__(self) -> None:
        self.book = []

    def count_book(self) -> int:
        return len(self.book)

    def registry_book(self, book: any) -> None:
        self.book.append(book)

    def get_book(self, book_name: str) -> any:
        for registry in self.book:
            if registry.name == book_name:
                return registry

            return None


book_enrollment = __BookEnrollment()
