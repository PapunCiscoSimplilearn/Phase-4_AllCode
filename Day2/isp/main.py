from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass


class Fax(ABC):
    @abstractmethod
    def fax_document(self):
        pass


class BasicPrinter(Printer):
    def print_document(self):
        print("Printing document")


class MultiFunctionPrinter(Printer, Scanner, Fax):
    def print_document(self):
        print("Printing document")

    def scan_document(self):
        print("Scanning document")

    def fax_document(self):
        print("Sending fax")


def main():
    basic_printer = BasicPrinter()
    multifunction_printer = MultiFunctionPrinter()

    basic_printer.print_document()
    multifunction_printer.print_document()
    multifunction_printer.scan_document()
    multifunction_printer.fax_document()


if __name__ == "__main__":
    main()