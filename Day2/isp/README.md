# Interface Segregation Principle (ISP)

Clients should not be forced to depend on methods they do not use. Prefer smaller interfaces focused on specific responsibilities over one large interface.

## Printer example

A single machine interface requiring printing, scanning, and faxing forces a basic printer to implement operations it cannot support, often by raising `NotImplementedError`.

Here, `Printer`, `Scanner`, and `Fax` are separate interfaces. `BasicPrinter` implements only printing, while `MultiFunctionPrinter` implements all three. This avoids unnecessary implementations and makes the design more flexible and easier to maintain.

In an employee management application, payroll, attendance, and leave management can similarly expose separate interfaces instead of requiring every component to implement every operation.

Run the example from the workspace root:

```bash
python3 Day2/isp/main.py
```

Expected output:

```text
Printing document
Printing document
Scanning document
Sending fax
```