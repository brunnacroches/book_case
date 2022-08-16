from src.views.show_book_view import ShowBookViews
from src.controllers.show_book_controller import ShowBookController

def show_book_process() -> None:
  show_book_view = ShowBookViews()
  show_book_controller = ShowBookController()

  book_informations = show_book_view.show_book_view()
  response = show_book_controller(book_informations)

  if response["success"]: show_book_view.show_book_success(response["registry"])
  else: show_book_view.show_book_fail(response["error"])